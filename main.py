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


def programar_cita():                      # funcion para programar una cita, validando cada campo y evitando que se cometan errores o malos ingresos
    conpro1 = True
    conpro2 = True
    conpro3 = True
    conpro4 = True
    conpro5 = True
    conpro6 = True
    while conpro1 == True:
        cliente_id = input("Ingrese el ID del cliente: ").strip()
        if not cliente_id:
            cliente_id = input("Ingrese el ID del cliente: ").strip()
        #validinicli = cliente_idini.isdigit()
        elif cliente_id.isdigit():
            cliente_id = int(cliente_id)
            cliente = next((c  for c in clientes if c.id == cliente_id), None)
            if not cliente:
                print ("Cliente no encontrado, debe registrarse. ")
                return
            else:
                print(f"El ID: {cliente.id} pertenece al cliente {cliente.nombre}")
                #mascota_idini = input("Ingrese el ID de la mascota: ").strip()
                conpro1 = False
                while conpro2 == True:
                    mascota_id = input("Ingrese el ID de la mascota: ").strip()
                    if not mascota_id:
                        mascota_id = input("Ingrese el ID de la mascota: ").strip()
                    elif mascota_id.isdigit():
                        mascota_id = int(mascota_id)
                        mascota = next((m  for m in mascotas if m.id == mascota_id), None)   #se modifico cliente.mascota
                        if not mascota:
                            print ("La Mascota no fue encontrada, debe registrarla. ")
                            return
                        else:
                            print(f"El ID {mascota_id} pertenece a la mascota {mascota.nombre}")
                            #fecha = input("Ingrese una fecha para la consulta (AAAA-MM-DD): ").strip()
                            conpro2 = False
                            while conpro3 == True:
                                fecha = input("Ingrese una fecha para la consulta (AAAA-MM-DD): ").strip()
                                if not fecha:
                                    fecha = input("Ingrese una fecha para la consulta no se aceptan espacios (AAAA-MM-DD): ").strip()
                                else:
                                    valfecha = validarFecha(fecha)
                                    if valfecha == True:
                                        try:
                                            datetime.strptime(fecha, "%Y-%m-%d")
                                            conpro3 = False                                 #verificar
                                            while conpro4 ==True:
                                                hora= input("Ingrese la hora para la consulta (HH:MM): ").strip()
                                                if not hora:
                                                    hora= input("Ingrese la hora para la consulta (HH:MM): ").strip()
                                                else:
                                                    valhora = validarHora(hora)
                                                    if valhora == True:
                                                        try:
                                                            datetime.strptime(hora, "%H:%M")
                                                            conpro4 = False
                                                            while conpro5 == True:
                                                                servicio = input("Elija el tipo de servicio (consulta, vacunación, esterilizacion, spa): ").strip()
                                                                if not servicio:
                                                                    servicio = input("Elija el tipo de servicio (consulta, vacunación, esterilizacion, spa): ").strip()
                                                                elif validarEntradaTexto(servicio):
                                                                    #veterinario =  input("Ingrese el nombre del veterinario: ").strip()
                                                                    conpro5 = False
                                                                    while conpro6 == True:
                                                                        veterinario =  input("Ingrese el nombre del veterinario: ").strip()
                                                                        if not veterinario:
                                                                            veterinario =  input("Ingrese el nombre del veterinario: ").strip()
                                                                        elif validarEntradaTexto(veterinario):
                                                                            cita = SistemaVeterinaria.Cita(fecha, hora, servicio, veterinario)
                                                                            mascota.agregar_cita(cita)
                                                                            #mascota.agregar_al_historial(cita)
                                                                            print(f"¡cita programada con exito!, ID: {cita.id}")
                                                                            conpro6 = False
                                                                        else:
                                                                            veterinario =  input("Ingrese el nombre del veterinario: ").strip()
                                                                else: 
                                                                    servicio = input("Elija un servicio valido (consulta, vacunación, esterilizacion, spa): ").strip()
                                                        except:
                                                            hora= input("Ingrese una hora con el formato solicitado (HH-MM): ").strip()
                                                    else:
                                                        hora= input("Ingrese una hora correcta para la consulta (HH-MM): ").strip()      
                                        except:
                                            print("Ingrese una fecha con el formato solicitado (AAAA-MM-DD)")
                                    else:
                                        fecha = input("Ingrese una fecha correcta para la consulta (AAAA-MM-DD): ").strip()
        else:
            cliente_id = input("Ingrese un ID valido del cliente: ").strip()
       

def consultar_historial():                 #funcion para consultar el historial de una mascota
    print("===============Consultar Historial de citas=====================")
    conhis1 = True
    conhis2 = True
    while conhis1 == True:
        cliente_id = input("Ingrese el ID del cliente: ").strip()
        if not cliente_id:
            cliente_id = input("Ingrese el ID del cliente: ").strip()
        #validinicli = cliente_idini.isdigit()
        elif cliente_id.isdigit():
            cliente_id = int(cliente_id)
            cliente = next((c  for c in clientes if c.id == cliente_id), None)
            if not cliente:
                print ("Cliente no encontrado, debe registrarse. ")
                return
            else:
                print(f"El ID: {cliente.id} pertenece al cliente {cliente.nombre}")
                #mascota_idini = input("Ingrese el ID de la mascota: ").strip()
                conhis1 = False
                while conhis2 == True:
                    mascota_id = input("Ingrese el ID de la mascota: ").strip()
                    if not mascota_id:
                        mascota_id = input("Ingrese el ID de la mascota: ").strip()
                    elif mascota_id.isdigit():
                        mascota_id = int(mascota_id)
                        mascota = next((m  for m in mascotas if m.id == mascota_id), None)   
                        if not mascota:
                            print ("La Mascota no fue encontrada, debe registrarla. ")
                            return
                        else:
                            print(f"El ID {mascota_id} pertenece a la mascota {mascota.nombre}")
                            conhis2 = False
                            mascota.mostrar_historial()
        else:
            cliente_id = input("Ingrese un ID del cliente valido: ").strip()
                        
