def tabla(seleccion_tabla):
    menu_multiplicacion = """
    SELECCIONE LA TABLA A VISUALIZAR
    **(OPC 01) TABLA DEL 1**
    **(OPC 02) TABLA DEL 2**
    **(OPC 03) TABLA DEL 3**
    **(OPC 04) TABLA DEL 4**  
    **(OPC 05) TABLA DEL 5**  
    **(OPC 06) TABLA DEL 6**  
    **(OPC 07) TABLA DEL 7**  
    **(OPC 08) TABLA DEL 8**
    **(OPC 09) TABLA DEL 9**

    Seleccione la opcion:  
    """
    seleccion = int(input(menu_multiplicacion))
    if seleccion == 1:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 2:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 3:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 4:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 5:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 6:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 7:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 8:
        operacion(seleccion_tabla, seleccion)
    elif seleccion == 9:
        operacion(seleccion_tabla, seleccion)
    else:
        print('No ha seleccionado una opcion correcta')
    


def operacion(tipo_tablas, tabla):
    if tipo_tablas == 1:
        print('Esta es la tabla de sumar ' + str(tabla))
        for i in range(1,12):
            print(i+tabla)
    elif tipo_tablas == 2:
        print('Esta es la tabla de sumar ' + str(tabla))
        for i in range(1,12):
            print(i*tabla)

def run():
    menu_tablas ="""
    SELECCIONE LA OPERACION A UTILIZAR 
    **(OPC 01) TABLA DE SUMAR 1**
    **(OPC 02) TABLA DE MULTIPLICAR 2**
    ingrese la opción: 
    """
    seleccion_tabla = int(input(menu_tablas))
    if seleccion_tabla == 1:
        tabla(seleccion_tabla)
    elif seleccion_tabla == 2:
        tabla(seleccion_tabla)
    else:
        print('No ha seleccionado una opcion correcta')


if __name__ == '__main__':
    run()
