Introducción
==============

"El Sistema de Gestión de Inventario es una aplicación de escritorio desarrollada en Python con la biblioteca Tkinter. 
Su objetivo es facilitar la administración de productos en un inventario, permitiendo realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar)
sobre una base de datos SQLite. Para una gestión eficiente y estructurada de los datos, el sistema utiliza el ORM Peewee, 
lo que permite interactuar con la base de datos de manera más intuitiva y segura, sin necesidad de escribir consultas SQL manuales. 
Esto mejora la mantenibilidad del código y reduce la posibilidad de errores en la manipulación de datos.
Este sistema está diseñado para ser intuitivo y eficiente, proporcionando una interfaz gráfica amigable
y un modelo de datos optimizado para la gestión de productos."

**Funcionalidades principales:**
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


* Alta, Baja y Modificación de productos.
* Consulta de productos por ID.
* Listado general de todos los productos.
* Persistencia de datos en una base SQLite.


Módulos principales:
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

+ 1. **Vista y Controlador(`main.py`)** → Maneja la interfaz gráfica con Tkinter y gestiona la comunicación entre la vista y el modelo.
+ 2. **Modelo (`modelo.py`)** → Gestiona la base de datos y la comunicación con SQLite.
