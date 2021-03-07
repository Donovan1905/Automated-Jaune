from django.db import models

class Kid(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Jaune(models.Model):
    quantity = models.IntegerField()
    kid = models.ForeignKey(
        'Kid',
        on_delete=models.CASCADE
    )
