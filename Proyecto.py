from io import open

print("Bienvenido a su programa de facturación")

class Usuario():
    
    administrativos=open("Puestos.txt","w")
    puestos=["Administrador","Contador","Auxiliar contable"]
    contraseñas=["Admin123","Conta123","Auxcont123"]

    puestos={}
    contraseñas={}
    
    administrativos
    
    numerodeUsuarios = 3

    def __init__(self, puestos, contraseñas):
        
        self.puestos = puestos
        self.contraseñas = contraseñas
        
        self.enlinea = False
        self.intentos = 3
        
        Usuario.numerodeUsuarios+=1
        
    def Iniciar_Sesion(self, puestos, contraseñas):
        print()
        MiPuesto = input("Escriba su puesto de trabajo: ")
        print()
        Micontraseña = input("Escriba su contraseña: ")
        
        if Micontraseña==contraseñas[0]:
            print()
            print(" >>> Ha iniciado sesión exitosamente <<< ")
            self.enlinea = True
            
        else:
            self.intentos-=1
            if self.intentos > 0:
                print()
                print (" * UPS, Contraseña Incorrecta, ingrese su contraseña de nuevo")
                print()
                print ("Te quedan: ", self.intentos, "intentos" )
                self.Iniciar_Sesion()
                
            else:
                print("No se pudo Iniciar Sesión")
                print(" * Failed * ")    
 
    print()  
          
    def Cerrar_Sesion(self):
        
        if self.enlinea:
            print(" >>> La sesión cerro correctamente <<<")        
            self.enlinea = False
            
        else:
            print(" >>> No ha iniciado sesión <<< ")
            
    def __str__(self):
        
        if self.enlinea:
            conect = "En línea"
            
        else:
            conect = "Fuera de línea"
        print()
        return f"Mi nombre de usuario es {self.puestos} y me encuentro {conect}"
        print()
print()  
usuario1 = Usuario(input("Ingrese su puesto: "), input("Ingrese su contraseña: "))
print(usuario1)    
usuario1.Iniciar_Sesion()