
# Vamos a poner en practica el manejo de archivos con un pequeño proyecto.
# 1.	Funcion principal run() y entry point
# 2.	Antes de run() vamos a crear dos funciones, read() y write().
# 3.	En la funcion read:
# a.	leer un archivo que va tener los numeros del uno al 10
# b.	Va convertir las líneas de ese texto en una lista, para trabajarla posteriormente
# c.	Para ello creamos una nueva carpeta llamada files_project.
# d.	Alli crearemos un archivo llamado numbers.txt con varios numeros aleatorios en lineas
# 4.	Vamos a ir de nuevo a nuestro archivo .py y en la funcion run() ejecutaremos la funcion read()
# 5.	En read() vamos a crear una lista llamada numbers que va contener los numeros de nuestro archivo.
# numbers = [ ]
# modo de apertura
# with open("./files_project/numbers.txt", "r") as f

# 6.	Pero vamos a agregar un parámetro adicional, que se ve en muy pocos lugares que es el atributo encoding=”utf—8”, este nos sirve para tener caracteres especiales como la ñ, 
# 7.	Damos dos puntos y empezaremos a trabajar dentro de este bloque de código del modo de apertura.
# 8.	Haremos un ciclo for para recorrer todas las líneas del archivo, asi: for line in f:
# a.	Adentro agregaremos agregar a nuestra lista de numeros, con el método append a esa línea: numbers.append(int(line)) pero convirtiéndolo a un int, porque sin el int, no deja de ser str 
# b.	Luego voy a cerrar el  bloque de código de modo de apertura e imprimo numbers


# Y si ejecutamos en consola el archivo files_project.py nos daremos cuenta que tenemos una lista con todos esos numeros.
 

# Ahora vamos a ir a nuestra funcion write y crearemos una lista
# 1.	lista llamada names = [“Felipe”, “Facundo”, “Fulanito”, “Peranito”] que contenga 4 nombres aleatorios. Lo que haremos es crear un archivo, que contenga en cada línea, a cada uno de estos nombres, que seria lo inverso a lo que hicimos con la funcion read. 
# 2.	Para ello haremos otra vez el modo de apertura. Notaremos que lo dirigiremos a otro archivo, que para este caso será strings.txt, despues simplemente le otorgaremos el modo, que será write “w” y al final, el econding=”utf-8”), as f:
# a.	dentro del bloque de código ejecutaremos otra vez un ciclo for, pero ahora recorreremos cada uno de los elementos de nuestra lista names =
# b.	y utilizaremos un método nuevo, llamado f.write(name), que llevaría al comienzo el nombre asignado y que llevara como parámetro los nombres y además, un salto de línea f.write(“\n“), para que este cada nombre en una linea distinta
# 3.	una vez terminado, en la funcon run vamos a ejecutar es write() y luego lo ejecutaremos en la consola. Veremos que no pasa nada, pero si vamos al archivo strings.txt, veremos como ha aparecido la lista ahí.
# Si hacemos cambios en la lista y volvemos a guardar, ejecutar en consola, nos daremos cuenta que el archivo se sobreescribe.
# Si quisiéramos solo agregar, tendríamos que utilizar el modo append que es “a”, en vez de “w” que solo sobreescribe.



def read():
    numbers = []
    with open("./files_project.txt/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    # names = ["Facundo", "Miguel", "Pepe", "Christian"] fueron los primeros nombres antes de hacer el append de los siguientes.
    names = ["Fausto", "Michael", "Pipe", "Cristina"]
    with open("./files_project.txt/strings.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()

