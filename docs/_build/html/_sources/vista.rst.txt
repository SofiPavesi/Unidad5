Interfaz Gráfica (Tkinter)
===========================

El archivo `main.py` maneja la **interfaz gráfica** utilizando `Tkinter`, proporcionando un entorno visual para gestionar el inventario de productos.  

Clase `VentanaPrincipal`
------------------------

Esta clase representa la ventana principal de la aplicación y actúa como intermediaria entre el usuario y la base de datos.  

.. code-block:: python

    class VentanaPrincipal():
        def __init__(self, window):
            self.root = window
            self.root.title("Gestión de Inventario")
            self.objetodb = Abmc()

    # Esta clase inicializa la ventana principal y se conecta con la base de datos.

Funciones principales
---------------------

La clase `VentanaPrincipal` cuenta con los siguientes métodos para la gestión del inventario:

- **`altaProducto()`**: Agrega un nuevo producto.  
- **`actualizar()`**: Modifica un producto existente.  
- **`consultar()`**: Busca un producto por ID.  
- **`borrar()`**: Elimina un producto de la base de datos.  
