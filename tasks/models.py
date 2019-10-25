import logging
from csv import DictReader
from keyword import iskeyword
from pathlib import Path
from pprint import pprint
from re import compile, sub

from invoke import Collection, task

index_pattern = compile(r"^\w+ID$")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@task
def generate(c):
    models = []
    outfile = Path.cwd().joinpath("baseball", "db", "models.py").resolve()

    for name, reader in _data_readers():
        model = {"name": name}
        logger.info("Generating model {}".format(model["name"]))
        rows = [row for row in reader]

        model["fields"] = {
            field: _get_column_type_for_field(field, rows)
            for field in reader.fieldnames
        }

        models.append(model)

    import_types = list(
        set().union(*map(lambda model: set(model["fields"].values()), models)))
    import_types.remove(None)

    output = ("from sqlalchemy import {}\n\n"
              "from .base import Base\n\n\n"
              "{}\n").format(
                  ", ".join(sorted(["Column", *import_types])),
                  "\n\n\n".join([_model_to_class(model) for model in models]))

    with outfile.open("w") as file:
        file.write(output)


@task
def reset(c):
    from baseball.db import engine_path

    logger.info("Resetting database")
    engine_path.unlink(missing_ok=True)


@task(pre=[reset])
def load(c):
    from baseball.db import get_engine, models
    from sqlalchemy import func, select

    engine = get_engine()

    for name, reader in _data_readers():
        logger.info("Loading {} data".format(name))
        table = eval("models.{}.__table__".format(name))

        engine.execute(table.insert(), [{
            column: _cast_value_for_insert(row[column], table.columns[column])
            for column in row
        } for row in reader])

        statement = select([func.count()]).select_from(table)
        count = engine.execute(statement).fetchone()[0]
        logger.info("Loaded {}, {} rows".format(name, count))


def _cast_value_for_insert(value, column):
    if column.type.__class__.__name__ == "Boolean":
        return value == "Y"

    if value == "":
        return None

    return value


def _data_readers():
    datadir = Path.cwd().joinpath("baseballdatabank", "core").resolve()

    for path in sorted(datadir.glob("*.csv")):
        with path.open("r") as file:
            yield path.stem, DictReader(file)


def _get_column_spec_for_field(name: str, column_type: str):
    args = []

    if not name.isidentifier():
        name = sub(r"[^0-9A-Za-z_]", "_", name)

    if not _is_valid_variable_name(name):
        args.append("\"{}\"".format(name))
        name = "_{}".format(name)

    args.append("{}".format(column_type))

    if index_pattern.match(name):
        args.append("index=True")

    notes = ""
    if column_type is None:
        notes = " # TODO Manually specify column type"

    return "{} = Column({}){}".format(name, ", ".join(args), notes)


def _get_column_type_for_field(field: str, rows: list):
    values = set(
        map(lambda r: r, (row[field].strip()
                          for row in rows if not row[field].strip() == "")))

    if len(values) == 0:
        logger.warn("Could not determine type for field {}".format(field))
    elif all(map(str.isdigit, values)):
        return "Integer"
    elif all(
            map(lambda v: all(map(str.isdigit, v.split(".", maxsplit=1))),
                values)):
        return "Numeric"
    elif all(map(lambda v: v[0] in ["Y", "N"], values)):
        return "Boolean"
    else:
        return "String"


def _is_valid_variable_name(name: str):
    try:
        eval("type({})".format(name))
        return False
    except (NameError, SyntaxError):
        return name.isidentifier() and not iskeyword(name)


def _model_to_class(model):
    return "class {}(Base):\n{}".format(
        model["name"], "\n".join([
            "    {}".format(
                _get_column_spec_for_field(field, model["fields"][field]))
            for field in model["fields"]
        ]))


models = Collection("models")
models.add_task(generate)
models.add_task(load)
models.add_task(reset)
