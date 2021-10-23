# Los archivos de lectura y escritura, son muy importantes.
 

# Los archivos de texto, que son los que están en gris. Los archivos binarios, que son los que están en verde.

# Los de texto solo representan textos, letras, numeros, símbolos. Los binarios tienen bytes que son infinitamente mas complejos, como datos de imágenes o videos.
# Comentario útil:
# Modos de Apertura
# •	r -> Solo lectura
# •	r+ -> Lectura y escritura
# •	w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# •	w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# •	a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# •	a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.



with open("./ruta/del/archivo.txt", "r") as f:

# ⭐ Si no escriben el modo de apertura, Python lo toma por Default como si fuera rt
# .
# Read and Text.
# .
# Además, f es el nombre por convención, entonces pues ese ponemos.

# Como escribir un archivo sin sobrescribir

# Con esto ya podemos manejar archivos, aclarando que solo necesitamos lectura.

# Fijémonos además, que tenemos una nueva palabra clave with que en Python es un manejador contextual. Esta palabra clave lo que hace es controlar el flujo de nuestro archivo, haciendo que si nosotros cerramos el programa o el script finaliza inesperadamente, el archivo no se rompa. Luego tenemos la funcion open que lo que hace es abrir un archivo que lleva varios parámetros, pero por el momento solo dos, el primero es la ruta donde esta ese archivo y un segundo, que es el modo de apertura, que para este caso solo es read. Cerramos los paréntesis y nos encontramos con el as, que sirve para asignarle nombre, que será f por convención. 
