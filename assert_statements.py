# Ya vimos la manera clásica de manejar los errores en Python con try, except, raise, finally. Pero hay algo mas, los assert statements o afirmaciones en Python, que marcan un diferencial en nuestra carrera. Estas son expresiones, como las que conocemos, combinando variables con operadores. 
# El flujo es mas o menos este.

 
# Tenemos código, tenemos el assert que es una afirmación, que si se cumple, devuelve true, seguimos con el código, pero si esta afirmación no se cumple, se devuelve un error.
# La estructura de un assert seria algo asi:


# assert condicion, mensaje de error

# tenemos una palabra clave assert, tenemos una condición que va devolver verdadero o falso y luego un mensaje de error.
# Y se lee: afirmo que esta condición es verdadera, sino imprime este mensaje de error.
# Veamos un ejemplo con la funcion palindrome.
# El caso que tenemos es que estamos intentanto introducir un string vacio que nos va devolver true.


def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacia"
    return string == string [::-1]

print(palindrome(""))


# Lo que dice es: afirmo que la longitud del string es mayor a cero para que se ejecute el programa, sino corta el programa y dale este mensaje de error.

# Y lo que nos devuelve Python es un AssertionError con el mensaje de error.

# Vamos a solucionar, ese problema que teníamos en nuestro programa de divisores, pero ahora con afirmaciones.

# Ahora, si cuando nos pide que ingresemos un numero, ingresamos la letra a, nos va dar un ValueError. Para resolverlo:

# 1.	Antes de comenzar, utilizaremos un método especial de los strings, llamado .isnumeric, que lo que hace es devolver True si el string se corresponde a una especie de numero y False si no se corresponde. Si el usuario ingresa la letra a, la línea va devolver False, esa será la condición que tendrá nuestro assert statement
# 2.	Debajo de num en nuestra funcion run(), vamos a incluir el assert y vamos a colocar la condición que queremos que se cumpla y el mensaje de error, que para este caso será con la siguiente lógica: afirmo que si num es numerico, entonces es True el assert statement y si no es numerico entonces es False.
# assert num.isnumeric(), “Debes ingresar un numero”
# 3.	Pero para que funcione tenemos que eliminar la funcion int que contiene el input que esta dentro de num, porque isnumeric es un método de cadenas de caracteres, strings.
# 4.	Y por ultimo, si el assert se cumple, lo que tendremos que hacer es enviarle ese string, pero convertido a int en la funcion divisors.


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        # if num % i == 1:   #ESTE ERA EL ERROR
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = (input("Ingresa un numero: "))
    # assert num.isnumeric(), "Debes ingresar un numero"
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un numero positivo" #RETO, evitar que ingrese numero negativo
    print(divisors(int(num)))
    print("Termino el programa")

if __name__ == '__main__':
    run()

