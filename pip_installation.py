# Dentro de Python hay un montón de código que se puede aprovechar, de otras personas. Pero ya hay unos modulos que ya vienen instalados.

# Los que no vienen de fabrica, que vienen de manera externa, se pueden instalar con un manejador de dependencias o instalador externo llamado Package Installer for Python (PIP)

# Algunos ejemplos de modulos de ese estilo son por ejemplo Requests, BeautifulSoup4, que son modulos famosos para hacer una tarea como el web scraping, para saber que es el web scraping, podríamos ver el curso de fundamentos de web scraping con Python y expa. Otros como, Pandas, Numpy, que se utilizan en Data Sciencie. O Pytest, que nos sirve para realizar tekking.

# Básicamente, pip es como el npm de JavaScript, y el archivo requeriments.txt es como el package.json de JavaScript.

# Es importante recordar que esto se debe correr con el entorno virtual activado (avenv), de esta manera todas las dependencias que instalemos se guardaran para este entorno virtual (de lo contrario se guardarían de manera global, que es justo lo que no queremos).

# Algo importante, si estás manejando git, es bueno siempre ignorar la carpeta venv, esto porque realmente no nos importa subir todo eso al repositorio, puedes mirarlo como que venv es el node_modules de JavaScript, a fin de cuentas, cualquier otro programador que trabaje con nuestro código creará su propio entorno virtual e instalará las dependencias que dejamos en nuestro requeriments.txt.

# Y un dato curioso es que, el operador > en la terminal es algo especial de UNIX, ya que este operador lo que hace es redirigir la salida de cualquier comando hacia donde lo mandes, por defecto la salida es en la terminal, pero al usar > le dijimos a la terminal que, en lugar de que la salida sea en la terminal, que se redirija al archivo requeriments.txt 👀. Si quieren jugar con ello, pueden hacerlo con este ejemplo: ls -al > test.txt, eso creará un archivo llamado test.txt, y si lo abren verán cómo es que ese comando funciona 😄


# Para utilizar pep, lo hacemos asi:

# 1.	Vamos a poner nuestro avenv en la consola, para que lo que instalemos no se quede mas que en nuestro proyecto temporal.
# 2.	Vamos a utilizar el comando pip freeze, que nos mostrara los packages que tenemos instalados.
# 3.	Vamos a instalar pandas, que es uno de los packages, esto lo hacemos con pip install pandas. Adicionalmente notaremos que tendremos instalados otros modulos con la instalación de pandas, esto es porque pandas es un modulo complejo que utiliza otros modulos.
#  Si queremos compartir nuestro proyecto con nuestro compañero al otro lado del mundo, nos servirá el comando pip freeze > requirements.txt

# Esto crea el archivo requeriments.txt, que si vemos que es lo que contiene, esto es, las dependencias, exactamente las mismas que nos da pip freeze. Asi por ejemplo si subimos nuestro proyecto a github y nuestro compañero quiere trabajar con el, al clonarlo, solo tiene que escribir el comando

# pip install -r requirements.txt


# Módulos populares
# Si bien pip puede instalar paquetes de Python, Pipenv es una herramienta de nivel superior que simplifica la administración de dependencias para casos de uso comunes.
# Instalar Pyenv:
# $ pip install --user pipenv
# Instalar dependencias:
# $ pipenv install "dependencia"
# This does a user installation to prevent breaking any system-wide packages. 
# If pipenv isn’t available in your shell after installation, 
# you’ll need to add the user base’s binary directory to your PATH.

# On Linux and macOS you can find the user base binary directory
#  by running python -m site --user-base and adding bin to the end. 
# For example, this will typically print ~/.local 
# (with ~ expanded to the absolute path to your home directory) 
# so you’ll need to add ~/.local/bin to your PATH. 
# You can set your PATH permanently by modifying ~/.profile.

# On Windows you can find the user base binary directory 
# by running py -m site --user-site and replacing site-packages with Scripts. 
# For example, this could return C:\Users\Username\AppData\Roaming\Python36\site-packages 
# so you would need to set your PATH to include 
# C:\Users\Username\AppData\Roaming\Python36\Scripts. 
# You can set your user PATH permanently in the Control Panel. 
# You may need to log out for the PATH changes to take effect.



# Si como yo, usas Linux y tuviste el error de EnvironmentError: [Errno 13]
# Y tampoco te funcionó la sugerencia de --user
# La solución es entrar al archivo pyvenv.cfg
# Hacer esta modificación: include-system-site-packages = true
# Apagas el entorno virtual, lo vuelves a encender y ya podrás descargar módulos en tu proyecto de Python

# Muchas gracias, me sirvió bastante.
# Además, para los que no saben como abrir el archivo en Ubuntu pueden hacer lo siguiente:
# .
# 1.	Ejecutan el comando cd venv
# 2.	Ejecutan el comando ls -a para ver los archivos ocultos.
# 3.	Ejecutan el comando code pyvenv.cfg , con esto se les abrirá el editor de texto y podrán editar el archivo.
# 4.	Guardan.
# 5.	Apagan el entorno virtual con el keyword deactivate
# 6.	Inician el entorno virtual con el keyword avenv
# .
# Y listo, podrán seguir con el curso.


# pip
# •	Es un manejador de dependencias, es decir un paquete que nos permite instalar otros paquetes dentro de nuestro entorno virtual (o de manera global si prefieres)
# •	Para instalar un paquete usamos el comando pip install <nombre_paquete>
# •	Para conocer las dependencias instaladas en el ambiente virtual usamos el comando pip freeze
# •	Puesto que necesitamos compartir las versiones de los paquetes que estamos utilizando en el proyecto (trabajo colaborativo) guardamos las versiones de los paquetes a un archivo txt: pip freeze > <archivo.txt> (normalmente requirements)
# •	Para instalar las dependencias desde un archivo de texto usamos el modificacor -r (read): pip install -r <archivo.txt>

#  
