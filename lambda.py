# Recordemos que una function, funcion, es código que escribimos una vez, nos permite no reutilizar código y nos permite, además, utilizarlo posteriormente.
# Hay una manera distinta de crear funciones, funciones sin nombre o anónimas, son lambda functions, es decir, no tienen un identificador.
# La sintaxis es la siguiente, notando que tenemos una palabra clave llamada lambda.
# lambda argumentos: expresión 
# Las funciones lambda pueden tener los argumentos que nosotros necesitemos, pero es solo una línea de código, una sola expresión. En JavaScript por ejemplo, las funciones si pueden tener mas de una línea de código, pero en Python solo una.

# Vamos a recordar nuestra funcion de palíndromo. En lambda se escribiría de esta manera. La estructura se lee así: vamos a tener un argumento, que es es un parámetro que recibe la función para trabajar, además de la palabra clave lambda, vamos a tener una expresión y vamos a tener una variable, que tiene un identificador, que NO es de la función, sino que es una variable que contiene un objeto de tipo función que retorna toda esa expresión de Python. Es decir, la funcion es anónima, pero el identificador con el que llamaremos la funcion es el identificador de la variable.

palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))


# Con funciones normales se haría de esta manera
def palindrome(string):
    return string == string[::-1]

print(palindrome('ana'))

