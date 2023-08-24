#!/usr/bin/env python3
import os
import xml.etree.ElementTree as ET
tree = ET.parse('./datos.xml')
root = tree.getroot()


#Funcion de Listar todo
def listar():
    print('DNI |  Nombre |  Apellidos | Telefono')
    print('-------------------------------------')
    for persona in root.findall('persona'):
        dni = persona.get('DNI')
        mombre = persona.get('nombre')
        apellidos = persona.get('apellidos')
        telf= persona.get('telefono')
        print(dni,'|', mombre,'|', apellidos,'|', telf)
#------------------------------------
    
#Funcion añadir
def anadir(dni,nombre,apellidos,telefono):
    nuevo=ET.Element('persona')
    root.append(nuevo)
    print('Añadir Registro')
    print('---------------')
    nuevo.set('DNI',dni)
    nuevo.set('nombre',nombre)
    nuevo.set('apellidos',apellidos)
    nuevo.set('telefono',telefono)
    tree.write('./datos.xml')
    print('Registro añadido.')

#------------------------------------

#Funcion Borrar
def borrar(dni):
    encontrado=False
    for persona in root.findall('persona'):
        if dni == persona.get('DNI'):
           encontrado=True
           os.system('clear')
           print('Borrar Registro:')
           print('----------------')
           print('DNI: ',persona.get('DNI'))
           print('Nombre: ',persona.get('nombre'))
           print('Apellidos: ',persona.get('apellidos'))
           print('Telefono :',persona.get('telefono'))
           print('')               
           SN=input('Borrar [S/N]')
           if SN=='s' or SN=='S':
              root.remove(persona)
              tree.write('./datos.xml')
              print('Registro Borrado')
           else:
              print('Registro NO Borrado')

    if not encontrado:
       print('Registro NO encontrado')
#------------------------------------

#Funcion Modificar
def modificar(dni):
    encontrado=False
    for persona in root.findall('persona'):
        if dni == persona.get('DNI'):
           encontrado=True
           salir=False
           modificado=False
           
           while not salir:
               os.system('clear')

               print('Modificar:')
               print('----------')
               print('DNI: ',persona.get('DNI'))
               print('Nombre: ',persona.get('nombre'))
               print('Apellidos: ',persona.get('apellidos'))
               print('Telefono :',persona.get('telefono'))
               print('')               
               if modificado:
                  print('**Modificado**\n')
               print('[D]NI [N]ombre [A]pellidos [T]elefono')
               print('[G]uardar [S]alir')

               opcion=input('Opcion:').upper() #opcion siempre sera mayusculas

               if opcion=='D':
                  texto=input('Nuevo DNI:')
                  persona.set('DNI',texto)
                  modificado=True
                  print('DNI Modificado')

               if opcion=='N':
                  texto=input('Nuevo Nombe:')
                  persona.set('nombre',texto)
                  modificado=True
                  print('Nombre Modificado')
  
               if opcion=='A':
                  texto=input('Nuevos Apellidos:')
                  persona.set('apellidos',texto)
                  modificado=True
                  print('Apellidos Modificados')

               if opcion=='T':
                  texto=input('Nuevo Telefono:')
                  persona.set('telefono',texto)
                  modificado=True
                  print('Telefono Modificados')

               if opcion=='G':
                  tree.write('./datos.xml')
                  modificado=False
                  print('Registro Guardado')

               if opcion=='S':
                  if modificado:
                      SN=input('Guardar los cambios antes de Salir [S/N]').upper()
                      if SN=='S':
                            tree.write('./datos.xml')
                            print('Registro Guardado')
                      else:
                           print('Cambios Descartados')
                  salir=True
    if not encontrado:
        print('DNI no encontrado')

#Funcion Buscar
def buscar(campo,valor):
    encontrado=False
    print('Busqueda de ',valor, 'en' ,campo)
    print('')           
    print('DNI |  Nombre |  Apellidos | Telefono')
    print('-------------------------------------')
    for persona in root.findall('persona'):
        if persona.get(campo).find(valor)>-1:
            encontrado=True
            dni = persona.get('DNI')
            mombre = persona.get('nombre')
            apellidos = persona.get('apellidos')
            telf= persona.get('telefono')
            print(dni,'|', mombre,'|', apellidos,'|', telf)
    if not encontrado:
       print('Registro no encontrado.')

#----------------------------------  

#Funcion Pausa
def pausa():
    input('\nPulsa una tecla.')
#------------------------------        

#PROGRAMA PRINCIPAL ---------------        
salir=False

while not salir:

   os.system('clear')
   print('El titulo:',root.find('titulo').text,'\n')

   print('[1] Listar Base de Datos')
   print('[2] Añadir Registro')        
   print('[3] Buscar en los registros')        
   print('[4] Modificar Registro por DNI')       
   print('[5] Borrar Registro por DNI')       
   print('')
   print('[0] Salir')       
   print('')

   opcion=input('Opcion:')

   if opcion=='0':
      salir=True

   if opcion=='1':
      os.system('clear')
      listar()
      pausa()

   if opcion=='2':
      os.system('clear')
      print('Añadir un nuevo registro')
      dni=input('DNI:')
      nombre=input('Nombre:')
      apellidos=input('Apellidos:')
      telefono=input('Telefono:')
      anadir(dni,nombre,apellidos,telefono)
      pausa()

   if opcion=='3':
      os.system('clear')
      print('Buscar registro por:')
      print('[D]NI [N]ombre [A]pellidos [T]elefono')
      print('')
      opcion=input('Opcion:').upper()
   
      if opcion=='D':
           opcion='DNI'
      if opcion=='N':
           opcion='nombre'
      if opcion=='A':
           opcion='apellidos'
      if opcion=='T':
           opcion='telefono'
   
      valor=input('\n'+opcion+': ')
      os.system('clear')
      buscar(opcion,valor)
      pausa()

   if opcion=='4':
      os.system('clear')
      dni=input('Introduce el DNI:')
      modificar(dni)
      pausa()

   if opcion=='5':
      os.system('clear')
      dni=input('Introduce el DNI:')
      borrar(dni)
      pausa()


