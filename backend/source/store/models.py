from utils.hshlib import get_hsh
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=120, default=None)
    hsh = models.CharField(
        max_length=128, 
        default=get_hsh,
        unique=True,
        db_index=True, 
    )

    def __str__(self):
        return self.name
