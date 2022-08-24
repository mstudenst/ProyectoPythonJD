from datetime import date
import os

#********** INICIA DECLARACION DE VARIABLES **********
today=date.today()
numero_factura=int()
saldo=float()
subtotal=float()
abono=float()
iva=float()
linea=str()
venta=str()
cant=int()
cliente=[]
codigo=[]
producto=[]
precio=[]
existencias=[]
comprando=True
compra=[]
cantidad=[]

# ********************* INICIA DECLARACIÓN DE FUNCIONES **********************
def imp_detalle ():                                                           
    print("===================== LISTA DE ARTICULOS ====================")
    print("Código \t Detalle \t\t Precio") 
    for c,d,p in zip(codigo,producto,precio):
        print (c, "\t", d, "\t","\t",p)
        print ("============================================================")

print ("\n Digite S para salir \n")

def imp_compra ():
    print("==================== LISTA DE COMPRA ====================")
    print ("Cantidad \t Código \t Detalle \t\t Precio")
    for prod in compra:


#************************* INICIA EJECUCION **********************************
contador=0
acumulador=0

while comprando==True:
    imp_detalle()                                #Muestra los artículos a la venta
    imp_compra()                                 #Muestra la lista de artículos a comprar
    print("Digite el artículo a comprar: ")
    venta=str.upper(input())                     #Controla el uso de mayúsculas y minúsculas

    if venta!="S":                               #Condicional que permita ingresar cantidad de unidades a comprar
        compra+=[venta]
        cant=int(input("Digite la cantidad de unidades a comprar: "))
        if cant > 0:
            cantidad+=[cant]
