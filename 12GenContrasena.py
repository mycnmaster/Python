import random
def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    minusculas = ['a','b','c', 'd', 'e']
    simbolos = ['!', '#', '$', '&', '%', '@', ')']
    numeros = ['1','2', '3', '4', '5', '6', '7', '8']

    caracteres = mayusculas + minusculas + simbolos +  numeros

    contrasena = []
    for i in range(15):
        caracter_randon = random.choice(caracteres)
        contrasena.append(caracter_randon)    
    contrasena = ''.join(contrasena)
    return contrasena.upp

        
def run():
 contrasena = generar_contrasena()
 print('Tu nueva contrasena es: '+ contrasena)

if __name__ == '__main__':
    run()