Crearemos una carpeta para nuestro proyecto ejemplo, que en este caso será la carpeta que ya teníamos creada en nuestro CursoPythonIntermedio.

# Ahora crearemos el entorno virtual dentro de esta carpeta, en el cual van a vivir todos nuestros modulos.

# 1.	Vamos a la consola con python3  -m  el -m nos indica que vamos a cambiar el comportamiento original por otra cosa, significa específicamente modulo, vamos a llamar al modulo venv es decir virtual enviroment. Y finalmente a este comando le falta el nombre que le vamos a poner, que será, por convención, es también venv, o env.
# Python3 -m venv venv
# 2.	Luego de esto podríamos actualizar y modificar los modulos que viven en este entorno virtual sin alterar el Python que vive en nuestro PC originalmente.
# 3.	Ademas tenemos que activar a ese Python interno. Eso en Linux lo hacemos con el comando source venv/bin/actívate porque en Linux la carpeta scripts no va existir, va tener el nombre de bin.


# Una vez que nos aparezca el venv antes de la dirección en donde estamos, es que estamos en el entorno virtual

 

# Para desactivar el entorno virtual basta con el comando deactivate y veremos que ya no estamos en el entorno virtual

# Aquí ya, con el venv, estamos utilizando un Python clonado que solo funciona en nuestro proyecto. Además, para no tener que estar escribiendo siempre la activación del entorno virtual, tenemos que crear un alias, que será un acortamiento de ese comando

# Para crear el alias en Linux, lo hacemos con alias nombre-alias=”comando”. Es decir alias avenv=”source venv/bin/actívate”

# Con esto, cada vez que escribamos avenv, se activara nuestro entorno virtual.


# Creando un ambiente virtual con VENV
# Creación de ambiente Virtual:
# python3 -m venv nombre_venv
# •	Usualmente el nombre del ambiente virtual es venv.
# Activación del ambiente virtual:
# •	Windows:
# .\venv\Scripts\activate
# •	Unix o MacOS:
# source venv/bin/activate
# Desactivar el ambiente virtual:
# deactivate
# Crear un alias en linux/mac:
# alias nombre-alias="comando"

# Aquí les dejo los pasos para crear un alias permanente en Linux Ubuntu:
# .
# Para hacerlo en este sistema operativo, necesitamos que cada que la terminal cargue, el alias sea leído, para ello, la terminal tiene un archivo llamado .bashrc que contiene la configuración inicial, y usualmente se encuentra en nuestro home, por lo que hacemos lo siguiente:
# .
# 1.	Ejecutar sudo nano ~/.bashrc
# 2.	Ir al final del archivo
# 3.	Agregar el comando: alias avenv='source venv/bin/activate'
# 4.	Guardar presionando ctrl + o y luego salir con ctrl + x
# 5.	Reejecutar la configuración de la terminal: source ~/.bashrc
# 6.	Activar el entorno vitual avenv
# .
# De esa forma persistirá siempre, ya que el alias se guarda dentro del archivo de configuración de la terminal 
