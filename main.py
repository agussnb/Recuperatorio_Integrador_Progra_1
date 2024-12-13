from biblioteca_almacen.funciones import *
def menu():
    menu_activado = True
    inventario = []
    while menu_activado:
        print('Bienvenido a Supermercado Jumbo, por favor, eliga una de las siguientes opciones: ')
        print("1 - Leer archivo inventario.csv")
        print("2 - Listar inventario")
        print("3 - Buscar producto por nombre")
        print("4 - Ordenar inventario por precio")
        print("5 - Ordenar inventario por cantidad")
        print("6 - Actualizar producto")
        print("7 - Actualizar inventario")
        print("8 - Mappear precios (Con aumento del 10%)")
        print("0 - Salir")
        opcion = input("Ingresa una opcion ")
        match opcion:
            case '1':
                inventario = leer_archivo()
                if inventario:
                    print('Archivo leido')
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '2':
                if inventario:
                    listar_inventario(inventario)
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '3':
                if inventario:
                    nombre = input("Ingresa el nombre del producto que buscas (Tal cual como se encuentra en el inventario) ")
                    buscar_producto(nombre,inventario)
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '4':
                if inventario:
                    inventario_ordenado = ordenar_inventario_por_precio(inventario)
                    print(inventario_ordenado)
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '5':
                if inventario:
                    inventario_ordenado_q = ordenar_inventario_por_cantidad(inventario)
                    print(inventario_ordenado_q)
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '6':
                if inventario:
                    producto = input("Ingresa el nombre del producto que desees actualizar su stock (Exactamente igual a como esta en el csv)")
                    producto_actualizado = actualizar_producto(producto,inventario)
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '7':
                if inventario:
                    actualizar_inventario(producto_actualizado,inventario)
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '8':
                if inventario:
                    inventario_mapeado = mapear_precios(inventario)
                    for productos in inventario_mapeado:
                        print(productos)
                else:
                    print("Error, no es posible utilizar esta opcion si no se leyo el archivo inventario.csv anteriormente")
            case '0':
                print("Saliendo del programa")
                print("Gracias por utilizar nuestros servicios!")
                menu_activado = False
                
menu()

