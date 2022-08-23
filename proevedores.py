import os
class proveedores:
     
    def __init__(self,Nombre,Representante,Telefono,Correo): #Modo Constructor, contiene en sus atributos:id,nombre,representante,telefono y correo.
    
        self.__nombre=Nombre
        self.__representante=Representante
        self.__telefono=Telefono
        self.__correo=Correo
        self.__nacionalidad=True
        self.__devoluciones=True
        self.diccionario_proveedor=dict # esto es nuevo y no se esta usando

    def diccinarioProveerdor(self,dicProv):
        self.diccinarioProveerdor=dicProv

        return self.diccionario_proveedor

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
        os.system("cls")
        return self.__nombre,self.diccionario_proveedor,self.__representante,self.__telefono,self.__correo,self.origen_proveedor(self.__nacionalidad),self.devolucion_dano(self.__devoluciones)


unilever=proveedores("UNILEVER","Federico Barquelo Solis","65479542","carlossolis@gmail.com")
unilever.origen_proveedor(False)
unilever.devolucion_dano(True)
print(unilever.estado())

diccionario_proveedor={}
diccionario_proveedor["84645"]=unilever.estado() #Se almacenan en un diccionario el estado general de los objetos que se puede actualizar en un futuro.
#print(diccionario_proveedor)


class proveedor2(proveedores):

    def __init__(self, Nombre, Representante, Telefono, Correo):
        super().__init__(Nombre, Representante, Telefono, Correo)

    def estado(self):
        return super().estado()

pg=proveedor2("P&G","Monica Campos Espinoza","62047855","Monicampos@gmail.com")
pg.origen_proveedor(False)
pg.devolucion_dano(False)
print(pg.estado())

diccionario_proveedor["84646"]=pg.estado()
print(diccionario_proveedor)
#dicc=diccionario_proveedor
#claves=dicc.keys
#valores=dicc.values
#print(claves)
#print(valores)


"""datosProveedor=open("proveedores.txt","a+") #Leer escribe y agrega texto al documento
class listapro(proveedores):
    def actualizar_proveedor():
        os.system("cls")
        registro=datosProveedor.readlines() #Almacena una lista
        primerdato=("84640\tESSITY\tCarlos Vargas Salazar\t65479542\tcarlos85@gmail.com\n") #se procede a ingresar todos los datos de los proveedores esenciales.
        segundodato=("84641\tFEMSA\tAlejandro Corrales Moralez\t88745244\talejandrocora52@gmail.com\n") 
        tercerdato=("84642\tGLOBAL MERCHANT\tMarcos Hernadez Porraz\t75852133\tmarchernade@gmail.com\n") 
        cuartodato=("84643\tHEIZ\tJohn Betancour  Four\t66782315\tjjbeta@.hotmail.com\n")
        quintodato=("\nIngrese un nuevo proveedor\t\n")
        
        registro.append(primerdato) #Agrega  los datos  en un orden
        registro.append(segundodato) #append agrega los datos de texto
        registro.append(tercerdato)
        registro.append(cuartodato)
        registro.append(quintodato)
        diccionario_proveedor

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