from django.db import models


class Account(models.Model):
    name = models.CharField()

    def __str__(self):
        return f'{{"name": "{self.name}"}}'
