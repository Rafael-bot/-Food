# +Food
### REQUISITOS
- Nombre: +Food.
- Descripción: Compartir Recetas.
- Idiomas: Español.
- Tecnologías:
    - HTML
    - CSS / BOOTSTRAP
    - JS
    - Django 
    - Diseño:
    - Color:![](https://i.imgur.com/TA2yvwy.png)
    - Secciones:
        - Home: Página principal. Va a tener una pequeña descripción. Portada llamativa.
        - Recetas: Va a tener recetas, cuando se clica a una receta se va abrir una pestaña nueva.
        - Recetas individual.
        - Login y Register. Opcional
        - Comentarios en la Receta: Se va a situar en cada receta.
        - Contactos: Formulario para contactarnos. 
        - Footer: Copyright, información de contacto.
- Roles:
    - Vladi: Diseño / Ayudante
    - Berny: Websocket.io / Node.Js / Ayudante
    - Rafael: Js / Organizar Grupo y Tablero / Ayudante

       
 ## Flujo de Trabajo en Git 

El flujo de trabajo que seguiremos será el representado a continuación:


Orden a seguir, por cada Sprint / Tarea:

1. Nueva rama sprint-n, donde n es el número de la tarea, desde develop

2. Crear rama personal de trabajo con el siguiente esquema:

   ​	SP-n (númeroDelSprint) / espejunjo (nombreUsuarioGithub - autor)

3. Realizar trabajo en su respectiva carpeta

4. Pull Request de rama individual a rama del sprint.

5. Revisión de trabajo individual

6. Testing de trabajo

7. Finalmente, Pull request de entrega de rama del sprint a develop.



## Trabajar con Git

Lo primero será clonar el repositorio:

```bash
git clone https://github.com/Rafael-bot/Grupo6-EntornoServidor.git
```



Aqui ya podremos acceder a los archivos del repositorio:

```bash
cd entorno-servidor/
```



Por defecto tendremos como current branch a la rama master:

![master](./docs/Defecto.png)



Para tener acceso a las demás ramas remotas tendremos que hacer lo siguiente:

```bash
git fetch --all

git pull --all
```



Tras esto ya podremos acceder a la rama que queramos con:

```bash
git checkout branchName
```



Acciones que necesitarás saber como se hacen:

- Acciones básicas:

```bash
# Añadir cambios
git add . # Añade todos los cambios
git add FileName.py # Añade cambios de un fichero

# Mensaje Descriptivo de los cambios añadidos
git commit -m "message descriptivo" 

# Subir cambios al remoto
git push origin branchName # branchName --> 
						   # nombre de la rama remota a la que subir los cambios

###################################OTHERS########################################

# Crear una rama nueva de trabajo
git branch -m newBranchName # -m hará que a parte de crear la rama te hago un checkout 								# automático a la misma

# Para traerte los cambios de una rama remota
git pull origin branchName

# Estacionar cambios
git stash

# Devolver cambios estacionados 
git stash pop

# Mergear rama especifica a la rama en la que estás situado (!!Cuidado con esto debido a los conflictos que puede dar como resultado)
git merge branchName
```



- Hacer un Pull Request de tu rama de trabajo

1. Ir al apartado Pull Request del repositorio de github y verás un botón verde "New pull request":



2. Este botón te redigirá a una vista como la siguiente, en la que tendrás que elegir la rama base (a la que quieres aplicar los cambios) y la rama compare (tu rama de trabajo):

 
## Instalación

 1. Deberas tener instalado [python ](https://www.python.org/downloads/). Tendras que instalar la ultima versión.
 2. Instalar [pip](https://docs.python.org/es/3.8/library/venv.html) en tu entorno virtual del sistema.
 3. Tienes que crear un [virtualenv](https://docs.python.org/es/3.8/library/venv.html) en tu projecto.
 4. Te vas a la terminal, y te situas dentro de la carpeta /Project/ donde has clonado el repositorio.
 5. Introduces el siguiente comando: ````pip install -r requirements````
 6. Te vas a la terminal, y te situas dentro de la carpeta /Project/moreFood/ donde esta el project Django.
 7. Para arrancar el servidor tienes que introducir el siguiente comando: ````py manage.py runserver````
