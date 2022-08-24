import os
class proveedores:
     
    def __init__(self,Nombre,Representante,Telefono,Correo): #Modo Constructor, contiene en sus atributos:id,nombre,representante,telefono y correo.
    
        self.__nombre=Nombre
        self.__representante=Representante
        self.__telefono=Telefono
        self.__correo=Correo
        self.__nacionalidad=True
        self.__devoluciones=True
        #self.diccionario_proveedor=dict # esto es nuevo y no se esta usando

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
        
        return self.__nombre,self.__representante,self.__telefono,self.__correo,self.origen_proveedor(self.__nacionalidad),self.devolucion_dano(self.__devoluciones)

arena=proveedores("ARENA","Federico Barquelo Solis","65479542","carlossolis@gmail.com") #primer objeto
arena.origen_proveedor(False)
arena.devolucion_dano(True)
print(arena.estado())

diccionario_proveedor={} #Diccionario vacio
diccionario_proveedor[84640]=arena.estado() #Se almacenan la llave del diccionario y los atributos del contructor como valores.

class proveedor2(proveedores): #clase que hereda los atribujos de la clase padre a hijo y asi mismo hasta donde este la ultima clase

    def __init__(self, Nombre, Representante, Telefono, Correo):
        super().__init__(Nombre, Representante, Telefono, Correo)

    def estado(self):
        return super().estado()

rusell=proveedor2("RUSELL","Monica Campos Espinoza","62047855","monicampos@gmail.com")#segundo objeto
rusell.origen_proveedor(False)
rusell.devolucion_dano(False)
print(rusell.estado())

diccionario_proveedor[84641]=rusell.estado()

class proveedor3(proveedor2):

    def __init__(self, Nombre, Representante, Telefono, Correo): #atributos heredados
        super().__init__(Nombre, Representante, Telefono, Correo)

    def estado(self):
        return super().estado()

calvin=proveedor3("CK","Marcos Hernadez Porraz","88745244","marchernade@gmail.com")#tercer objeto 
calvin.origen_proveedor(True)
calvin.devolucion_dano(True)

diccionario_proveedor[84642]=calvin.estado()

class proveedor4(proveedor3):

    def __init__(self, Nombre, Representante, Telefono, Correo):
        super().__init__(Nombre, Representante, Telefono, Correo)

    def estado(self):
        return super().estado()

leonisa=proveedor4("LEONISA","Alejandro Corrales Moralez","88745250","alejandrocora52@gmail.com")#cuarto objeto
leonisa.origen_proveedor(False)
leonisa.devolucion_dano(True)
os.system("cls") #limpia la pantalla
diccionario_proveedor[84643]=leonisa.estado()
print(diccionario_proveedor) # diccionario final con llaves y valores

#diccionario_proveedor.items
#diccionario_proveedor.values
#diccionario_proveedor.keys  

lista_Id=[84640,84641,84642,84643] #listas 
lista_Nombres=["ARENA","RUSELL","CK","LEONISA"]
lista_Representantes=["Federico Barquelo Solis","Monica Campos Espinoza","Marcos Hernadez Porraz","Alejandro Corrales Moralez"]
lista_Telefonos=["65479542","62047855","88745244","88745250"]
lista_Correos=["carlossolis@gmail.com","monicampos@gmail.com","marchernade@gmail.com","alejandrocora52@gmail.com"]

print("\n""\t\t\t\t\t""Provedores de Ropa""\t\t\t\t\t""\n")
print("\n""Identidad","\t","Nombre","\t","Representante","\t\t\t","Telefono","\t","Correo""\n") #Impresiónn de los proeevedores.
def listas_proeevedores():
    for a,b,c,d,e in zip(lista_Id,lista_Nombres,lista_Representantes,lista_Telefonos,lista_Correos):
       print(a,"\t\t",b,"\t\t",c,"\t",d,"\t",e)

listas_proeevedores()


"""datosProveedor=open("proveedores.txt","a+") #Leer escribe y agrega texto al documento
class listapro(proveedores):
    def actualizar_proveedor():
        os.system("cls")
        registro=datosProveedor.readlines() #Almacena una lista
        primerdato=diccionario_proveedor #se procede a ingresar todos los datos de los proveedores esenciales.
        registro.append(primerdato) #Agrega  los datos  en un orden
        
        datosProveedor.seek(0) #posicion del  inicio del texto
        datosProveedor.writelines(registro)
        datosProveedor.close() #Se cierra el documento luego de los cambios

    def imprimir_proveedores():
        os.system("cls")
        datosProveedor=open("proveedores.txt","r")
        print(datosProveedor.read())
        datosProveedor.close
        
    print("\n""********************Actualización de los proeevedores********************""\n")    
    actualizar_proveedor() # se mostrara por pantalla los nuevos datos
    imprimir_proveedores()


        """