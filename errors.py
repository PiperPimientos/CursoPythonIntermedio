# Una de las formas de encontrar errores de lógica en el código se denomina debuggin o depuración. El otro tipo de error es cuando Python si nos avisa que nos equivocamos, ahí lo que el lenguaje de programación hace es devolvernos un traceback.
# Cuando Python nos avisa, podemos dividir esos errores en dos 
 
# Errores en el código
# Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como traceback, puede ser debido a:
# •	Errores de Sintaxis (SyntaxError) → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.

# Ejemplo: escribir far en vez de for.

# •	Excepciones (Exeption) → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro del código o fuera de el (elevar una excepción)

# Cuando Python detecta este error, va decirnos en cual línea esta el error y ejecutara todas las líneas de código anteriores. Es nnecesario consultar cuales son las excepciones y a que se deben, además de las ya mencionadas KeyboardInterrupt, KeyError, IndexError, FileNotFoundError, ZeroDivisionError, ImportError

# El KeyboardInterrupt sucede cuando cortamos el proceso interactivo de Python y todo se cierra, ahí Python para poder interrumpir el programa, crea un objeto tipo error y lo va moviendo en nuestro programa en los bloques de código desde adentro hacia afuera

# Otro tipo de error es el KeyError, por ejemplo cuando intentamos a acceder a una llave que no existe dentro de un diccionario.

# Otro error que es el IndexError, es cuando estamos trabajando con listas y queremos acceder a un elemento que no existe

# FileNotFoundError cuando tratamos de encontrar un archivo que no existe dentro de Python, nos arroja este error

# ZeroDivisionError, es un error clásico que nos indica que intentamos dividir un numero entre 0

# ImportError, cuando importamos un modulo y hay un error en ese modulo y falla.

# El mensaje que nos arrojan los errores se llama Traceback


# Tenemos este ejemplo

# Traceback (most recent call last):
#         File “<stdin>”, line 1, in <module>
# ZeroDivisionError: división by zero


# Lectura de un traceback
# •	La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error. 
# •	En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
# En este caso es ZeroDivisionError
# •	La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
# En este caso nos dice el archivo en el que sucedió el error. Este ejemplo fue hecho en consola interactiva, por eso aparece <stdin>, luego que sucedió en la línea 1 y finalmente el modulo en el que sucedió.
# •	La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)
# Elevar una excepción
# •	Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback

