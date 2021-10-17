#Super listas que contienen diccionarios y super diccionarios que contienen listas

#  Vamos a crear todo un entorno virtual.  Basicamente, creamos el .gitignore para incluir adentro la carpeta venv/, que no necesitamos que sea visible en nuestro repositorio en github.
# Podemos tener diccionarios que guarden listas y listas que guarden diccionarios. Vamos a ver con que:
# 1.	Vamos a crear el archivo list_and_dicts.py
# 2.	Vamos a crear nuestras buenas practicas para función y entry point
# def run():
#     pass

# if __name__ == '__main__':
#     run()


# 3.	Vamos a recordar el concepto de lista, creando una lista llamada my_list = [1, “Hello”, True, 4.5]
# 4.	Luego crearemos un diccionario llamado my_dict = {“firstname”: “Felipe”, “lastname”: “Restrepo”}
# 5.	Ahora crearemos una super lista para demostrar que podemos colocar diccionarios dentro de listas, que tendrá la estructura
# super¬¬_list = [ 
#                                          {“firstname”: “Felipe”, “lastname”: “Restrepo”},
#                                          {“firstname”: “Facundo”, “lastname”: “Garcia”},
#                                         {“firstname”: “Miguel”, “lastname”: “Torres”},
#                                         {“firstname”: “Pepe”, “lastname”: “Mujica”},

# ]
# Dejamos este espacio adentro para poder incluir los diccionarios que contendrá esta lista. Alli adentro pegaremos este primer diccionario que tenemos, y lo separaremos con una coma. Luego podremos colocar otros diccionario

# 6.	Igualmente lo podremos hacer con los diccionarios, crearemos un super diccionario donde incluiremos listas
# Super_dict = {
#         “natural_nums”: [1, 2, 3, 4],
#         “integer_nums”: [-1, -2, 0, 1, 2],
#          “floating_nums”: [1.1, 4.5, 6.43]
# }

# 7.	Para demostrar que funcionan, haremos un ciclo for.
# a.	Vamos a recorrer tanto llaves como valores entonces será for key, value,
# b.	Utilizaremos el método .items que nos permite recorrer las llaves y valores al mismo tiempo, de un diccionario en un ciclo.
# c.	Ahora adentro del ciclo haremos el print(key, “-“, value)




def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"}

super_list = [
    {"firstname": "Felipe", "lastname": "Restrepo"},
    {"firstname": "Miguel", "lastname": "Torres"},
    {"firstname": "Pepe", "lastname": "Rodelo"},
    {"firstname": "Jose", "lastname": "Garcia"},
]

super_dict = {
    "natural_nums": [1, 2, 3, 4, 5],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [1.1, 4.5, 6.4],

}

for key, value in super_dict.items():
    print(key, "-", value)

if __name__ == '__main__':
    run()
