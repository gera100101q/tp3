# ============================================================
# PROGRAMA: ASISTENTE DE MISION ESPACIAL - TP3 COLECCIONES
# Laboratorio de Aplicaciones II - 6 G - 2026
# ============================================================

def mostrar_menu():
    """Muestra las opciones del sistema de control."""
    print("\n" + "=" * 45)
    print("   SISTEMA DE CONTROL LUNAR - APOLO 11")
    print("=" * 45)
    print("  1. Playlist Dinamica de la Mision  (Listas)")
    print("  2. Promedio de Calificaciones      (Listas)")
    print("  3. Inventario de Productos  (Listas + Tuplas)")
    print("  4. Coordenadas Geograficas         (Tuplas)")
    print("  5. Registro de Invitados Unicos      (Sets)")
    print("  6. Salir")
    print("=" * 45)


# ------------------------------------------------------------
# OPCION 1: Playlist Dinamica (Listas)
# ------------------------------------------------------------
def opcion_playlist():
    print("\n--- OPCION 1: PLAYLIST DINAMICA ---")

    playlist_mision = []

    try:
        cantidad = int(input("Cuantas canciones deseas agregar?: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return

        for i in range(cantidad):
            cancion = input(f"  Cancion {i + 1}: ")
            playlist_mision.append(cancion)

        orden = input("Orden alfabetico: (A) Ascendente / (D) Descendente: ").strip().upper()
        if orden == "D":
            playlist_mision.sort(reverse=True)
            etiqueta = "Descendente"
        else:
            playlist_mision.sort()
            etiqueta = "Ascendente"

        print(f"\nLista de reproduccion final (Orden {etiqueta}):")
        print("-" * 30)
        for cancion in playlist_mision:
            print(f"  - {cancion}")

    except ValueError:
        print("Error: ingresa un numero entero valido.")


# ------------------------------------------------------------
# OPCION 2: Promedio de Calificaciones (Funciones de Listas)
# ------------------------------------------------------------
def opcion_promedio():
    print("\n--- OPCION 2: PROMEDIO DE CALIFICACIONES ---")

    calificaciones = []

    try:
        cantidad = int(input("Cuantas calificaciones deseas ingresar?: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return

        for i in range(cantidad):
            nota = float(input(f"  Calificacion {i + 1}: "))
            calificaciones.append(nota)

        total = sum(calificaciones)
        promedio = total / len(calificaciones)

        print("\nCalificaciones ingresadas:")
        print("-" * 30)
        for i, nota in enumerate(calificaciones, 1):
            print(f"  Nota {i}: {nota}")
        print("-" * 30)
        print(f"  Suma total : {total}")
        print(f"  Promedio   : {promedio:.2f}")

    except ValueError:
        print("Error: ingresa un numero valido.")


# ------------------------------------------------------------
# OPCION 3: Inventario de Productos (Listas + Tuplas)
# ------------------------------------------------------------
def opcion_inventario():
    print("\n--- OPCION 3: INVENTARIO DE PRODUCTOS ---")

    # Lista predefinida de tuplas (ID, Descripcion, Precio)
    inventario = [
        (101, "Casco Espacial",     15000.00),
        (102, "Traje Presurizado",  42000.50),
        (103, "Modulo de Oxigeno",   8500.75),
        (104, "Botas Magneticas",    6200.00),
        (105, "Guantes Termicos",    3100.25),
    ]

    print("\n{:<6} {:<22} {:>12}".format("ID", "Descripcion", "Precio ($)"))
    print("-" * 42)

    # Desempaquetado (unpacking) de cada tupla
    for id_prod, descripcion, precio in inventario:
        print("{:<6} {:<22} {:>12.2f}".format(id_prod, descripcion, precio))

    precio_total = sum(precio for _, _, precio in inventario)
    print("-" * 42)
    print("{:<28} {:>12.2f}".format("TOTAL DEL INVENTARIO:", precio_total))


# ------------------------------------------------------------
# OPCION 4: Coordenadas y Desempaquetado (Tuplas)
# ------------------------------------------------------------
def opcion_coordenadas():
    print("\n--- OPCION 4: COORDENADAS GEOGRAFICAS ---")

    try:
        x = float(input("Ingresa la coordenada X (latitud) : "))
        y = float(input("Ingresa la coordenada Y (longitud): "))

        # Almacenamos en una tupla (inmutable)
        coordenada = (x, y)

        print(f"\nCoordenada almacenada: {coordenada}")
        print(f"  Acceso por indice -> X: {coordenada[0]}  |  Y: {coordenada[1]}")

        # Demostracion de inmutabilidad mediante manejo de error
        print("\nIntentando modificar la coordenada...")
        try:
            coordenada[0] = 999  # Esto lanzara TypeError
        except TypeError as e:
            print(f"  Error capturado: {e}")
            print("  Las tuplas son INMUTABLES: no se puede reasignar un elemento.")

    except ValueError:
        print("Error: ingresa un numero valido.")


# ------------------------------------------------------------
# OPCION 5: Registro de Invitados Unicos (Sets)
# ------------------------------------------------------------
def opcion_invitados():
    print("\n--- OPCION 5: REGISTRO DE INVITADOS UNICOS ---")

    invitados = set()

    try:
        cantidad = int(input("Cuantos nombres deseas ingresar?: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return

        for i in range(cantidad):
            nombre = input(f"  Nombre {i + 1}: ").strip()
            antes = len(invitados)
            invitados.add(nombre)
            if len(invitados) == antes:
                print(f"  '{nombre}' ya estaba registrado. No se agrego duplicado.")

        print(f"\nTotal de invitados unicos: {len(invitados)}")
        print("Lista de invitados:")
        print("-" * 30)
        for nombre in invitados:
            print(f"  - {nombre}")

        buscar = input("\nIngresa un nombre para verificar si esta en la lista: ").strip()
        if buscar in invitados:
            print(f"  '{buscar}' SI esta en la lista de invitados.")
        else:
            print(f"  '{buscar}' NO esta en la lista de invitados.")

    except ValueError:
        print("Error: ingresa un numero entero valido.")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------
def ejecutar_asistente():
    nave = "Apolo 11"
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-6): ").strip()

        if opcion == "1":
            opcion_playlist()
        elif opcion == "2":
            opcion_promedio()
        elif opcion == "3":
            opcion_inventario()
        elif opcion == "4":
            opcion_coordenadas()
        elif opcion == "5":
            opcion_invitados()
        elif opcion == "6":
            print(f"\nCerrando conexion desde la nave {nave}. Hasta luego!")
            continuar = False
        else:
            print("Opcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    ejecutar_asistente()