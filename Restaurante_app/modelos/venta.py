from typing import Dict, Any


class Venta:
    """Clase que representa la transacción realizada por un usuario sobre un producto."""

    def __init__(
        self, venta_id: int, usuario_id: str, producto_id: int, cantidad: int
    ) -> None:
        if venta_id <= 0:
            raise ValueError("El ID de venta debe ser un entero positivo.")
        if not usuario_id or not str(usuario_id).strip():
            raise ValueError("El ID de usuario es obligatorio.")
        if producto_id <= 0:
            raise ValueError("El ID de producto es obligatorio.")
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor a cero.")

        self.venta_id: int = int(venta_id)
        self.usuario_id: str = str(usuario_id).strip()
        self.producto_id: int = int(producto_id)
        self.cantidad: int = int(cantidad)

    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte el objeto Venta a diccionario para guardar en JSON."""
        return {
            "venta_id": self.venta_id,
            "usuario_id": self.usuario_id,
            "producto_id": self.producto_id,
            "cantidad": self.cantidad,
        }

    def __str__(self) -> str:
        return f"Venta #{self.venta_id} | Usuario ID: {self.usuario_id} | Producto ID: {self.producto_id} | Cantidad: {self.cantidad}"
