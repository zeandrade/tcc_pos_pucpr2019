from django.contrib import admin

# Register your models here.
from .models import Registro, Atuacao

admin.site.register(Registro)
admin.site.register(Atuacao)
