from typing import Dict, Any


class Usuario:
    """Clase que representa un usuario o cliente registrado en el sistema."""

    def __init__(self, usuario_id: str, nombre: str, rol: str = "Cliente") -> None:
        if not usuario_id or not str(usuario_id).strip():
            raise ValueError("El ID/Cédula del usuario no puede estar vacío.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")

        self.usuario_id: str = str(usuario_id).strip()
        self.nombre: str = nombre.strip()
        self.rol: str = rol.strip()

    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte los atributos de Usuario a un diccionario compatible con JSON."""
        return {"usuario_id": self.usuario_id, "nombre": self.nombre, "rol": self.rol}

    def __str__(self) -> str:
        return (
            f"ID Usuario: {self.usuario_id} | Nombre: {self.nombre} | Rol: {self.rol}"
        )
