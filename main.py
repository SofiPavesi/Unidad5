from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from modelo import Abmc

# ##### #
# VISTA #
# ##### #

class VentanaPrincipal():
    def __init__(self, window):
        self.root = window
        self.root.title("Gestión de Inventario")
        self.objetodb = Abmc()
    
        # ################################# #
        # FUNCIONES AUXILIARES PARA VISTA   #
        # ################################# #
        def actualizar_treeview(self, mitreview):
            records = mitreview.get_children()
            for element in records:
                mitreview.delete(element)
            retorno = self.objetodb.extraer_bd()
            for fila in retorno:
                print(fila)
                mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3],fila[4],fila[5]))
                
        def altaProducto(nombre, descripcion, cantidad, precio, categoria):
            retorno = self.objetodb.altaProducto(nombre, descripcion, cantidad, precio, categoria)
            print(retorno)
            #limpiar campos que usé para crear el producto
            a_val.set(""), b_val.set(""), c_val.set(0), d_val.set(0.0), e_val.set("")
            actualizar_treeview(self,tree)
            


        def actualizar(id_prod,nombre, descripcion, cantidad, precio, categoria):
            item_seleccionado = tree.selection() 
            if not item_seleccionado:
                showwarning("Advertencia", "Debes seleccionar un producto.")
                return
            
            id_prod = tree.item(item_seleccionado[0], 'text')  # 'text' es el ID (primer columna)
            
            retorno = self.objetodb.actualizar(id_prod, nombre, descripcion, cantidad, precio, categoria)
            a_val.set(""), b_val.set(""), c_val.set(0), d_val.set(0.0), e_val.set("")
            actualizar_treeview(self,tree)
            print(retorno)
            
        def consultar(id_consultado,tree):
            retorno = self.objetodb.consultar(id_consultado, tree)
            print(retorno)
            
        def borrar(tree):
            retorno = self.objetodb.borrar(tree)
            actualizar_treeview(self,tree)
            print(retorno)

                
        titulo = Label(self.root, text="Alta de Productos", bg="HotPink2", fg="thistle1", height=1, width=30)
        titulo.grid(row=0, column=0, columnspan=2, padx=1, pady=1, sticky=W+E)

        titulo2 = Label(self.root, text="Consulta de Productos por ID", bg="lemonchiffon4", fg="thistle1", height=1, width=30)
        titulo2.grid(row=0, column=2, columnspan=2, padx=1, pady=1, sticky=W+E)

        titulo3 = Label(self.root, text="Actualización y Baja de Productos", bg="Cyan4", fg="thistle1", height=1, width=30)
        titulo3.grid(row=11, column=0, columnspan=2, padx=1, pady=1, sticky=W+E)

        nombre = Label(self.root, text="Producto")
        nombre.grid(row=2, column=0, sticky=W)
        descripcion = Label(self.root, text="Descripción")
        descripcion.grid(row=3, column=0, sticky=W)
        cantidad=Label(self.root, text="Cantidad")
        cantidad.grid(row=4, column=0, sticky=W)
        precio=Label(self.root, text="Precio")
        precio.grid(row=5, column=0, sticky=W)
        categoria=Label(self.root, text="Categoria")
        categoria.grid(row=6, column=0, sticky=W)
        id_prod=Label(self.root, text="ID para Consulta")
        id_prod.grid(row=2, column=2, sticky=W)
        paso1 = Label(self.root, text=" 1.       Listar todos los productos del Inventario -->")
        paso1.grid(row=12, column=0, sticky=W)
        paso2 = Label(self.root, text=" 2.       Seleccioná el producto a actualizar/borrar.")
        paso2.grid(row=13, column=0, sticky=W)
        paso3 = Label(self.root, text=" 3.       Completá TODOS los campos (solo si vas actualizar). ")
        paso3.grid(row=14, column=0, sticky=W)
        paso4 = Label(self.root, text=" 4.       Clickeá la opción seleccionada -->        ")
        paso4.grid(row=15, column=0, sticky=W)


        # Defino variables para tomar valores de campos de entrada
        a_val, b_val, c_val, d_val, e_val, f_val = StringVar(), StringVar(), IntVar(), DoubleVar(), StringVar(), IntVar()
        w_ancho = 20


        entrada2 = Entry(self.root, textvariable = a_val, width = w_ancho) 
        entrada2.grid(row = 2, column = 1)
        entrada3 = Entry(self.root, textvariable = b_val, width = w_ancho) 
        entrada3.grid(row = 3, column = 1)
        entrada4 = Entry(self.root, textvariable = c_val, width = w_ancho) 
        entrada4.grid(row = 4, column = 1)
        entrada5 = Entry(self.root, textvariable = d_val, width = w_ancho) 
        entrada5.grid(row = 5, column = 1)
        entrada6 = Entry(self.root, textvariable = e_val, width = w_ancho) 
        entrada6.grid(row = 6, column = 1)
        entrada7 = Entry(self.root, textvariable = f_val, width = w_ancho) 
        entrada7.grid(row = 2, column = 3)


        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        tree = ttk.Treeview(self.root)
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
        boton_alta=Button(self.root, text="Alta", bg="HotPink3", command=lambda: altaProducto(a_val.get(), b_val.get(), c_val.get(),d_val.get(),e_val.get()))
        boton_alta.grid(row=7, column=1, sticky=W+E)

        boton_consulta = Button(self.root, text="Consultar",bg="antiqueWhite4", command=lambda:  consultar(f_val.get(), tree))
        boton_consulta.grid(row=3, column=3)

        boton_borrar=Button(self.root, text="Borrar", bg="dim gray", command=lambda: borrar(tree))
        boton_borrar.grid(row=16, column=1, sticky=W+E )

        boton_actualizar = Button(self.root, text="Actualizar", bg="lightblue4", command=lambda: actualizar(a_val.get(), b_val.get(), c_val.get(),d_val.get(),e_val.get(),f_val.get()))

        boton_actualizar.grid(row=15, column=1,sticky=W+E)

        boton_listar = Button(self.root, text="Listado", bg="lightblue3", command=lambda: actualizar_treeview(self, tree))
        boton_listar.grid(row=12, column=1,sticky=W+E)

            


# ########### #
# CONTROLADOR #
# ########### #
if __name__ == "__main__":
    root = Tk()
    obj1=VentanaPrincipal(root)
    root.mainloop()