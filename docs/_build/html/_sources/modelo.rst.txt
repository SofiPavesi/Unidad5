Manejo de la Base de Datos
=================================

El archivo `modelo.py` se encarga de la **persistencia de datos**, utilizando SQLite como base de datos relacional. Este módulo administra todas las operaciones relacionadas con la gestión de productos en la base de datos.

Clase `Abmc`
------------

La clase `Abmc` es responsable de realizar las operaciones CRUD (Crear, Leer, Actualizar, Borrar) sobre la base de datos SQLite.

.. code-block:: python

    class Abmc:
        def __init__(self):
            # Inicialización de la conexión con la base de datos y configuración inicial.
            pass

        def conexion(self):
            # Establece la conexión con la base de datos SQLite.
            pass

        def crear_tabla(self):
            # Crea la tabla 'productos' si no existe en la base de datos.
            pass

        def altaProducto(self, producto):
            # Inserta un nuevo producto en la base de datos.
            pass

        def actualizar(self, id_producto, nuevos_datos):
            # Modifica un producto existente en la base de datos.
            pass

        def consultar(self, id_producto):
            # Busca un producto por ID en la base de datos.
            pass

        def borrar(self, id_producto):
            # Elimina un producto de la base de datos.
            pass

Métodos principales
-------------------

La clase incluye los siguientes métodos para la administración de la base de datos:

- **`conexion()`**: Establece la conexión con SQLite.  
- **`crear_tabla()`**: Crea la tabla `productos` si aún no existe.  
- **`altaProducto(producto)`**: Inserta un nuevo producto en la base de datos.  
- **`actualizar(id_producto, nuevos_datos)`**: Modifica un producto existente utilizando su ID.  
- **`consultar(id_producto)`**: Busca un producto en la base de datos por su ID.  
- **`borrar(id_producto)`**: Elimina un producto específico de la base de datos.  
