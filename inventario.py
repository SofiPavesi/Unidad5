from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re
# ##############################################
# MODELO
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
 

def consultar(compra):
    
    print(compra)

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





# ##############################################
# VISTA (LO QUE SE MUESTRA EN PANTALLA SE PONE ENTRE EL ROOT.TK() Y TERMINA EN ROOT.MAINLOOP())
# ##############################################

root = Tk()
root.title("Gestión de Inventario")
        
titulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)


nombre = Label(root, text="Producto")
nombre.grid(row=2, column=0, sticky=W)
descripcion = Label(root, text="Descripción")
descripcion.grid(row=3, column=0, sticky=W)
cantidad=Label(root, text="Cantidad")
cantidad.grid(row=4, column=0, sticky=W)
precio=Label(root, text="Precio")
precio.grid(row=5, column=0, sticky=W)
categoria=Label(root, text="Categoria")
categoria.grid(row=6, column=0, sticky=W)
id_prod=Label(root, text="ID para Consulta")
id_prod.grid(row=2, column=2, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val, d_val, e_val, f_val = StringVar(), StringVar(), IntVar(), DoubleVar(), StringVar(), IntVar()
w_ancho = 20


entrada2 = Entry(root, textvariable = a_val, width = w_ancho) 
entrada2.grid(row = 2, column = 1)
entrada3 = Entry(root, textvariable = b_val, width = w_ancho) 
entrada3.grid(row = 3, column = 1)
entrada4 = Entry(root, textvariable = c_val, width = w_ancho) 
entrada4.grid(row = 4, column = 1)
entrada5 = Entry(root, textvariable = d_val, width = w_ancho) 
entrada5.grid(row = 5, column = 1)
entrada6 = Entry(root, textvariable = e_val, width = w_ancho) 
entrada6.grid(row = 6, column = 1)
entrada7 = Entry(root, textvariable = f_val, width = w_ancho) 
entrada7.grid(row = 2, column = 3)

# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------

tree = ttk.Treeview(root)
tree["columns"]=("col1", "col2", "col3","col4","col5")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.column("col4", width=200, minwidth=80)
tree.column("col5", width=200, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="Producto")
tree.heading("col2", text="Descripción")
tree.heading("col3", text="Cantidad")
tree.heading("col4", text="Precio")
tree.heading("col5", text="Categoria")
tree.grid(row=10, column=0, columnspan=4)

boton_alta=Button(root, text="Alta", command=lambda:altaProducto(a_val.get(), b_val.get(), c_val.get(),d_val.get(),e_val.get(), tree))
boton_alta.grid(row=7, column=1)

boton_consulta = Button(root, text="Consultar", command=lambda: consultar(f_val.get(), tree))
boton_consulta.grid(row=3, column=3)

boton_borrar=Button(root, text="Borrar", command=lambda:borrar(tree))
boton_borrar.grid(row=9, column=1)
root.mainloop()


