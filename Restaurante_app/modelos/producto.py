from typing import Dict, Any


class Producto:
    """Clase que representa un producto del restaurante con gestión de stock."""

    def __init__(
        self,
        producto_id: int,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int = 0,
    ) -> None:
        if producto_id <= 0:
            raise ValueError("El ID del producto debe ser un entero positivo.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if not categoria or not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.producto_id: int = int(producto_id)
        self.nombre: str = nombre.strip()
        self.precio: float = float(precio)
        self.categoria: str = categoria.strip()
        self.stock: int = int(stock)

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock disponible tras validar la cantidad."""
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente para realizar la venta.")
        self.stock -= cantidad

    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte los atributos de Producto a un diccionario compatible con JSON."""
        return {
            "producto_id": self.producto_id,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock,
        }

    def __str__(self) -> str:
        return f"ID: {self.producto_id} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}"
