from logging import basicConfig

from invoke import Collection

from .models import models

basicConfig(format="%(asctime)s %(levelname)s [%(name)s] %(message)s")

ns = Collection(models)
