# Este es el reto final: el juego del ahorcado. Tiene bastantes cosas:
# asi debe funcionar.
# 1.	Creamos un archivo llamado juego_del_ahorcado.py
# 2.	Vamos a tener que crear un script donde ejecutemos el programa y Python nos diga: adivina la palabra, luego la cantidad de espacios que ocupa la palabra y al final el input de ingresa una letra:
# 3.	Si ingresamos de a letra, veremos como se completa el juego
 

# 4.	Y que cuando ganes, te tire un mensaje:
 

# Tenemos que poner en practica todo lo aprendido en el curso.
# Hay unas reglas:
# -Incorporar comprehensions, manejo de errores y manejo de archivos
# -Utiliza el archivo data.txt y leelo para obtener las palabras.
# Ayudas y pistas:
# -Investigar la funcion enumerate
# -Investigar método get de los diccionarios puede servirnos
# -La sentencia
# os.system(“cls”) -> Windows
# os.system(“cls”) -> Unix
# Servira para limpiar pantalla. Porque cada vez que ponemos una letra, la pantalla se limpia y se vuelve a colocar la interfaz que habíamos desarrollado
# SI queremos mejorar el juego
# -Podemos ponerle un sistema de puntos
# -Dibuja el ahorcado en cada jugada con código ASCII
# -Mejora la interfaz.

# Comentario útil:
# Para el que empieza perdido en el juego les comparto el camino que seguí para desarrollarlo, aunque las sugerencias al código son muy bien recibidas, se que tiene mucho por mejorar. Estos son los pasos:
# -Leer el archivo con las palabras. (También vi que algunos lo creaban en el caso que el archivo no estuviera, me pareció buena función y lo agregue).
# -Escoger una palabra del archivo aleatoriamente.
# -Recibir una letra de parte del jugador.
# -Crear un string o lista con el caracter “_” debe ser del tamaño de la palabra escogida.
# -Las tildes generan problemas, se deben traducir en letras sin tildes.
# -Encontrar las veces que la letra se encuentra en la palabra y en que posición están.
# -Ubicar la letra en la posición correspondiente dentro del espacio con las rayas al piso.
# -Reescribir cada vez que el usuario adivina una letra.
# -Validar si ya encontró la palabra completa.
# -Crear el sistema de puntos.
# -Crear el banner con código ASCII, hay varias paginas para hacerlo fácilmente (solo hay que tener en cuenta que algunos caracteres se ven en windows y en linux no)
# Espero a alguien le sirva de ayuda.!



import random
import os

def read(filepath="./files_project.txt/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())

        return words


def run():
    data = read(filepath="./files_project.txt/data.txt")
    IMAGES = ["""
  +---+
  |   |
      |
      |
      |
      |
=========

  +---+
  |   |
  O   |
      |
      |
      |
=========

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    """]

    word = random.choice(data)
    word_list = [letter for letter in word]
    word_list_underscores = ["_"] * len(word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    attemps = 6

    while True:
        os.system("clear")
        print("Adivina la palabra")
        for element in word_list_underscores:
            print(element + " ", end=" ")
        letter = input("Elige una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"


         
        if letter in word_list:
            for idx in letter_index_dict[letter]:
                word_list_underscores[idx] = letter
        
        if "_" not in word_list_underscores:
            os.system("clear")
            print("Ganaste, la palabra era", word)
            break
            imput()
        


if __name__ == '__main__':
    run()

#EN CONSTRUCCION.