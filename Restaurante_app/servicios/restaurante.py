from typing import List, Optional, Dict, Set
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Clase que representa un restaurante y gestiona productos, usuarios y ventas."""

    def __init__(self) -> None:
        # Inicializa las listas principales y los índices auxiliares
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []

        # Índices auxiliares para búsquedas rápidas
        self._indice_productos: Dict[int, Producto] = {}
        self._indice_usuarios: Dict[str, Usuario] = {}
        self._indice_ventas_usuario: Dict[str, List[Venta]] = {}

        self._ids_productos: Set[int] = set()
        self._ids_usuarios: Set[str] = set()

    def _reconstruir_indices(self) -> None:
        """Reconstruye los índices auxiliares a partir de las listas principales."""
        self._indice_productos = {p.producto_id: p for p in self._productos}
        self._ids_productos = {p.producto_id for p in self._productos}

        self._indice_usuarios = {u.usuario_id: u for u in self._usuarios}
        self._ids_usuarios = {u.usuario_id for u in self._usuarios}

        self._indice_ventas_usuario = {}
        for v in self._ventas:
            if v.usuario_id not in self._indice_ventas_usuario:
                self._indice_ventas_usuario[v.usuario_id] = []
            self._indice_ventas_usuario[v.usuario_id].append(v)

    def establecer_datos(
        self, productos: List[Producto], usuarios: List[Usuario], ventas: List[Venta]
    ) -> None:
        """Establece los datos iniciales del restaurante y reconstruye los índices auxiliares."""
        self._productos = productos
        self._usuarios = usuarios
        self._ventas = ventas
        self._reconstruir_indices()

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def obtener_usuarios(self) -> List[Usuario]:
        return self._usuarios

    def obtener_ventas(self) -> List[Venta]:
        return self._ventas

    # Búsquedas y registros con índices auxiliares para eficiencia
    def buscar_producto(self, producto_id: int) -> Optional[Producto]:
        """ Búsqueda directa en O(1) mediante diccionario."""
        return self._indice_productos.get(producto_id)

    def buscar_usuario(self, usuario_id: str) -> Optional[Usuario]:
        """ Búsqueda directa en O(1) mediante diccionario."""
        return self._indice_usuarios.get(str(usuario_id).strip())

    def registrar_producto(self, nuevo_producto: Producto) -> bool:
        """Registro de un producto manteniendo sincronizados los índices en memoria."""
        if nuevo_producto.producto_id in self._ids_productos:
            print(f"¡Error! Ya existe un producto con el ID {nuevo_producto.producto_id}.")
            return False

        self._productos.append(nuevo_producto)
        self._indice_productos[nuevo_producto.producto_id] = nuevo_producto
        self._ids_productos.add(nuevo_producto.producto_id)
        return True

    def registrar_usuario(self, nuevo_usuario: Usuario) -> bool:
        """Registro de un usuario manteniendo sincronizados los índices en memoria."""
        if nuevo_usuario.usuario_id in self._ids_usuarios:
            print(
                f"¡Error! Ya existe un usuario registrado con la identificación {nuevo_usuario.usuario_id}."
            )
            return False

        self._usuarios.append(nuevo_usuario)
        self._indice_usuarios[nuevo_usuario.usuario_id] = nuevo_usuario
        self._ids_usuarios.add(nuevo_usuario.usuario_id)
        return True

    def vender_producto(self, usuario_id: str, producto_id: int, cantidad: int) -> bool:
        """Venta de un producto a un usuario, actualizando stock y registrando la venta."""
        usuario = self.buscar_usuario(usuario_id)
        producto = self.buscar_producto(producto_id)

        if usuario is None:
            print(f"¡Error! Venta rechazada: El usuario con ID '{usuario_id}' no existe.")
            return False
        if producto is None:
            print(f"¡Error! Venta rechazada: El producto con ID {producto_id} no existe.")
            return False
        if cantidad <= 0:
            print("¡Error! Venta rechazada: La cantidad debe ser mayor a cero.")
            return False
        if producto.stock < cantidad:
            print(
                f"¡Error! Venta rechazada: Stock insuficiente ({producto.stock} disponibles)."
            )
            return False

        # Registro de venta
        nuevo_id_venta = len(self._ventas) + 1
        producto.vender(cantidad)

        nueva_venta = Venta(
            nuevo_id_venta, usuario.usuario_id, producto.producto_id, cantidad
        )
        self._ventas.append(nueva_venta)

        # Sincronización del índice de ventas por usuario
        if usuario.usuario_id not in self._indice_ventas_usuario:
            self._indice_ventas_usuario[usuario.usuario_id] = []
        self._indice_ventas_usuario[usuario.usuario_id].append(nueva_venta)

        print(
            f"¡Venta realizada con éxito! Nuevo stock de '{producto.nombre}': {producto.stock}"
        )
        return True

    def consultar_ventas_usuario(self, usuario_id: str) -> List[Venta]:
        """Consulta las ventas realizadas por un usuario específico utilizando el índice auxiliar."""
        id_limpio = str(usuario_id).strip()
        return self._indice_ventas_usuario.get(id_limpio, [])
