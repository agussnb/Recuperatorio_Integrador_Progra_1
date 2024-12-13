import csv
def leer_archivo():
    """
    Funcion para leer el archivo inventario.csv
    """
    inventario_vacio = []
    with open('inventario.csv','r') as inventario:
        lector = csv.reader(inventario)
        next(lector)
        for fila in lector:
            nombre,precio,cantidad = fila
            inventario_formato = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
            inventario_vacio.append(inventario_formato)
        return inventario_vacio
    
def listar_inventario(inventario:list):
    """
    Funcion para listar los productos del inventario
    """
    for item in inventario:
        print(f"Nombre: {item['nombre']}, Precio: {item['precio']}, Cantidad: {item['cantidad']}")
        
def buscar_producto(nombre: str, inventario: list):
    """
    Función para buscar un producto por su nombre.
    """
    nombre_sin_guion = nombre.replace("-", "")  
    for item in inventario:
        nombre_item_sin_guion = item['nombre'].replace("-", "") 
        if nombre_item_sin_guion == nombre_sin_guion:
            print("Producto encontrado! \n")
            print(f"Nombre: {item['nombre']}, Precio: {item['precio']}, Cantidad: {item['cantidad']}")
            return item
    
    print("Error al buscar el producto, intenta de nuevo")
    return None


def ordenar_inventario_por_precio(inventario:list):
    """
    Funcion para ordenar el inventario por precio 
    """
    n = len(inventario)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if float(inventario[j]['precio']) > float(inventario[j+1]['precio']):
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]
                swap = True
        if not swap:
            break
    
    for item in inventario:
        print(item)
        

def ordenar_inventario_por_cantidad(inventario:list):
    """
    Funcion para ordenar el inventario por cantidad
    """
    n = len(inventario)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if int(inventario[j]['cantidad']) < int(inventario[j+1]['cantidad']):
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]
                swap = True
        if not swap:
            break
    for item in inventario:
        print(item)
            
def actualizar_producto(nombre: str, inventario: list):
    """
    Funcion para actualizar el stock de un producto luego de la venta
    """
    producto = buscar_producto(nombre, inventario)
    if producto:  
        print(f"Stock actual {producto['cantidad']} ")
        nueva_cantidad = int(input("Ingresa el stock nuevo "))
        while nueva_cantidad > int(producto['cantidad']):
            print('Error, no es posible que el stock nuevo sea mayor al anterior')
            nueva_cantidad = int(input("Ingresa el stock nuevo "))
        while nueva_cantidad < 0:
            print("No puede haber stock negativo")
            nueva_cantidad = int(input("Ingresa el stock nuevo "))
        producto['cantidad'] = nueva_cantidad
        producto_actualizado = producto
        print(f"Cantidad actualizada: {producto_actualizado['cantidad']} ")
        
        return producto_actualizado
    else:
        print("Error, producto no encontrado.")


def actualizar_inventario(producto_actualizado: dict, inventario: list):
    """
    Funcion para actualizar el inventario luego de actualizar el producto
    """
    nombre_archivo = 'inventario.csv'
    for item in inventario:
        if item['nombre'] == producto_actualizado['nombre']:
            item['cantidad'] = producto_actualizado['cantidad']  

    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(['nombre', 'precio', 'cantidad'])

        for item in inventario:
            escritor.writerow([item['nombre'], item['precio'], item['cantidad']])

    print(f"El inventario ha sido actualizado en {nombre_archivo}. ")
    
def mapear_precios(inventario):
    for producto in inventario:
        producto['precio'] = float(producto['precio']) * 1.10
    return inventario


    
        


