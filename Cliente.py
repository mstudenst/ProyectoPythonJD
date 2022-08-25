from io import open
print("Clientes")
class Cliente:
    Id=["1234", "2345", "6345"]
    Nombre=["Mario Castillo", "Mainor Segura", "Andrea Mora"]
    Correo=["mario@invenio.com", "mainor@invenio.com", "andrea@invenio.com"]
    Telefono=[23456, 67899,43667]
    menucliente= int(input("Opciones: \n 1-Ver datos  \n 2-Insertar datos de la persona \n 3-Eliminar persona \n 4-Editar persona \n 0- SALIR \n "))
    
    while menucliente != 0: #Señala si menucliente es diferente a 0
        if menucliente == 1:
            print("*Id*               *Nombre*                     *Correo*               *Teléfono*        ")
            for x in range(len(Nombre)):
                print(Id[x],"         ",Nombre[x],"              ",Correo[x],"             ",Telefono[x],"       ")

        elif menucliente== 2:
            print("Llenar los siguientes datos")
            Id.append(int(input("Su id:  "))) # Se utiliza para
            Nombre.append(input("Su nombre: "))
            Correo.append(str(input("Su correo:  ")))
            Telefono.append(int(input("Su teléfono:  ")))

        elif menucliente== 3:
            print("Eliminar persona")
            id= input("Ingrese el Id del cliente que desee eliminar: ")
            for i in range(len(Id)-1,-1,-1): #Recorre las listas en la posición que se desea eliminar 
                if Id[i] == id:
                    Id.pop(i)  #Se utiliza el .pop para eliminar la información ingresada
                    Nombre.pop(i)
                    Correo.pop(i)
                    Telefono.pop(i)
            print("Persona eliminada")

        elif menucliente== 4:
            print("Editar persona")
            id= input("Ingrese el id del cliente que desee editar")
            for a in range (len(Id)):
                if Id [a]== id:
                    Nombre[a] = input("Cual es el nuevo nombre: ")
                    Correo[a] = input("Cual es el nuevo correo: ")
                    Telefono[a] = int(input("Cual es el nuevo teléfono: "))
            print("Persona editada")

        else:
            print("Ingresar una opcion correcta")

        menucliente= int(input("Opciones: \n -Ver datos \n 2-Insertar datos de la persona \n 3-Eliminar persona \n 4-Editar persona \n 0- SALIR \n "))

#Se inicia con la creación del archivo de texto
    Datos1=open("Id.txt", "w")
    Datos2=open("Nombre.txt", "w")
    Datos3=open("Correo.txt", "w")
    Datos4=open("Telefono.txt", "w")

    for x in range(len(Id)): #Busca un un rango en todas las listas
        Datos1.write(Id[x]+",")
        Datos2.write(Nombre[x]+",")
        Datos3.write(Correo[x]+",")
        Datos4.write(str(Telefono[x])+",")

    Datos1.close()
    Datos2.close()
    Datos3.close()
    Datos4.close()+","