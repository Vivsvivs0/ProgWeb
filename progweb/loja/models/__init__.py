from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .Fabricante import Fabricante
from .Categoria import Categoria
from .Produto import Produto
