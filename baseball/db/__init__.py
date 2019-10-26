from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..utils.singleton import Singleton
from . import base, models

DEFAULT_ENGINE_PATH = Path.cwd().joinpath("baseball.sqlite3").resolve()
engine_path = DEFAULT_ENGINE_PATH


class _Engine(metaclass=Singleton):
    def __init__(self, engine_path=DEFAULT_ENGINE_PATH):
        self._engine_path = "sqlite:///{}".format(engine_path)
        self.engine = create_engine(self._engine_path)
        self.Session = sessionmaker(bind=self.engine)

        base.Base.metadata.create_all(self.engine)


def get_engine():
    return _Engine().engine


def Session():
    return _Engine().Session()
