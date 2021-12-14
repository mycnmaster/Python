# pesos = input("Cuantos pesos a colombianos tienes?: ")
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dolares")
def conversor(tipo_pesos,valor_dolar):
    pesos = float(input("Cuantos pesos "+tipo_pesos+" tienes ?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares) 
    print("Tienes $" + dolares + "dólares")

menu_1 = """
Bienvenido al conversor de monedas 🧳

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int (input(menu_1))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion==2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opcion correcta')

