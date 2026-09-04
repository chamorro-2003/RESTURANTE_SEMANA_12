<div align="justify">
  
# RESTURANTE_SEMANA_12

# Universidad Estatal Amazonica (UEA)

# Sistema de Gestión de Restaurante - Optimización de Rendimiento mediante Colecciones

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

---

## Descripción General del Sistema

Este proyecto corresponde a una nueva versión del sistema **restaurante_app**, en la cual se incorporan mejoras orientadas a optimizar el rendimiento de las operaciones realizadas con productos, usuarios y ventas, manteniendo las listas como colecciones principales para almacenar y conservar la información en archivos **JSON**, mientras que se utilizan estructuras auxiliares como diccionarios y conjuntos para realizar búsquedas y validaciones de manera más rápida, evitando recorridos innecesarios y permitiendo que el sistema sea más eficiente conforme aumenta la cantidad de datos.

---

## Estructura del Proyecto

El sistema mantiene una organización modular que permite separar las responsabilidades de cada componente, de manera que la carpeta datos conserva la información mediante archivos **JSON**, modelos contiene las clases principales del sistema, servicios administra la lógica de negocio y las estructuras utilizadas para mejorar el rendimiento, mientras que **main.py** funciona como punto de entrada y permite al usuario interactuar con las diferentes opciones mediante la consola.

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

## Mejoras de Rendimiento

Para mejorar la velocidad de las operaciones, se incorporaron estructuras auxiliares en el archivo **restaurante.py**, por lo que el diccionario _indice_productos permite encontrar productos directamente mediante su **ID**, mientras que **_indice_usuarios** facilita la búsqueda de usuarios, además, **_indice_ventas_usuario** organiza las ventas según el usuario para consultar su historial sin recorrer todas las ventas, finalmente, los conjuntos **_ids_productos** y **_ids_usuarios** permiten comprobar rápidamente si un **ID** ya existe, evitando así registros duplicados y reduciendo recorridos innecesarios.

---

## Sincronización de Colecciones

Las estructuras auxiliares deben mantenerse actualizadas para que siempre coincidan con las listas principales, por esta razón, cuando el sistema inicia y recupera la información desde los archivos **JSON**, se ejecuta **_reconstruir_indices()** para volver a crear los índices en memoria, posteriormente, cada vez que se registra un **producto**, **usuario** o **venta**, la información se incorpora tanto a las colecciones principales como a los índices correspondientes, garantizando que las búsquedas y validaciones trabajen con información actualizada durante toda la ejecución.

---

## Persistencia y Pruebas

Para comprobar las mejoras implementadas se inició el sistema con información previamente almacenada y se verificó que los productos y usuarios pudieran localizarse rápidamente mediante sus identificadores, posteriormente, se realizaron varias ventas para un mismo usuario y se consultó su historial utilizando el índice correspondiente, además, se intentó registrar productos y usuarios con **IDs** existentes para comprobar que los conjuntos rechazaran los duplicados, finalmente, se realizó una venta exitosa y se verificó que el stock se actualizara correctamente tanto en memoria como en **productos.json**, mientras que la nueva transacción quedara registrada en **ventas.json**.

---

## Reflexión Final

La incorporación de diccionarios y conjuntos demuestra que la elección adecuada de las estructuras de datos puede mejorar considerablemente el funcionamiento de una aplicación, ya que permiten realizar búsquedas, validaciones y consultas de manera más eficiente sin modificar la estructura principal del sistema, de esta manera, las listas continúan siendo útiles para almacenar la información y mantener la persistencia, mientras que los índices auxiliares optimizan las operaciones más frecuentes, logrando un sistema más rápido, organizado y preparado para trabajar con una mayor cantidad de datos.

<div>
