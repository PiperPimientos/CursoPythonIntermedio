
# Crearemos el archivo debugging_2.py que será una copia de debugging para poder aplicar el manejo de exceptions a el código que teníamos como ejemplo para debugging.


# def divisors(num):
#     divisors = []
#     for i in range(1, num + 1):
#         # if num % i == 1:   #ESTE ERA EL ERROR
#         if num % i == 0:
#             divisors.append(i)
#     return divisors

# def run():
#     num = int(input("Ingresa un numero: "))
#     print(divisors(num))
#     print("Termino el programa")

# if __name__ == '__main__':
#     run()


# Si maliciosamente introducimos un string ‘a’ en vez de el entero que nos pide el programa, veremos como nos salta un ValueError

# Si leemos el Traceback completo, entenderemos que el programa falla en num, y veremos que se esta introduciendo un valor de tipo str y no el valor de tipo int que nos pide el input.
# 1.	Lo que haremos entonces para resolver este problema, es que el bloque de código de la funcion run() lo meteremos todo dentro de un try: 
# 2.	Luego colocaremos el except y veremos que la excepción que nos surge es que es una excepción de tipo ValueError, y si sucede esta excepción, lo que haremos es imprimir en pantalla “debes ingresar un numero entero”


# def divisors(num):
#     divisors = []
#     for i in range(1, num + 1):
#         # if num % i == 1:   #ESTE ERA EL ERROR
#         if num % i == 0:
#             divisors.append(i)
#     return divisors

# def run():
#     try:
#         num = int(input("Ingresa un numero: "))
#         print(divisors(num))
#         print("Termino el programa")
#     except ValueError:
#         print("Debes ingresar un numero")

# if __name__ == '__main__':
#     run()


# Reto: Utiliza las palabras clave, try, except y raise para elevar un error si el usuario ingresa un numero negativo en nuestro programa de divisores. Porque tenemos pensado que el programa funcione solo con numeros positivos.


def divisors(num):
    try:
        if num < 0:
            raise ValueError("No se pueden ingresar numeros negativos ")
        divisors = []
        for i in range(1, num + 1):
            # if num % i == 1:   #ESTE ERA EL ERROR
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Termino el programa")
    except ValueError:
        print("Debes ingresar un numero")

if __name__ == '__main__':
    run()



# Otra solucion que nos permite agregar un ciclo while 1-x para ejecutar en bucle

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        # if num % i == 1:   #ESTE ERA EL ERROR
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    while True:
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")

if __name__ == '__main__':
    run()