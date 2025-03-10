import sqlite3



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

    def actualizar(self,nombre, descripcion, cantidad, precio, categoria,id_prod):
        con = self.conexion()
        cursor = con.cursor()
        sql = "UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id = ?"
        data = (str(nombre), str(descripcion), int(cantidad), float(precio), str(categoria), int(id_prod))       
        cursor.execute(sql, data)
        con.commit()
        con.close()

    def consultar(self, id_buscado, tree):
        con = self.conexion()
        cursor = con.cursor()
        sql = "SELECT * FROM productos WHERE id = ?"
        cursor.execute(sql, (id_buscado,))
        resultado = cursor.fetchone()
        con.close()
        return resultado


    def borrar(self, mi_id):
        con = self.conexion()
        cursor = con.cursor()
        sql = "DELETE FROM productos WHERE id = ?"
        cursor.execute(sql, (mi_id,))
        con.commit()
        con.close()



    def extraer_bd(self):
        con = self.conexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM productos")
        resultado = cursor.fetchall()
        con.close()
        return resultado
