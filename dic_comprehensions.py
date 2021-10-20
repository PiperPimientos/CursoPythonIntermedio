# Lo mismo que hicimos con listas, ahora con diccionarios.

# Reto: un diccionario cuya llave sean los primeros 100 numeros naturales y cuyos valores sean esos numeros pero elevados al cubo
# De manera clásica seria asi:
# 1.	dentro de nuestra función run guardaremos un diccionario vacio 
# my_dict = { }
# 2.	Crearemos un ciclo for i in range(1, 101): y lo que haremos es guardar en cada una de las i, que son nuestras llaves, asignado a esa misma i elevada al cubo
#            my_dict[i] = i**3
# 3.	Luego solo print(my_dict)
# 4.	Al final nuestro entry point que corra nuestra función run

def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i**3

    print(my_dict)

if __name__ == '__main__':
    run()

# Ahora, como lo resumimos en una línea con los dictionary comprehensions?

# 1.	Vamos a crear nuestro my_dict = { } y dentro de las llaves estará todo el código que necesitamos. La lógica es que ponemos i : como llave luego i**3 como valor, luego el ciclo, para cada i en el rango de 1 a 101

my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}


# Estructura:
# {key :value for value in iterable if condition}
# Se lee: para cada elemento en un iterable, yo voy a colocar una llave y un valor, solamente si se cumple una condición.

 
# RETO: Crear un nuevo dictionary comprehension, cuyas llaves sean lo 1000 primeros numeros naturales con sus raíces cuadradas como valores


def run():

    my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}
#El round es para redondearlos solo a 2 decimales
    print(my_dict)

if __name__=='__main__':
    run()