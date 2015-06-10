from django.db import models
from tiendas.models import Cita

class Cita(models.Model):
	ship_to = models.ForeignKey(Cita)
	nombre = models.CharField(max_length=60)
	email = models.EmailField()
	telefono = models.CharField(max_length=10)
	fecha = models.DateField()
	hora = models.TimeField(help_text='Formato 24 Horas')



#
#Perfiles de Usuario App
#  


# Vendedor
# Agente de Call Center
# Tecnico
#
#
#
#
#
#