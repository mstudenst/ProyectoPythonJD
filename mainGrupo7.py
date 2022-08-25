# El siguiente programa es diseñado para el Proyecto Final de Python en Main
# Estudiantes: Maria Milena, Eduarth, Josebeth y Maria Paz

usuario1=input("Digite nombre: ") #El login nos da Error y no pasa el while para avanzar
while usuario1 == "mmed":
    print("----------------------------------------------------")
    print("               MENU PRINCIPAL DE OPERACIONES        ")
    print("----------------------------------------------------")
    print("  [ 1 ] INVENTARIO                 [ 3 ] CLIENTE    ")
    print("  [ 2 ] PROVEEDORES                [ 4 ] FACTURACIÓN ")
    modulo=input("Digitar opcion para ingresar al modulo: ")
    if modulo== "1":
        from inventario import inventario #importación del Grupo 
        existencia=inventario()
        existencia.menu()
    elif modulo == "2":
        from proveedores import proveedores
        unilever=proveedores("UNILEVER","Federico Barquelo Solis","65479542","carlossolis@gmail.com")
        unilever.origen_proveedor(False)
        unilever.devolucion_dano(True)
        print(unilever.estado())
    elif modulo == "3":
        from cliente import Cliente
    elif modulo == "4":
        from facturacion import facturacion 
    else: 
        print("Error") 
    break 
