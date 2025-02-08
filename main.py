#GestióndeClientesyMascotasReto 2 - Gestión de Veterinaria usandoProgramación Orientada a Objetos (Terminal)
#Integrantes: Daniela Palechor y Ever Lopez
from abc import ABC, abstractmethod
from datetime import datetime
import re   #libreria para crear patrones y realizar comparaciones

#Variables globales
clientes = []
mascotas = []
servicios = ["consulta", "vacunación", "esterilizacion", "spa"]
#clientes = [
#    Cliente(1, "Daniela Palechor", "3124567852", "calle 5 Nro. 26-45"),
#    Cliente(2, "Andres Agudelo", "3145824653", "calle 4 Nro. 23-36")
#]
#mascotas = []
"""mascotas = [
    Mascota(1, "Toby", "Perro", "Pastor Aleman", "3"),
    Mascota(2, "lucita", "Perro", "Crillo", "5")
]   """



























    class Mascota:             #Se crea una clase mascota 
        id_counter = 1                                           #se iniciara el contador para mascotas en 1
        def __init__(self, nombre, especie, raza, edad):
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinica = []   # cada mascota tiene una historia clinica
            SistemaVeterinaria.Mascota.id_counter += 1

        def agregar_cita(self, cita):
            self.historia_clinica.append(cita)

        def mostrar_historial(self):                         #funcion para mostrar la información de una cita
            if not self.historia_clinica:
                print(f"No hay citas registradas para {self.nombre}")
            else:
                print(f"\nHistorial de las citas para {self.nombre}")
                for cita in self.historia_clinica:
                    print(f" {cita.id}- {cita.fecha} a las {cita.hora}, servicio: {cita.servicio}, veterinario: {cita.veterinario}")

        #def actualizar_cita(self,cita):
        """def actualizar_cita(self, **kwargs):
            for clave, valor in kwargs.items():
                if hasattr(self, clave):
                    setattr(self, clave, valor)"""
