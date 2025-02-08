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

#clases principales
class SistemaVeterinaria:     # se crea una clase llamado SistemaVeterianaria

    class Persona:            # se crea una clase Persona
        id_counter = 1                                          #se iniciara el contador para personas en 1
        def __init__(self, nombre, contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre                                # variable que almacenara el nombre de la persona
            self.contacto = contacto                            # variable que almacenara el telefono de la persona
            SistemaVeterinaria.Persona.id_counter += 1          # el contador se autoincrementara a medida que se cree una persona

    class Cliente(Persona):    #se crea una clase cliente que hereda de la clase Persona
        def __init__(self, nombre, contacto, direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []   # el cliente tiene vinculada una mascota   #ojo

        #def agregar_cliente(self, cliente):
            #self.cliente.append(cliente)
        
        def agregar_mascota(self, mascota):
            self.mascotas.append(mascota)              #se quito self.mascota

        def mostrar_informacion(self):
            return f"cliente: {self.nombre}, contacto{self.contacto}, direccion: {self.direccion}"  # función para mostrar informacion del cliente 

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

    class Cita:                #Se crea una clase cita          
        id_counter = 1                      #funcion que inicializa las citas en 1 a medida que se van creando
        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterinaria.Cita.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario  
            SistemaVeterinaria.Cita.id_counter += 1            #para incrementar las citas en 1 a medida que se crean

        def actualizar_cita(self, **kwargs):
            for clave, valor in kwargs.items():
                if hasattr(self, clave):
                    setattr(self, clave, valor)

#Funciones del sistema, definicion de las subclases
def validarEntradaTexto(texto):            #funcion que me permite crear un patron y realizar comparaciones de solo texto
    patron ="[a-z áéíóú]+$"  
    if re.match(patron, texto):
        return True
    else:
        print("La entrada no es valida, solo se permiten letras y espacios")
        return False

def validarEntradaalfnum(texto):           #funcion que me permite crear un patron para validar entradas de letras, números y espacios
    patron ="[a-z 0-9#-áéíóú]+$"  #patron ="[a-zA-Z0-9_]+$"
    if re.match(patron, texto):
        return True
    else:
        print("La entrada no es valida, solo se permiten letras, numeros, espacios # y -")
        return False
    
def validarFecha(fecha):                   #funcion que me permite crear un patron para validar entradas de solo numeros y - para las fechas
    patron ="[0-9-]+$"
    if re.match(patron, fecha):
        return True
    else:
        return False

def validarFechaNueva(fecha):              ##funcion que me permite crear un patron para validar entradas de solo numeros, - y espacios para las fechas nuevas
    patron ="[0-9- ' ']+$"
    if re.match(patron, fecha):
        return True
    else:
        return False
    
def validarHora(hora):                     #funcion que me permite crear un patron para validar entradas de solo numeros y : para las horas
    patron ="[0-9:]+$"
    if re.match(patron, hora):
        return True
    else:
        return False
def validarHoraNueva(hora):                #funcion que me permite crear un patron para validar entradas de solo numeros, : y espacios para las horas nuevas
    patron ="[0-9: ' ']+$"
    if re.match(patron, hora):
        return True
    else:
        return False

