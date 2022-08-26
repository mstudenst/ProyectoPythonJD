import os
from io import open
class proveedores:
    print("\n""*********************************************************************************""\n")

#Programa que permite leer agregar y editar proveedores de un documento de texto Junior Developer.

def imprimir_proveedores():#Impresiónn de los proeevedore actuales.
    datosProveedor=open("provedores.txt","r")
    print(datosProveedor.read())
    datosProveedor.close
        
def imprecion_Menu(): #Menú de opciones para proveedores.
    print("\n\t\t\t\t\t""Bienvenido""\t\t\t\t\t\n")
    print("\nOpciones disponibles\n")
    print("1\t\t\tAgregar Proveedor\n2\t\t\tEditar Proveedor\n")

imprecion_Menu() 
print("\n""\t\t\t\t\t""Provedores""\t\t\t\t\t""\n")#Rotúlos del Menú.
print("\n""Identidad","Nombre","\t","Representante","\t\t","Telefono","\t","Correo""\n")
imprimir_proveedores()

def agregar_proveedor():
    
    datosProveedor=open("provedores.txt","a+") #Leé escribe y agrega texto al documento proveedores.
    registro=datosProveedor.readlines() 
    Identidad=str(input("El codigo de proveedor es: ""\n"))
    Nombre=input("cual es el nonbre del proveedor: ""\n")
    Representante=input("Digite el representante: ""\n")
    Telefono=input("Digite el teléfono: ""\n")
    Correo=input("El correo electrico es: ""\n")
    registro.append(Identidad) #Agrega  los datos  en un orden a provedores.txt.
    registro.append(Nombre)
    registro.append(Representante)
    registro.append(Telefono)
    registro.append(Correo)    
    datosProveedor.seek(0) #Posición del  inicio del texto.
    datosProveedor.writelines(registro)
    datosProveedor.close() #Se cierra el documento luego de los cambios.

def editar_provedor(): #Permite editar proveedor
    datosProveedor=open("provedores.txt","r+")
    registro=datosProveedor.readlines()
    Identidad=str(input("El codigo de proveedor es "))
   
    for ide in (registro):
        ide(registro.index(Identidad))
        datosProveedor.writelines(registro)
        datosProveedor.close() #Se cierra el documento luego de los cambios.
        
def seleccion_de_Menu(): #Seleccion del menu del usuario de acuerdo a la opcines disponibles.
    
    print("\n\n""*********************************************************************************""\n\n")
    print("Seleccione una opción")
    desicion=str(input())
    if desicion =="1": #De acuerdo a la eleccion procede a relizar una acción.
        return agregar_proveedor()

    elif desicion =="2":
        return editar_provedor()
    
    else: 
        return seleccion_de_Menu()
seleccion_de_Menu() # Actualización de proveedor.
os.system("cls")

    


