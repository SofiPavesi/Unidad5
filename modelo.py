import sqlite3
from tkinter.messagebox import *
from tkinter import *


# ##############################################
#                       MODELO                 #
# ##############################################



class Abmc:
    def __init__(self):
        try:
            self.conexion()
            self.crear_tabla()
        except Exception as e:
            print(f"Error en la inicialización: {e}")

    def conexion(self):
        return sqlite3.connect("inventario.db")

    def crear_tabla(self):
        con = self.conexion()
        cursor = con.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS productos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nombre TEXT NOT NULL, 
                        descripcion TEXT NOT NULL, 
                        cantidad INTEGER NOT NULL, 
                        precio REAL NOT NULL, 
                        categoria TEXT NOT NULL )'''
        cursor.execute(sql)
        con.commit()
        con.close()

    def altaProducto(self,nombre, descripcion, cantidad, precio, categoria):
        con = self.conexion()
        cursor = con.cursor()
        data = (nombre, descripcion, cantidad, precio, categoria)
        sql = "INSERT INTO productos(nombre, descripcion, cantidad, precio, categoria) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        con.close()
        showinfo("Éxito", "Producto agregado correctamente.")
        

    def actualizar(self,id_prod,nombre, descripcion, cantidad, precio, categoria):
        con = self.conexion()
        cursor = con.cursor()
        sql = "UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id_prod = ?"
        data = (str(nombre), str(descripcion), int(cantidad), float(precio), str(categoria), int(id_prod))        
        cursor.execute(sql, data)
        con.commit()
        con.close()
        showinfo("Éxito", "Producto actualizado correctamente.")

    def consultar(self, id_buscado, tree):
        try:
            id_buscado = int(id_buscado)
        except ValueError:
            showerror("Error", "Debe ingresar un ID numérico válido.")
            return

        con = self.conexion()
        cursor = con.cursor()
        sql = "SELECT * FROM productos WHERE id = ?"
        cursor.execute(sql, (id_buscado,))
        resultado = cursor.fetchone()
        con.close()

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

    def borrar(self, tree):
        valor = tree.selection()
        if not valor:
            showerror("Error", "Debe seleccionar un producto para borrar.")
            return

        item = tree.item(valor)
        mi_id = item['text']
        confirmacion = askyesno("Confirmar eliminación", f"¿Seguro que desea eliminar el producto con ID {mi_id}?")
        
        if confirmacion:
            con = self.conexion()
            cursor = con.cursor()
            sql = "DELETE FROM productos WHERE id = ?"
            cursor.execute(sql, (mi_id,))
            con.commit()
            con.close()
            tree.delete(valor)
            showinfo("Éxito", "Producto eliminado correctamente.")

    def extraer_bd(self):
        con = self.conexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM productos")
        resultado = cursor.fetchall()
        con.close()
        return resultado
