from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import modelo
# ##############################################
# FUNCIONES AUXILIARES PARA VISTA
# ##############################################

def altaProucto(nombre, descripcion, cantidad, precio, categoria, tree):
    modelo.altaProducto(nombre, descripcion, cantidad, precio, categoria, tree)


# ##############################################
# VISTA (LO QUE SE MUESTRA EN PANTALLA SE PONE ENTRE EL ROOT.TK() Y TERMINA EN ROOT.MAINLOOP())
# ##############################################
#Controlador
root = Tk()
root.title("Gestión de Inventario")
        
titulo = Label(root, text="Alta de Productos", bg="HotPink2", fg="thistle1", height=1, width=30)
titulo.grid(row=0, column=0, columnspan=2, padx=1, pady=1, sticky=W+E)

titulo2 = Label(root, text="Consulta de Productos por ID", bg="lemonchiffon4", fg="thistle1", height=1, width=30)
titulo2.grid(row=0, column=2, columnspan=2, padx=1, pady=1, sticky=W+E)

titulo3 = Label(root, text="Actualización y Baja de Productos", bg="Cyan4", fg="thistle1", height=1, width=30)
titulo3.grid(row=11, column=0, columnspan=2, padx=1, pady=1, sticky=W+E)

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
paso1 = Label(root, text=" 1.       Listar todos los productos del Inventario -->")
paso1.grid(row=12, column=0, sticky=W)
paso2 = Label(root, text=" 2.       Seleccioná el producto a actualizar/borrar.")
paso2.grid(row=13, column=0, sticky=W)
paso3 = Label(root, text=" 3.       Completá TODOS los campos (solo si vas actualizar). ")
paso3.grid(row=14, column=0, sticky=W)
paso4 = Label(root, text=" 4.       Clickeá la opción seleccionada -->        ")
paso4.grid(row=15, column=0, sticky=W)


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
tree.grid(row=20, column=0, columnspan=4)


#lambda constituye la comunicación pasando información al bucle
boton_alta=Button(root, text="Alta", bg="HotPink3", command=lambda:altaProducto(a_val.get(), b_val.get(), c_val.get(),d_val.get(),e_val.get(), tree))
boton_alta.grid(row=7, column=1, sticky=W+E)

boton_consulta = Button(root, text="Consultar",bg="antiqueWhite4", command=lambda: consultar(f_val.get(), tree))
boton_consulta.grid(row=3, column=3)

boton_borrar=Button(root, text="Borrar", bg="dim gray", command=lambda:borrar(tree))
boton_borrar.grid(row=16, column=1, sticky=W+E )

boton_actualizar = Button(root, text="Actualizar", bg="lightblue4", command=lambda: actualizar(tree, a_val, b_val, c_val,d_val,e_val))
boton_actualizar.grid(row=15, column=1,sticky=W+E)

boton_listar = Button(root, text="Listado", bg="lightblue3", command=lambda: actualizar_treeview(tree))
boton_listar.grid(row=12, column=1,sticky=W+E)
root.mainloop()