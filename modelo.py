from peewee import *
import re





# ##############################################
#                       MODELO                 #
# ##############################################

db=SqliteDatabase('inventario.db')
class BaseModel(Model):
    class Meta:
        database = db
        
class Productos(BaseModel):
    id= AutoField()
    nombre= CharField()
    descripcion=CharField()
    cantidad=IntegerField()
    precio=FloatField()
    categoria=CharField()

db.connect()
db.create_tables([Productos]) 

   
class Abmc:
    def altaProducto(self, nombre, descripcion, cantidad, precio, categoria):
        Productos.create(
            nombre=nombre,
            descripcion=descripcion,
            cantidad=cantidad,
            precio=precio,
            categoria=categoria
        )
    
    def actualizar(self, id_prod, nombre, descripcion, cantidad, precio, categoria):     
        query = (Productos.update(
            nombre=nombre,
            descripcion=descripcion,
            cantidad=cantidad,
            precio=precio,
            categoria=categoria
        ).where(Productos.id == id_prod))
        query.execute()
        
    def consultar(self, id_buscado):
        resultado = Productos.get_or_none(Productos.id == id_buscado)
        return resultado
    
    def borrar(self, id_prod):
        eliminar = (Productos.delete()
                    .where(Productos.id == id_prod))
        eliminar.execute()
           
    def extraer_bd(self):
        return list(Productos.select().tuples())
    





