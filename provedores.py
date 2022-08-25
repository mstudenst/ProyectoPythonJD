import os
from io import open
class proveedores:
    def actualizar_proveedor():
        datosProveedor=open("provedores.txt","a+") #Leer escribe y agrega texto al documento
        registro=datosProveedor.readlines() #Almacena una lista
        primerdato=("8000,ARENA,Federico Barquelo Solis,65479542,carlossolis@gmail.com\n") #se procede a ingresar todos los datos de los proveedores esenciales.
        segundodato=("8001,RUSELL,Monica Campos Espinoza,62047855,monicampos@gmail.com\n") 
        tercerdato=("8002,CK,Marcos Hernadez Porraz,88745244,marchernade@gmail.com\n") 
        cuartodato=("8003,ACTITUD,Alejandro Corrales Moralez,88745250,alejandrocora52@gmail.com\n")
        quintodato=("8004,LEVIS,Camila Rodriguez Abarca,65764743,camilabarca@gmail.com\n")
        sextodato=("8005,NIKE,Sofia Vargas Diaz,88796641,sofidiaz@gmail.com\n")
        septimodato=("8006,PEPE,Roberto Martinez Hernandez,78906755,robertomtz@gmail.com\n")
        octavodato=("8007,ADIDAS,Juan Perez Perez,87465634,perezjuan@gmail.com\n")
        novenodato=("8008,VOLKOM,Tatiana Abarca Reyes,65748475,taniara@gmail.com\n")
        decimodato=("8009,REEBOK,Maria Salas Duran,80529475,mmariasalas@gmail.com\n")
            
        registro.append(primerdato) #Agrega  los datos  en un orden
        registro.append(segundodato)#append agrega los datos de texto
        registro.append(tercerdato)
        registro.append(cuartodato)
        registro.append(quintodato)
        registro.append(sextodato)
        registro.append(septimodato)
        registro.append(octavodato)
        registro.append(novenodato)
        registro.append(decimodato)

        datosProveedor.seek(0) #posicion del  inicio del texto
        datosProveedor.writelines(registro)
        datosProveedor.close() #Se cierra el documento luego de los cambios

    def imprimir_proveedores():
    
        datosProveedor=open("provedores.txt","r")
        print(datosProveedor.read())
        datosProveedor.close
            
    print("\n""********************Actualización de los proeevedores********************""\n")    
#actualizar_proveedor() # se mostrara por pantalla los nuevos datos
    imprimir_proveedores()

class proveedores:
    
    def __init__(self): #Modo Constructor, contiene en sus atributos:id,nombre,representante,telefono y correo.
        self._identidad=int(input("El codigo de proveedor es "))
        self._nombre=input("cual es el nonbre del proveedor ")
        self._representante=input("Digite el representante ")
        self._telefono=input("Digite el teléfono ")
        self._correo=input("El correo electrico es ")
        self.__nacionalidad=True
        self.__devoluciones=True
        #self.diccionario_proveedor=dict # esto es nuevo y no se esta usando.

    def origen_proveedor(self,nnacionalidad): #Metodo de clase para saber el origen nacional o internacional.
        
        self.__nacionalidad=nnacionalidad
        
        if self.__nacionalidad:
            return "nacional"
        else: 
            return "internacional"

    def devolucion_dano(self,ddano): # Metodo de clase para saber si aplica para devolucion de productos o no.
        self.__devoluciones=ddano

        if self.__devoluciones:
            return "con devolucion"
        else:
            return "sin devolucion"

    def estado(self):
        
        return self._identidad,self._nombre,self._representante,self._telefono,self._correo,self.origen_proveedor(self.__nacionalidad),self.devolucion_dano(self.__devoluciones)

arena=proveedores() #primer objeto
arena.devolucion_dano(False)
arena.origen_proveedor(False)
print(arena.estado())
 #Se almacenan la llave del diccionario y los atributos del contructor como valores.


rusell=proveedores()#segundo objeto
rusell.origen_proveedor(False)
rusell.devolucion_dano(False)
print(rusell.estado())


calvin=proveedores()#tercer objeto 
calvin.origen_proveedor(True)
calvin.devolucion_dano(True)
print(calvin.estado())


actitud=proveedores()#cuarto objeto
actitud.origen_proveedor(False)
actitud.devolucion_dano(True)
os.system("cls") #limpia la pantalla

levis=proveedores()
levis.origen_proveedor(False)
levis.devolucion_dano(True)
                                        # diccionario final con llaves y valores

#diccionario_proveedor.items
#diccionario_proveedor.values
#diccionario_proveedor.keys  

lista_Id=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009] #listas 
lista_Nombres=["ARENA","RUSELL","CK","ACTIDUD","LEVIS","NIKE","PEPE","ADIDAS","VOLCOM","REEKBOK"]
lista_Representantes=["Federico Barquelo Solis","Monica Campos Espinoza","Marcos Hernadez Porraz","Alejandro Corrales Moralez","Camila Rodriguez Abarca","Sofia Vargas Diaz","Roberto Martinez Hernandez","Juan Perez Perez","Tatiana Abarca Reyes","Maria Salas Duran"]
lista_Telefonos=["65479542","62047855","88745244","88745250","65764743","88796641","78906755","87465634","65748475","80529475"]
lista_Correos=["carlossolis@gmail.com","monicampos@gmail.com","marchernade@gmail.com","alejandrocora52@gmail.com","camilabarca@gmail.com","sofidiaz@gmail.com","robertomtz@gmail.com","perezjuan@gmail.com","taniara@gmail.com","mmariasalas@gmail.com"]

print("\n""\t\t\t\t\t""Provedores de Ropa""\t\t\t\t\t""\n")
print("\n""Identidad","\t","Nombre","\t","Representante","\t\t\t","Telefono","\t","Correo""\n") #Impresiónn de los proeevedores.
def listas_proeevedores():
    for a,b,c,d,e in zip(lista_Id,lista_Nombres,lista_Representantes,lista_Telefonos,lista_Correos):
       print(a,"\t\t",b,"\t\t",c,"\t",d,"\t",e)

listas_proeevedores()
print("\n\n""*********************************************************************************""\n\n")

