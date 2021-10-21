# High order funcions
# O funciones de orden superior, son funciones que reciben como parámetro a otra función.
# Funciones de orden superior de importancia:
# •	filter → recibe una función filtro (anónima) y un iterable (lista, tupla, etc) devolviendonos un iterador: objeto optimizado recorrer elemento a elemento (iterar) por lo que no lo podemos inprimir de manera directa (para ello lo convertimos a una lista), su sintaxis es: filter(<funcion filtro>, <iterable>)

# Veamos un ejemplo

# Tenemos una lista aleatoria de numeros, 1, 4, 5, 6, 9, 13, 19, 21. Pero solo quiero en una lista los impares, entonces me quedan 1, 5, 9, 13, 19, 21

# Esto lo podríamos desarrollar por ejemplo, por list comprehensions o un ciclo for de toda la vida.

# Pero con filter podemos hacerlo de esta manera. Analicemos esta pieza de código:

my_list = [1, 4, 5, 6, 9, 15, 19, 21]

odd = [i for i in my_list if i % 2 != 0]

print(odd)


# Ahora bien, esto mismo lo podemos hacer con filter
# Analicemos la siguiente línea de código:


my_list = [1, 4, 5, 6, 9, 15, 19, 21]
odd = list(filter(lambda x: x % 2 != 0, my_list))
print(odd)


# •	map → al igual que filter recibe una función anónima y un iterable como parámetros pero en este caso map ejecuta la función sobre cada uno de los elementos del iterable, sintaxis: map(<funcion>, <iterable>)

# Veamos un ejemplo, tenemos una lista de numeros del 1 al 5. Y como resultado quiero una lista de los mismos numeros elevados al cuadrado.

# Esto se puede hacer tanto con un for o con un list comprehensions. 


my_list = [1, 2, 3, 4, 5]
squares = [i**2 for i in my_list]
print(squares)

# donde la lógica es que, para cada i en mi lista, voy a colocar a esa i, elevada al cuadrado.

# Pero para hacerlo con map, hacemos lo siguiente

my_list = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, my_list))

print(squares)

# •	reduce → tenemos que importar esta función desde functools para poder usarla, tiene los mismos argumentos que las anteriores funciones, reduce el iterable por medio de la función anonima, su sintaxis es: reduce(<funcion reduccion>, <iterable>), la función de reducción necesita de dos parámetros, uno que almacena el resultado (o el primer valor del iterable) y otro que opera con el siguiente valor del iterable: lambda a,b: <expresión>

# Reduce es mas sencillo. Veamos el siguiente ejemplo

# tengo una lista de 5 veces el numero 2 y quiero obtener a partir de esta lista al numero 32 multiplicando todos los elementos.

# Como reduzco los valores de esta lista a un único valor. Veamos como lo haríamos con un ciclo for:


my_list = [2, 2, 2, 2, 2]

all_multiplied = 1

for i in my_list:
    all_multiplied = all_multiplied * i

print(all_multiplied)

# donde tenemos una lista con 5 numeros 2. Luego un valor llamado all_multiplied, que significa todos los numeros multiplicados, con valor de 1. Luego vamos a recorrer con un for cada uno de los elementos en my_list y, en cada iteración, se va guardar a ese numero de la iteración, multiplicado por el valor del ciclo, es decir por i. En otros términos, en la primera iteración, all multiplied que vale 1, se va multiplicar por 2, luego en la siguiente iteración, ya ese 2 que quedo como resultado se multiplica por el siguiente numero en lista que es 2, y asi sucesivamente.

# Con reduce es lo mismo, con la misma estructura que vimos en las high order functions anteriores. Pero con la diferencia de que tendremos que importar el método reduce del modulo fuctools

from functools import reduce

my_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda a, b: a * b, my_list)

print(all_multiplied)

# Hay una estructura un poco distinta. 
# 1.	Lambda lleva dos parámetros a y b y multiplica a y b, a y b son el primer y segundo elemento de nuestra lista. En la segunda iteración pasa lo mismo que hacíamos con el ciclo for, donde el resultado, es decir 4, pasara a ser el parámetro a, y el siguiente numero de la lista es el parámetro b



#Ahora veremos el proyecto de filtrando datos con estas tres high order functions