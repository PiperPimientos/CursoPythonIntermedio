
# Y si quiero crear una lista de los primeros cien números naturales elevados al cuadrado.

# 1.	Creamos nuestra función y nuestro entry point
# 2.	Dentro de la función creamos una lista vacia llamada squares
# squares = [ ]
# 3.	Creamos un ciclo for i in range(1, 101):
# a.	adentro llamaremos a nuestra función squares.append(i**2) es decir, en cada ciclo elevaremos i al cuadrado y ese resultado lo agregaremos a la lista con el método .append.
# 4.	Ahora solo queda hacer el print(squares)
# 5.	Si ejecutamos nuestro programa veremos que tendremos una lista de los 100 primeros numeros naturales elevados al cuadrado.


# def run():
#     squares = []
#     for i in range(1, 101):
#         squares.append(i**2)
    
#     print(squares)

# if __name__ == '__main__':
#     run()

# Ahora, pero si quiero guardar solo el cuadrado de los numeros que no sean divisibles entre 3

# 1.	 antes de sacar del append del cuadrado, voy a poner la condicional: si el resto de la división de i entre 3, es distinto de 0, por lo tanto la división no es exacta, es decir no es divisible entre 3, voy a guardar en mi lista a ese numero elevado al cuadrado
# if i % 3 != 0:
#       squares.append(i**2)


# def run():
#     squares = []
#     for i in range(1, 101):
#         if i % 3 != 0:
#             squares.append(i**2)
    
#     print(squares)

# if __name__ == '__main__':
#     run()

# Todo esto que acabamos de hacer se podria resumir en una sola línea de codigo mediante list comprehensions
# 1.	La lógica de nuestro anterior ejemplo seria: i elevado al cuadrado para todas las i dentro el rango de numeros hasta el 100, solo si i modulo 3 es distinto de 0

# squares = [i**2 for i in range(1, 101) if i % 3 != 0]

# [element for element in iterable if condition]

 

# Esto se leeria: para cada elemento en el iterable, ese elemento, solo si se cumple la condición 

# Con nuestro ejemplo seria: para cada i en los numeros del 1 al 100, voy a guardar esa i al cuadrado, solo si no es divisible por 3.

 

# RETO: crear con un list comprehensions, una lista de todos lo múltiplos de 4 que a la vez también son múltiplos de 6 y 9 hasta 5 digitos Es decir desde el 1 hasta el 99999, revisando si cada uno de los elementos es multiplo de 4,  6 y 9

# solo uso el 36 por que es el numero multiplo de 4, 6 y 9 al mismo tiempo.

squares = [ i for i in range(1, 100000) if i % 36 == 0]
print(squares)