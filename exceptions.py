# Para trabajar las excepciones utilizaremos unas palabras claves que hasta el momento no habíamos visto, estas son raise, try, except y finally.
# Vamos primero con try, except, que se traduce como: probar y excepto que ___, hago lo siguiente
# Vamos a trabajar con un error en el ejemplo clásico que es el del palíndromo.

# def palindrome(string):
#     return string == string [::-1]

# print(palindrome(1))

# Si nos fijamos bien, estamos queriendo hacer un palíndromo pero con un numero entero que es un 1, y generalmente lo tenemos que hacer es con una frase. Esto nos va pasar mucho, por ejemplo creando aplicaciones web donde tendremos un formulario y un usuario va ingresar algo que no esperábamos, vamos a tener que saber como arreglarlo.
# Si lo leemos como lo vimos en clases anteriores, empezamos desde el final,
# 1.	Tenemos que es un TypeError y que tenemos un objeto tipo int que is not suscriptable
# 2.	Nos dice que tenemos un error en el archivo, en la línea dos, en la funcion palindrome
# 3.	Si seguimos leyendo el traceback hacia arriba, vamos a poder ver tendremos otro error pero ahora en esa línea 4 que corresponde al print
# Como utilizamos el try, except?
# Si sabemos que nos va saltar error cuando ingresemos ese int, pues la lógica es que le devolvamos un mensaje que indique que solo se pueden ingresar strings. La sintaxis es la siguiente

def palindrome(string):
    return string == string [::-1]

try:
    print(palindrome(1))
except TypeError:
    print("Solo se pueden ingresar strings")

# La lógica se lee asi: 
# Prueba imprimir el palíndrome del int 1, excepción: si hay un typeError, entonces imprime “solo se pueden ingresar strings”

# Ahora, puede suceder que en nuestro programa tengamos un error, pero Python no lo detecta en si como un error. Lo vamos a resolver con la palabra clave raise, veamos un ejemplo:
# Supongamos que tenemos el mismo ejemplo, pero ahora en vez de pasarle el 1, le pasamos una cadena vacia al try
# try:
#     print(palindrome(“ “))

# Y esto también esta mal, porque no deberíamos permitirle al usuario que el valor que ingrese sea null o nada.
# En el caso de hacerlo con el try, except, el valor retornado va ser True, porque aunque efectivamente es un null, pues además, es un string, tiene las comillas, entonces el valor va ser True.
# Con raise vamos a incorporarlo, veamos el siguiente bloque de código

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacia ')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")


# Tenemos al final el try except normal, que teníamos antes, con el string vacio.
# Pero arriba, en la definición de la funcion tenemos un try, except que envuelve a todo el código de la funcion. Dentro del try la lógica es: si la longitud de la string es 0, entonces vamos a elevar(raise) un error de tipo ValueError -una excepción de tipo ValueError- y entre paréntesis el mensaje de error que python devolverá. Si la longitud del string es distinta a 0, retornamos el resultado de la expresión string que es igualdad a string[::-1]. Despues tenemos el except, que nos dice, que si sucede un ValueError as ve, vamos a ejecutar ese print, explicando el error.
# Nota: tenemos una nueva palabra clave que es as, esto lo único que hace es ponerle un nombre al error y en el ejemplo ve es una abreviatura de ValueError.


# Luego tenemos la palabra clave finally, que se usa al final de una estructura try, except, para hacer varias cosas particulares, como lo son: cerrar un archivo dentro de Python, cerrar una conexión a una base de datos, o liberar recursos externos.
# Ejemplo

try:
    f = open("archivo.txt")
finally:
    f.close()

