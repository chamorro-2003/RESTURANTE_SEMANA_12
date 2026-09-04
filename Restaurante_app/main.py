from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


# Función de mostrar menú
def mostrar_menu() -> None:
    """Muestra el menú usando una sola cadena multilínea formateada."""
    menu_texto = """
=============================================
      SISTEMA DE GESTIÓN DE RESTAURANTE      
=============================================
1. Registrar Producto
2. Listar Productos
3. Buscar Producto por ID
4. Registrar Usuario
5. Listar Usuarios
6. Buscar Usuario por ID
7. Realizar Venta
8. Consultar Ventas por Usuario
9. Salir
============================================="""
    print(menu_texto)


# Función principal
def main() -> None:
    servicio_archivo = ArchivoServicio()
    restaurante = Restaurante()

    # Carga datos JSON e inicializa índices
    prods = servicio_archivo.cargar_productos()
    usrs = servicio_archivo.cargar_usuarios()
    vts = servicio_archivo.cargar_ventas()
    restaurante.establecer_datos(prods, usrs, vts)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            try:
                p_id = int(input("ID único del producto: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                categoria = input("Categoría: ")
                stock = int(input("Stock inicial: "))

                prod = Producto(p_id, nombre, precio, categoria, stock)
                if restaurante.registrar_producto(prod):
                    servicio_archivo.guardar_productos(restaurante.obtener_productos())
                    print(" Producto registrado correctamente.")
            except ValueError as e:
                print(f"¡Error! Entrada inválida: {e}")

        elif opcion == "2":
            print("\n--- CATÁLOGO DE PRODUCTOS ---")
            lista = restaurante.obtener_productos()
            if not lista:
                print("No existen productos registrados.")
            for p in lista:
                print(p)

        elif opcion == "3":
            try:
                p_id = int(input("Ingrese el ID del producto a buscar: "))
                prod = restaurante.buscar_producto(p_id)
                if prod:
                    print(f"\n Producto encontrado: {prod}")
                else:
                    print("¡Error! Producto no encontrado.")
            except ValueError:
                print("¡Error! El ID debe ser un número entero.")

        elif opcion == "4":
            try:
                u_id = input("ID/Cédula del Usuario: ")
                nombre = input("Nombre completo: ")
                rol = input("Rol (Cliente/Admin): ")
                usr = Usuario(u_id, nombre, rol if rol else "Cliente")
                if restaurante.registrar_usuario(usr):
                    servicio_archivo.guardar_usuarios(restaurante.obtener_usuarios())
                    print("Usuario registrado correctamente.")
            except ValueError as e:
                print(f"¡Error! {e}")

        elif opcion == "5":
            print("\n--- LISTA DE USUARIOS ---")
            lista = restaurante.obtener_usuarios()
            if not lista:
                print("No existen usuarios registrados.")
            for u in lista:
                print(u)

        elif opcion == "6":
            u_id = input("Ingrese el ID/Cédula del usuario a buscar: ")
            usr = restaurante.buscar_usuario(u_id)
            if usr:
                print(f"\n Usuario encontrado: {usr}")
            else:
                print("¡Error! Usuario no encontrado.")

        elif opcion == "7":
            try:
                u_id = input("ID/Cédula del Usuario comprador: ")
                p_id = int(input("ID del Producto a comprar: "))
                cant = int(input("Cantidad: "))

                if restaurante.vender_producto(u_id, p_id, cant):
                    servicio_archivo.guardar_productos(restaurante.obtener_productos())
                    servicio_archivo.guardar_ventas(restaurante.obtener_ventas())
            except ValueError as e:
                print(f"¡Error! Entrada inválida: {e}")

        elif opcion == "8":
            u_id = input("Ingrese la identificación del Usuario: ")
            ventas = restaurante.consultar_ventas_usuario(u_id)
            print(f"\n--- VENTAS REGISTRADAS PARA EL USUARIO: {u_id} ---")
            if not ventas:
                print("No se registraron ventas para este usuario.")
            for v in ventas:
                p = restaurante.buscar_producto(v.producto_id)
                nombre_p = p.nombre if p else "Producto Desconocido"
                print(f"{v} | Producto: {nombre_p}")

        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("¡Error! Opción inválida. Seleccione un número de 1 a 9.")


if __name__ == "__main__":
    main()
