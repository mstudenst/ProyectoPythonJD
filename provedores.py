import os
from io import open
class proveedores:
    print("\n""*********************************************************************************""\n")
lista_Id=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009] #listas 
lista_Nombres=["ARENA","RUSELL","CK","ACTIDUD","LEVIS","NIKE","PEPE","ADIDAS","VOLCOM","REEKBOK"]
lista_Representantes=["Federico Barquelo Solis","Monica Campos Espinoza","Marcos Hernadez Porraz","Alejandro Corrales Moralez","Camila Rodriguez Abarca","Sofia Vargas Diaz","Roberto Martinez Hernandez","Juan Perez Perez","Tatiana Abarca Reyes","Maria Salas Duran"]
lista_Telefonos=["65479542","62047855","88745244","88745250","65764743","88796641","78906755","87465634","65748475","80529475"]
lista_Correos=["carlossolis@gmail.com","monicampos@gmail.com","marchernade@gmail.com","alejandrocora52@gmail.com","camilabarca@gmail.com","sofidiaz@gmail.com","robertomtz@gmail.com","perezjuan@gmail.com","taniara@gmail.com","mmariasalas@gmail.com"]

def listas_proeevedores():
    for a,b,c,d,e in zip(lista_Id,lista_Nombres,lista_Representantes,lista_Telefonos,lista_Correos):
        print(a,"\t",b,"\t",c,"\t",d,"\t",e)

def imprimir_proveedores():
    
    datosProveedor=open("provedores.txt","r")
    print(datosProveedor.read())
    print("\n""Identidad","Nombre","\t","Representante","\t\t","Telefono","\t","Correo""\n") #Impresiónn de los proeevedores.
    datosProveedor.close
        
def imprecion_Menu(): #Menu de opciones para proveedores
    print("\n\t\t\t\t\t""Bienvenido""\t\t\t\t\t\n")
    print("\nOpciones disponibles\n")
    print("1\t\t\tAgregar Proveedor\n2\t\t\tEditar Proveedor\n")

imprecion_Menu() 
print("\n""\t\t\t\t\t""Provedores de Ropa""\t\t\t\t\t""\n")
imprimir_proveedores()

datos_de_usuario=[]
datos_de_usuario1=[]

def seleccion_de_Menu():
    desicion=input("digite una opción ")

    if desicion == 1:
        return "usted va agregar nuevos datos"
        
    elif desicion == 2:
        return "Usted va a editar proveedores"
    
print(seleccion_de_Menu())       
       
def agregar_proveedor():

    datosProveedor=open("provedores.txt","a+") #Leer escribe y agrega texto al documento
    registro=datosProveedor.readlines() #Almacena una lista
    Identidad=str(input("El codigo de proveedor es: ""\n"))
    Nombre=input("cual es el nonbre del proveedor: ""\n")
    Representante=input("Digite el representante: ""\n")
    Telefono=input("Digite el teléfono: ""\n")
    Correo=input("El correo electrico es: ""\n")
    registro.append(Identidad) #Agrega  los datos  en un orden append agrega los datos de texto
    registro.append(Nombre)
    registro.append(Representante)
    registro.append(Telefono)
    registro.append(Correo)    
    datosProveedor.seek(0) #posicion del  inicio del texto
    datosProveedor.writelines(registro)
    datosProveedor.close() #Se cierra el documento luego de los cambios
#agregar_proveedor()

def editar_provedor():
    datosProveedor=open("provedores.txt","r+")
    registro=datosProveedor.readlines()
    Identidad=input("El codigo de proveedor es ")
    #registro.append(Identidad)
    
    registro(registro.index(Identidad))
    datosProveedor.seek(0) #posicion del  inicio del texto
    datosProveedor.writelines(registro)
    datosProveedor.close() #Se cierra el documento luego de los cambios

editar_provedor()