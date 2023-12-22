from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#Crear Usuarios
class CrearUsuario(BaseUserManager):
    def crear_usuario(self, nombre_usuario, correo_usuario, password_usuario = None, **extra_fields):
        if not correo_usuario:
            raise ValueError('El correo electronico es obligatorio')
        if not nombre_usuario:
            raise ValueError('El nombre de usuario es obligatorio')
        email_usuario =  self.normalize_email(correo_usuario)
        usuario = self.model(correo_usuario = email_usuario, nombre_usuario = nombre_usuario, **extra_fields)
        usuario.set_password(password_usuario)
        usuario.save(using=self._db)
        return usuario
    
#Usuarios
class Usuarios(AbstractBaseUser, PermissionsMixin):
    correo_usuario = models.EmailField(unique=True)
    nombre_usuario = models.CharField(max_length=30, unique=True)
    esta_activa = models.BooleanField(default=True)
    objects = CrearUsuario()
    USERNAME_FIELD = 'correo_usuario'
    REQUIRED_FIELDS = ['nombre_usuario']
    def __str__(self):
        return self.correo_usuario
