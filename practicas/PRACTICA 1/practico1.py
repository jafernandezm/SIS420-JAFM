def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1 Nombre', accion1),
        '2': ('Opción 2 Cu', accion2),
        '3': ('Opción 3 Telefono', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Jhon Alan Fernandez Maturano')


def accion2():
    print('Cu:	111-410')


def accion3():
    print('telefono 68643975')


def salir():
    print('Saliendo')



menu_principal()