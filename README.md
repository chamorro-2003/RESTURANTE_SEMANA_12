<div align="justify">
  
# RESTURANTE_SEMANA_12

# Universidad Estatal Amazonica (UEA)

# Sistema de Gestión de Restaurante - Relaciones, Ventas y Persistencia de Datos en JSON

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

---

## Descripción General del Sistema

Este proyecto corresponde a una nueva versión del sistema **restaurante_app**, en la cual se incorporan relaciones entre diferentes entidades mediante el uso de **Programación Orientada a Objetos**, permitiendo gestionar productos, usuarios y ventas de una manera más organizada y cercana a un escenario real, además, el sistema incorpora el control de stock y el registro de las ventas realizadas, de manera que cada compra pueda relacionarse con un usuario y un producto específico, mientras que la información se conserva mediante archivos independientes en formato **JSON**, permitiendo recuperar los datos cuando la aplicación vuelve a ejecutarse.

---

## Estructura del Proyecto

El sistema se encuentra organizado en módulos para separar las responsabilidades y facilitar la comprensión del código, de manera que la carpeta llamada **datos** almacena la información persistente, la de **modelos** contiene las clases principales, en **servicios** se administra la lógica del sistema y el acceso a los archivos **JSON**, mientras que el archivo **main.py** funciona como punto de entrada y permite al usuario interactuar mediante un menú de consola.

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   ├── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.json
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

---
## Componentes Técnicos Aplicados
---

## Responsabilidad de las Clases y Módulos

Cada componente del proyecto cumple una función determinada para evitar mezclar responsabilidades y facilitar el mantenimiento del sistema, por lo tanto, la clase **Producto** representa los artículos disponibles en el restaurante y administra información como su identificación, nombre, precio, categoría y cantidad disponible en stock, mientras que **Usuario** representa a las personas registradas y permite identificar a quienes realizan las compras, por otra parte, **Venta** relaciona un usuario con un producto y una cantidad adquirida, mientras que **Restaurante** administra las colecciones y aplica las reglas necesarias para realizar las diferentes operaciones del sistema.

---

## Flujo de Venta

El proceso de venta comienza cuando el usuario selecciona el producto que desea comprar y proporciona su identificación, posteriormente, el sistema verifica que tanto el **usuario_id** como el **producto_id** existan en sus respectivas colecciones, luego se comprueba que la cantidad solicitada sea mayor que cero y que el producto tenga suficiente stock disponible, si todas las validaciones son correctas, se ejecuta **producto.vender(cantidad)** para disminuir las unidades disponibles, después se crea una nueva instancia de **Venta** con la información de la transacción y finalmente se actualizan los archivos **JSON**, permitiendo que el nuevo stock y la venta queden registrados de forma permanente.

---

## Persistencia y Pruebas

La persistencia permite que la información del sistema se conserve después de cerrar la aplicación, por lo que **productos.json** mantiene los productos y su stock actualizado, **usuarios.json** almacena los usuarios registrados y **ventas.json** conserva el historial de las transacciones realizadas, para comprobar este funcionamiento se registró un producto con 12 unidades de stock y se realizó ventas de los demás productos registrados, verificando que el stock disminuyera y que las ventas aparecieran en el archivo correspondiente, además, se realizó una prueba con una cantidad superior al stock disponible para comprobar que la operación fuera rechazada sin modificar los datos, finalmente, se reinició la aplicación y se verificó que la información permaneciera disponible y que el historial pudiera consultarse correctamente.

---

## Reflexión Final

La incorporación de relaciones entre entidades, control de inventario y persistencia en **JSON** permite que el sistema se aproxime cada vez más al funcionamiento de una aplicación real, ya que ahora no solamente se administran productos y usuarios, sino que también es posible relacionarlos mediante las ventas realizadas y conservar esta información después de cerrar el programa, además, la separación de responsabilidades facilita la comprensión del código y permite realizar cambios de manera más segura, fortaleciendo así el aprendizaje de **Programación Orientada a Objetos** y proporcionando una estructura preparada para incorporar nuevas funcionalidades en futuras versiones.

<div>
