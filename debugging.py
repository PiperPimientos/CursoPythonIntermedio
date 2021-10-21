

# El Debugging o depuración es una herramienta que traen varios editores de código como el VSC

# Si usas otro editor y no quieres tener que usar VS Code por algún motivo Python tiene un paquete preinstalado llamado pdb que se puede usar para hacer debuggin, en resumen y lo que yo uso mucho sobre todo cuando desarrollo con Flask o Django (Frameworks para desarrollo web usando Python) uso la siguiente línea de código para hacer un breakpoint en el código
# import pdb; pdb.set_trace() 
# Puedes preguntarte al ver esta linea 😱 Punto y coma en python… pues si mi amigo se pueden usar y sirven para decirle cuando termina una línea de código y sigue otra, pero en la misma línea
# Eso lo que va a hacer es que cuando llegue a esto te liberara él tu consola una terminal interactiva para poder consultar tus variables y demás; para salir de la consola debes escribir la letra c y luego un enter
# Documentacion de pdb

# Vamos a ver un ejemplo de un programa mal escrito

# 1.	Vamos a crear nuestra funcion de buenas practicas y nuestro entry point.
# 2.	Crearemos una funcion previa llamada divisors que nos retorne una lista con todos los divisores de un numero.
# a.	Le pasaremos el parámetro nums
# b.	Crearemos una lista vacia divisors
# c.	Podriamos hacerlo con un list comprehensions, pero para este caso lo haremos con un ciclo for. for i in range(1, num +1) es decir, un ciclo que vaya desde el 1 hasta ese numero, y le colocamos el +1 porque recordemos que el ultimo numero no es inclusivo en ciclos. Adentro del ciclo estableceremos la condicional que sea: que si num, modulo i, es igual a 1: entonces agrega a nuestra lista de divisores ese numero i. 
# if num % i == 1:
#     divisors.append(i)
# d.	Finalmente lo que haremos es retornar esos divisores return divisors
# 3.	En la funcion run, le pediremos un numero al usuario, para que el mismo nos pueda decir el numero del que obtendremos divisores
# Ahí mismo, haremos el print para que nos haga una lista con los divisores del numero que ingresamos
# Luego un print que nos diga que el programa termino
# 4.	Si vamos a la consola y ejecutamos el programa, nos dice que ingresemos un numero, ingresamos el 10 y nos devuelve una lista con el 3 y el 9, pero esto no esta bien, porque los divisores de 10 son 



def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        # if num % i == 1:   #ESTE ERA EL ERROR
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("Termino el programa")

if __name__ == '__main__':
    run()


# Entonces vamos a hacer el debugging.
# 1.	Revisaremos nuestro programa del inicio hasta el final. Pero en esta clase lo haremos con una técnica especial que es el debugging, En visual studio code 

 
# 2.	Presionaremos ese botón llamado run and debug
# 3.	Daremos click en esa primera opción que dice Python File
 

# 4.	Veremos que nos aparece una terminal y Python nos pide que ingresemos un numero, se ejecuta nuestro programa.

 
# De manera distintiva encontraremos un menú superior que tiene varios botones. Un botón de pausa, un botón de paso siguiente, un botón de meternos dentro, un botón de salir de un lugar, un botón de restart y un botón de detener.
 
# Si apretamos el botón de pausa, y luego en nuestro programa elegimos como numero por ejemplo, el 5, VSC nos va a subrayar una línea. Es decir que nuestro programa se ejecuto, pero va estar parado en esa línea de código, 
 
# Con el botón play, podremos seguir la ejecución a ver que pasaba. Pero le daremos al botón stepover que nos llevara a la línea siguiente.
 
# Si le damos un click mas a stepover, nos dice que termino nuestro programa.

# Ya sabemos como funciona el botón de pausa y siguiente para ver como se ejecuta el programa paso a paso. Pero vamos a ejecutar el debugger de nuevo.

# 1.	Apretamos pausa
# 2.	Ingresamos el numero 5 en nuestro programa
# 3.	Que pasa si yo quiero meterme a la funcion divisors que es donde esta el error?
# Le daremos click al botón step into
# y de inmediato Python nos llevara a la funcion divisors
# notaremos que a la izquierda hay una pestana llamada variables, que nos mostrara las variables en el código, con los valores que ya contienen. En este caso nos mostrara la variable num, con el numero 5 que es el que ingreso el usuario
 


# 4.	Vamos a dar stepover y veremos que entraremos al for. En nuestras variables se creara una lista vacia.
# Otra vez daremos stepover, entraremos al if, en las variables nos dira que i vale 1
# Otra vez daremos stepover, nos llevara al for de nuevo, es decir, la siguiente iteración. Y ahí nos daremos cuenta que hay algo mal, porque el if no entro. Ahí es donde vemos el error, porque en la condicional estamos preguntando si el num modulo i, es igual a 1, cuando lo correcto es preguntar si num modulo i, es igual a 0. Esto es porque un numero es divisor de 1, si la división exacta entre el anterior y este mismo es igual a 0.
# Entonces si 5 dividido entre 1, da como resto 0, quiere decir que hicimos las cosas bien. 
# Por lo tanto ya que lo descubrimos, vamos a parar el debugger, guardaremos nuestro programa y ejecutaremos el programa con el entero 5 y nos tendría que decir que sus divisores son 1 y 5

# Antes de finalizar la clase, veremos los breakpoints o puntos de quiebre. Esto es, si queremos parar el código en determinada línea. Para ello seleccionaremos el botón rojo que aparece a la izquierda de cada línea en VSC. Esto será un breakpoint, es decir que cuando corramos el debugger, el programa se va parar en la línea 4. Y si ejecutamos el programa, Python detecta ese breakpoint y el programa se frena en esa línea. Es una herramienta útil para hacer el proceso de depuración. 
