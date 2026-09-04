import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """Persistencia en formato JSON para el sistema."""

    def __init__(self, carpeta_datos: str = "datos") -> None:
        self.carpeta_datos: str = carpeta_datos
        self.ruta_productos: str = os.path.join(carpeta_datos, "productos.json")
        self.ruta_usuarios: str = os.path.join(carpeta_datos, "usuarios.json")
        self.ruta_ventas: str = os.path.join(carpeta_datos, "ventas.json")
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)

    # --- PRODUCTOS ---
    def guardar_productos(self, productos: List[Producto]) -> bool:
        try:
            datos = [p.a_diccionario() for p in productos]
            with open(self.ruta_productos, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
            return True
        except PermissionError:
            print(" ¡Error! Permisos insuficientes para escribir productos.json.")
            return False

    def cargar_productos(self) -> List[Producto]:
        productos: List[Producto] = []
        try:
            with open(self.ruta_productos, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for item in datos:
                    try:
                        p = Producto(
                            producto_id=int(item["producto_id"]),
                            nombre=str(item["nombre"]),
                            precio=float(item["precio"]),
                            categoria=str(item["categoria"]),
                            stock=int(item.get("stock", 0)),
                        )
                        productos.append(p)
                    except (KeyError, ValueError) as e:
                        print(
                            f" ¡Advertencia! Registro de producto ignorado por inconsistencia: {e}"
                        )
        except FileNotFoundError:
            print(" ¡Archivo 'productos.json' no encontrado! Se inicia lista vacía.")
        except json.JSONDecodeError:
            print(" ¡Advertencia! Archivo 'productos.json' corrupto. Se cargará vacío.")
        except PermissionError:
            print(" ¡Error! Permisos insuficientes para leer productos.json.")
        return productos

    # --- USUARIOS ---
    def guardar_usuarios(self, usuarios: List[Usuario]) -> bool:
        try:
            datos = [u.a_diccionario() for u in usuarios]
            with open(self.ruta_usuarios, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
            return True
        except PermissionError:
            print(" ¡Error! Permisos insuficientes para escribir usuarios.json.")
            return False

    def cargar_usuarios(self) -> List[Usuario]:
        usuarios: List[Usuario] = []
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for item in datos:
                    try:
                        u = Usuario(
                            usuario_id=str(item["usuario_id"]),
                            nombre=str(item["nombre"]),
                            rol=str(item.get("rol", "Cliente")),
                        )
                        usuarios.append(u)
                    except (KeyError, ValueError) as e:
                        print(f" ¡Advertencia! Registro de usuario ignorado: {e}")
        except FileNotFoundError:
            print(" ¡Archivo 'usuarios.json' no encontrado! Se inicia lista vacía.")
        except json.JSONDecodeError:
            print(" ¡Advertencia! Archivo 'usuarios.json' corrupto. Se cargará vacío.")
        except PermissionError:
            print(" ¡Error! Permisos insuficientes para leer usuarios.json.")
        return usuarios

    # --- VENTAS ---
    def guardar_ventas(self, ventas: List[Venta]) -> bool:
        try:
            datos = [v.a_diccionario() for v in ventas]
            with open(self.ruta_ventas, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
            return True
        except PermissionError:
            print(" ¡Error! Permisos insuficientes para escribir ventas.json.")
            return False

    def cargar_ventas(self) -> List[Venta]:
        ventas: List[Venta] = []
        try:
            with open(self.ruta_ventas, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for item in datos:
                    try:
                        v = Venta(
                            venta_id=int(item["venta_id"]),
                            usuario_id=str(item["usuario_id"]),
                            producto_id=int(item["producto_id"]),
                            cantidad=int(item["cantidad"]),
                        )
                        ventas.append(v)
                    except (KeyError, ValueError) as e:
                        print(f" ¡Advertencia! Registro de venta ignorado: {e}!")
        except FileNotFoundError:
            print(" ¡Archivo 'ventas.json' no encontrado! Se inicia lista vacía.")
        except json.JSONDecodeError:
            print(" ¡Advertencia! Archivo 'ventas.json' corrupto. Se cargará vacío.")
        except PermissionError:
            print(" ¡Error! Permisos insuficientes para leer ventas.json.")
        return ventas
