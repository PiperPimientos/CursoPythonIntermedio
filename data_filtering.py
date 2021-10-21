# Vamos a utilizar las high order functions, filtrando datos.

# Tendremos una lista de diccionarios, donde tendremos una lista de empleados con todos sus datos. Y lo que haremos es hacer varias high order functions y algunas list comprehensions para filtrar esos datos, por ejemplo, si de una lista de empleados queremos saber solo los que trabajan en platzi o solo los que manejan Python como lenguaje.

# 1.	Vamos a crear nuestra funcion y nuestro entry poit de buenas practicas.
# 2.	Vamos a analizar la constante DATA. Vemos que es una lista que contiene diccionarios, dentro de los diccionarios veremos varias llaves con su respectivo valor.
# 3.	A partir de esta lista de diccionarios. Vamos a colocar los distintos filtros. Que hacemos para ponerlo en practica?
# a.	Vamos a nuestra funcion run() y creamos una lista llamada all_python_devs que va contener el nombre de los trabajadores, esta lista va contener a worker, que sera cada uno de los diccionarios internos, de worker quiero el contenido de la llave “name” y le agregamos el ciclo a ese list comprehensions con un for worker in DATA. Es decir, para todos los trabajadores que están dentro de DATA, yo voy a guardar el contenido de la llave nombre. Solo si, worker language, es decir el lenguaje que domina, es igual a Python. if worker[“language”] == “python”
# b.	vamos a crear un ciclo para ver el resultado de esto for worker in all_python_devs: print(worker).
# c.	inmediatamente nos daría como resultado la lista de los nombres
# 4.	Si queremos una lista con todos los trabajadores de Platzi, aplicamos la misma estructura a un list comprehension llamado all_Platzi_workers
# 5.	Haremos otras listas, como los mayores de 18 años, y utilizaremos para este caso filters, combinando las high order functions con las lambda.
# a.	Crearemos una lista llamada adults que va contener un list() que va contener un filter() que va contener dos parámetros, una lambda function y luego un iterable que será DATA.
# b.	nuestra funcion lambda va contener cada uno de los elementos que contiene el iterador DATA, que contiene diccionarios, los cuales hemos llamado worker, y solo lo llamaremos si este trabajador es mayor a 18
# list(filter(lambda worker: worker[“age”] > 18, DATA))
# c.	Sin embargo si lo ejecutamos a este punto, nos sale todo el diccionario completo y yo solo quiero que muestre el age y la edad. Esto lo podemos resorver con un high order function, el map
# Ponemos la misma estructura, pero en vez de un filter, colocamos un map, pero del diccionario solo pediremos el “name”, pero ya no viene del iterable DATA sino de adults
# list(map(lambda worker: worker[“name”], adults))


# Y ahora, si tendremos a los adultos, en sus nombres solamente y no en el diccionario completo

# 6.	Vamos con un ultimo ejemplo para probar otra high order function. Crearemos una nueva lista de diccionarios, pero en lugar de tener las llaves tradicionales, tendrá una llave mas que será true or false como contenido, será llamada old, para saber si la persona es mayor a 70 años o menor
# a.	creamos la variable old_people
# b.	Lo haremos con la funcion map, que le pasaremos como lambda un worker
# list(map(lambda worker: worker | (“old”: worker[“age”] > 78, DATA))
# Esta quiza es la línea de código mas compleja hasta el momento, desde el curso Basico de Python. Pero podemos explicarla, analizarla desde adentro hacia afuera.
# tenemos un list() que lo que hace es transformarnos en lista el resultado de la funcion map(). La funcion map() lleva dos parámetros, una lambda function y un iterable, en este caso todo hasta DATA, es la function, 
# Lo que estamos haciendo es transformar cada uno de los diccionarios que tenemos en DATA en un diccionario nuevo que es la combinación de nuestro diccionario original con un nuevo diccionario que unimos con el operador |. La llave es una expresión llamada old que es el resultado de worker age, mayor a 70.
# El símbolo | es para sumar diccionarios. 


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# def run():
#     all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
#     all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
#     adults = list(filter(lambda worker: worker["age"] > 18, DATA))
#     adults = list(map(lambda worker: worker["name"], adults))
#     old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

#     for worker in all_python_devs:
#         print(worker)

# if __name__ == '__main__':
#     run()



# RETO: Crear las listas all_python_devs y all_Platzi_workers usando una combinación de filter y map.
# Crear la lista old_people y adults con list comprehensions.

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in all_python_devs:
        print(worker)

if __name__ == '__main__':
    run()



# RETO: Crear las listas all_python_devs y all_Platzi_workers usando una combinación de filter y map.
# Crear la lista old_people y adults con list comprehensions.


    
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
#     En mi caso tengo python 3.8.3, por lo que utilicé la sintaxis
# z = {**x, **y} --> para sumar diccionarios o agregar una nueva key.
#Pero de una forma antigua, seria asi
    old_confirmation = lambda worker_age: worker_age > 70
    old_people = [worker | {'old': old_confirmation(worker['age'])} for worker in DATA]
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    all_Platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzi_workers = list(map(lambda worker: worker["name"], all_Platzi_workers))
