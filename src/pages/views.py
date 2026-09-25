import os

from django import get_version
from django.conf import settings
from django.shortcuts import render


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + "PROBANDO CAMBIOS" ,
        "python_ver": os.environ["PYTHON_VERSION"] + "MAS CAMBIOS",
    }

    return render(request, "pages/home.html", context)

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.deposito = self.saldo + cantidad
        self.saldo = self.deposito
    def retirar(self, cantidad):
        if self.saldo < cantidad:
            print("No hay saldo suficiente")
        else:
            self.retiro = self.saldo - cantidad
            self.saldo = self.retiro


def home(request):
    cuenta1 = Cuenta("Iave", 15000)
    cuenta1.depositar(1000)
    cuenta1.retirar(500)

    return render(request, "pages/home.html", {"cuenta" : cuenta1})

class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel 
    def recibir_danio(self, cantidad):
        if cantidad < self.vida:
            self.vida = self.vida - cantidad
        elif cantidad >= self.vida:
            self.vida = (0)
    def curarse(self, cantidad):
        if self.vida + cantidad <= 100:
            self.vida = self.vida + cantidad
        else:
            self.vida = 100
    def subir_nivel(self):
        self.subir_nivel =+ 1

def home(request):
    personaje1 = Personaje("Iave", 80, 1)
    personaje1.recibir_danio(30)
    personaje1.curarse(50)
    personaje1.subir_nivel()

    return render(request, "pages/home.html", {"personaje1" : personaje1})
