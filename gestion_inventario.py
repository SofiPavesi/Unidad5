import sqlite3
#Conectar a la base de datos 
conexion = sqlite3.connect("inventario.db")
#Hacemos que la base de datos me retorne como lista de dict sino por default devuelve list de tuplas
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()


def crear_inventario():
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL, 
                    descripcion TEXT NOT NULL, 
                    cantidad INTEGER NOT NULL, 
                    precio REAL NOT NULL, 
                    categoria TEXT NOT NULL )
                    ''');
    conexion.commit()
    print("Tabla productos creada correctamente.")

#Esta funcion agrega un nuevo producto a la tabla.
def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del Producto o 'salir': ")
        if nombre.lower() == "salir":
            break
        
        descripcion = str(input("Ingrese una breve descripción del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese precio del producto ingresado: "))
        categoria = str(input("Ingrese la categoría del producto: "))
        
         # Insertar el producto en la base de datos
        cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?,?)", (nombre, descripcion, cantidad, precio,categoria))
        conexion.commit()
        
        print(f"Producto '{nombre}' agregado correctamente.")

#Esta funcion muestra una lista de todos los productos de la tabla.
def mostrar_productos():
   cursor.execute("SELECT * FROM productos ORDER BY nombre ASC")
   resultados = cursor.fetchall()
   
   if not resultados:
       print("No hay ningún registro en la tabla productos.")
   else:
       for registro in resultados:
           print(f"ID: {registro['id']} - Nombre: {registro['nombre']} - Descripción: {registro['descripcion']} - Cantidad: {registro['cantidad']} - Precio: ${registro['precio']} - Categoría: {registro['categoria']}")
   
#Esta funcion comprueba la existencia de un producto
def producto_existe(id):
    cursor.execute("SELECT * FROM productos WHERE id = ? ", (id,))
    resultado = cursor.fetchone()
    
    return bool(resultado)

#Esta función actualiza la cantidad de un producto de la tabla, accediendo a el por por el id      
def actualizar_producto():
    id_buscado = int(input("Ingrese el id del producto a actualizar: "))
    
    if producto_existe(id_buscado):
        nueva_cantidad = int(input("Ingrese nueva cantidad: "))
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad,id_buscado))
        conexion.commit()   
        
        print("La cantidad del producto ha sido actualizada exitosamente.")
    else:
        print("No existe el ID del producto buscado.")

#Esta función elimina un producto de la tabla, accediendo a el por el nombre o el id
def eliminar_producto():
    producto_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    
    if producto_existe(producto_eliminar):
       cursor.execute( "DELETE FROM productos WHERE id = ?", (producto_eliminar,))
       conexion.commit() 
       print(f"El producto ha sido eliminado con éxito.\n")
    else:
        print("No existe el ID del producto a eliminar.")
         
#Esta función busca un producto de la tabla en específico, accediendo a el por el nombre o el id
def buscar_producto():
   id_buscado = int(input("Ingrese ID del producto buscado: "))
   
   if producto_existe(id_buscado):
       cursor.execute("SELECT * FROM productos WHERE id = ?", (id_buscado,))
       resultado = cursor.fetchone()
       return print(f"ID: {resultado['id']} - Nombre: {resultado['nombre']} - Descripción: {resultado['descripcion']} - "
                  f"Cantidad: {resultado['cantidad']} - Precio: ${resultado['precio']} - Categoría: {resultado['categoria']}")
   else:
       print("No hay ningún registro de ese producto en la tabla.")
   
#Función para generar un reporte de productos con bajo stock, tomando como bajo stock un parámetro recibido por consola
def reporte_bajo_stock():
    bajo_stock = int(input("Ingrese el valor a considerar como 'Bajo stock': "))

    if bajo_stock<=0:
        print("El stock debe ser un número mayor que cero.")
    else:
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?",(bajo_stock,))
        resultados= cursor.fetchall()
        print("\n\t---Productos con bajo Stock---\n")
    for registro in resultados:
        print(f"id: {registro['id']} - Nombre: {registro['nombre']} - Cantidad: {registro['cantidad']}\n")

#Fucion del menú con el que interacturá el usuario.
def menu():         
    while True:
        print("-"*40)
        print("\n\t---Menú Principal---\n")
        print("-"*40)
        print("1. Agregar: Agrega Productos al stock.")
        print("2. Mostrar: Muestra todos los productos del inventario.")
        print("3. Actualizar: Actualizar la cantidad en stock de un producto.")
        print("4. Eliminar: Dar de baja productos.")
        print("5. Buscar: Busca un producto por ID.")
        print("6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
        print("7. Salir.")
        print("-"*40)
        opcion = int(input("Ingrese la opción deseada (1-7):\n"))
        
    #Gestiono las opciones que seleccione el usuario:

        while opcion < 1 or opcion > 7:
            print("No ha seleccionado una opción válida.")
            opcion = int(input("Por favor, Ingrese la opción deseada (1-7):\n"))
        
        if opcion == 1:
            print(f"Ha seleccionado la opción: {opcion}. Agregar Producto.")
            agregar_producto()
        elif opcion == 2:
            print(f"Ha seleccionado la opción: {opcion}. Mostrar Producto.")
            mostrar_productos()
        elif opcion == 3:
            print(f"Ha seleccionado la opción: {opcion}. Actualizar Producto.")
            actualizar_producto()
        elif opcion == 4:
            print(f"Ha seleccionado la opción: {opcion}. Eliminar Producto.")
            eliminar_producto()
        elif opcion == 5:
            print(f"Ha seleccionado la opción: {opcion}. Buscar Producto.")
            buscar_producto()        
        elif opcion == 6:
            print(f"Ha seleccionado la opción: {opcion}. Reporte de Bajo Stock.")
            reporte_bajo_stock()
        elif opcion == 7:
            print("Saliendo del programa. ¡Hasta luego!")
            #cerramos conexión con la base de datos 
            conexion.close()
            break  
           
#Función main donde se crea el inventario y se ejecuta el menú
def main():
    crear_inventario()
    menu()      

main()