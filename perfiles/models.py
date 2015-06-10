from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):

	TIPOS_DE_USUARIOS = (
			(TECN, 'TECNICO'),
			(COM, 'COMERCIAL'),
			(CALL, 'AGENTE DE CALL CENTER'),
		)

	usuario = models.OneToOneField(User)
	perfil = models.CharField(max_length=4, choices=TIPOS_DE_USUARIOS, default=TECN)