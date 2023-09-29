from django.db import models


# Create your models here.
class Coment(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=500, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=50, default="Firma")

    def __str__(self):
        return self.nombre
