import logging
from csv import DictReader
from keyword import iskeyword
from pathlib import Path
from pprint import pprint
from re import compile, sub

from invoke import Collection, task

index_pattern = compile(r"^\w+ID$")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@task
def generate(c):
    models = []
    datadir = Path.resolve(
        Path.joinpath(Path.cwd(), "baseballdatabank", "core"))

    for path in sorted(datadir.glob("*.csv")):
        model = {"name": path.stem}
        logger.info("Generating model {}".format(model["name"]))

        with path.open("r") as file:
            reader = DictReader(file)
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

    outfile = Path.resolve(
        Path.joinpath(Path.cwd(), "baseball", "db", "models.py"))

    with outfile.open("w") as file:
        file.write(output)


def _get_column_spec_for_field(name: str, column_type: str):
    args = []

    if not _is_valid_variable_name(name):
        args.append("\"{}\"".format(name))
        name = sub(r"[^0-9A-Za-z_]", "_", name)

        if not _is_valid_variable_name(name):
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