def actualizar_cita():                     # funcion para actualizar una cita
    print("===============Actualización de citas=====================")
    conact1 = True
    conact2 = True
    conact3 = True
    conact4 = True
    conact5 = True
    conact6 = True
    conact7 = True
    while conact1 == True:
        cliente_id = input("Ingrese el ID del cliente: ").strip()
        if not cliente_id:
            cliente_id = input("Ingrese el ID del cliente: ").strip()
        elif cliente_id.isdigit():
            cliente_id = int(cliente_id)
            cliente = next((c  for c in clientes if c.id == cliente_id), None)
            if not cliente:
                print ("Cliente no encontrado, debe registrarse. ")
                return
            else:
                print(f"El ID: {cliente.id} pertenece al cliente {cliente.nombre}")
                conact1 = False
        else:
            cliente_id = input("Ingrese un ID valido del cliente: ").strip() 

    while conact2 == True:                
        mascota_id = input("Ingrese el ID de la mascota: ").strip()
                #while conact2 == True:
                    #mascota_id = input("Ingrese el ID de la mascota: ").strip()
        if not mascota_id:
            mascota_id = input("Ingrese el ID de la mascota: ").strip()
        elif mascota_id.isdigit():
            mascota_id = int(mascota_id)
            mascota = next((m  for m in mascotas if m.id == mascota_id), None)   
            if not mascota:
                print ("La Mascota no fue encontrada, debe registrarla. ")
                return
            else:
                print(f"El ID {mascota_id} pertenece a la mascota {mascota.nombre}")
                #fecha = input("Ingrese una fecha para la consulta (AAAA-MM-DD): ").strip()
                conact2 = False
        else:
            mascota_id = input("Ingrese un ID valido de la mascota: ").strip()
            

    if not mascota.historia_clinica:
        print(f"No hay citas relacionadas con {mascota.nombre}")
    else:
        print("Citas disponibles para actualizar")
        for cita in enumerate(mascota.historia_clinica):   # i,
            mascota.mostrar_historial()
        indice = input("Ingrese el número de la cita a actualizar: ").strip() 
    
    while conact3 == True:
        if not indice:
            indice = input("Ingrese el número de la cita a actualizar: ").strip()
        elif indice.isdigit():
            indicef = int(indice) -1
            if indicef < 0 or indicef >= len (mascota.historia_clinica):
                indice = input("Ingrese el número la cita valido a actualizar: ").strip()
            else:
                cita = mascota.historia_clinica[indicef]
                #print(cita)
                print("Deje en blanco los campos que no desea actualizar")
                nueva_fecha = input("Ingrese la nueva fecha (AAAA-MM-DD): ").strip()
                while conact4 == True:
                    if not nueva_fecha:
                        #if nueva_fecha:
                        #datetime.strptime(nueva_fecha, "%Y-%m-%d")
                        #cita.actualizar(fecha = nueva_fecha)
                        conact4 = False
                    elif validarFechaNueva(nueva_fecha):
                        try:
                            datetime.strptime(nueva_fecha, "%Y-%m-%d")
                            cita.actualizar_cita(fecha = nueva_fecha)
                            conact4 = False
                        except:
                            print("Ingrese una nueva fecha con el formato solicitado (AAAA-MM-DD)")
                    else:
                        nueva_fecha = input("Ingrese la nueva fecha (AAAA-MM-DD): ").strip()            
                                
                nueva_hora = input("Ingrese la nueva hora (HH:MM): ").strip()
                while conact5 == True:                  
                    if not nueva_hora:
                        #if nueva_hora:
                            #datetime.strptime(nueva_hora, "%H:%M")
                            #cita.actualizar_cita(hora = nueva_hora)
                            conact5 = False
                    elif validarHoraNueva(nueva_hora):
                        try:
                            datetime.strptime(nueva_hora, "%H:%M")
                            cita.actualizar_cita(hora = nueva_hora)
                            conact5 = False
                        except:
                            hora= input("Ingrese una hora con el formato solicitado (HH-MM): ").strip() 
                    else:
                        nueva_hora = input("Ingrese la nueva hora (HH:MM): ").strip()

                while conact6 == True:
                    nuevo_servicio = input("Elija el nuevo servicio (consulta, vacunación, esterilización, spa: ").strip()
                    if validarEntradaTexto(nuevo_servicio):
                        cita.actualizar_cita(servicio = nuevo_servicio)
                        conact6 = False
                    else:
                        nuevo_servicio = input("Elija el nuevo servicio (consulta, vacunación, esterilización, spa: ").strip()                            
                                                                
                while conact7 == True:
                    nuevo_veterinario = input("Ingrese el nuevo veterinario: ").strip()
                    if validarEntradaTexto(nuevo_veterinario):
                        cita.actualizar_cita(veterinario = nuevo_veterinario)
                        print(f"¡Cita actualizada con éxito!. ID: {cita.id}")
                        conact7 = False
                    else:
                        nuevo_veterinario = input("Ingrese el nuevo veterinario: ").strip()
                conact3 = False                                                                                                                      
        else:
            indice = input("Ingrese el número valido de la cita a actualizar: ").strip()                                                            

