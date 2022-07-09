from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class SecretWords(models.Model):
  word = models.CharField(max_length=50)