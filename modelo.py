from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk

# ##############################################
#                       MODELO                 #
# ##############################################
def conexion():
    con = sqlite3.connect("inventario.db")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = ('''CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL, 
                    descripcion TEXT NOT NULL, 
                    cantidad INTEGER NOT NULL, 
                    precio REAL NOT NULL, 
                    categoria TEXT NOT NULL )
                    ''');
    cursor.execute(sql)
    con.commit()

try:
    conexion()
    crear_tabla()
except:
    print("Hay un error")

def altaProducto(nombre, descripcion, cantidad, precio, categoria, tree):
 
    print(nombre, descripcion, cantidad, precio, categoria)
    con=conexion()
    cursor=con.cursor()
    data=(nombre, descripcion, cantidad, precio, categoria)
    sql="INSERT INTO productos(nombre, descripcion, cantidad, precio, categoria) VALUES(?, ?, ?, ?,?)"
    cursor.execute(sql, data)
    con.commit()
    print("Alta de producto realizada correctamente.")
    actualizar_treeview(tree)
    return ("alta realizada.")


def actualizar(tree, a_val, b_val, c_val, d_val, e_val):
    valor = tree.selection()
    
    if not valor:
        showerror("Error", "Debe seleccionar un producto para actualizar.")
        return
    
    item = tree.item(valor)
    mi_id = item["text"]  # ID del producto (columna #0)
    
    # Obtener los nuevos valores desde las entradas
    nuevo_nombre = a_val.get()
    nueva_descripcion = b_val.get()
    nueva_cantidad = c_val.get()
    nuevo_precio = d_val.get()
    nueva_categoria = e_val.get()
    
     # Actualizar el producto en la base de datos
    con = conexion()
    cursor = con.cursor()
    sql = "UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id = ?"
    data = (nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria, mi_id)
    cursor.execute(sql, data)
    con.commit()

    # Mostrar mensaje de éxito y actualizar el Treeview
    showinfo("Éxito", "Producto actualizado correctamente.")
    actualizar_treeview(tree)
    

def consultar(id_buscado, tree):
    try:
        id_buscado = int(id_buscado)
    except ValueError:
        showerror("Error", "Debe ingresar un ID numérico válido.")
        return

    con = conexion()
    cursor = con.cursor()

    sql = "SELECT * FROM productos WHERE id = ?"
    cursor.execute(sql, (id_buscado,))
    resultado = cursor.fetchone()

    if resultado:
        mensaje = (f"ID: {resultado[0]}\n"
                   f"Producto: {resultado[1]}\n"
                   f"Descripción: {resultado[2]}\n"
                   f"Cantidad: {resultado[3]}\n"
                   f"Precio: ${resultado[4]:.2f}\n"
                   f"Categoría: {resultado[5]}")
        showinfo("Producto encontrado", mensaje)

        for item in tree.get_children():
            tree.delete(item)
        tree.insert("", 0, text=resultado[0], values=(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5]))
    else:
        showwarning("Sin resultados", "No se encontró un producto con el ID ingresado.")

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM productos WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)

def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM productos ORDER BY id ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3],fila[4],fila[5]))



