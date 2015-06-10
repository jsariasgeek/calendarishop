from django.db import models

class Tienda(models.Model):
	ship_to=models.CharField(max_length=10, primary_key=True)
	nombre = modes.CharField(max_length=60)