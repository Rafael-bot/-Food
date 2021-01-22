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

# INTERFASES WEB DESPLEGAR PROYECTO WEB +FOOD


### Flujo de Trabajo en Git 

El flujo de trabajo sera desplegado a travez de un repositorio en Git, por lo tanto para poder desplegarlo debera seguir las siguientes indicaciones:
### Desplegar proyecto con Git:


### Lo primero será clonar el repositorio:
>>```git clone https://github.com/Rafael-bot/-Food.git```



### Aqui ya podremos acceder a los archivos del repositorio:
>>```cd -Food/```

# Por defecto tendremos como current branch a la rama main:


### Para tener acceso a las demás ramas remotas tendremos que hacer lo siguiente:
>>```git fetch --all``` 

>>```git pull --all```



### Tras esto ya podremos acceder a la rama que queramos con:

>>```git checkout branchName```


# Tras realizar esta acción podremos abrir nuestro IDE (en nuestro caso desplegaremos nuestro proyecto en VSCode)

### En una terminal de vs code aplicaremos la siguiente configuración:

>>```cd .\Project\```

### Luego nos dirigiremos a la raíz del proyecto:

>>```cd .\moreFood\``` 

### Una vez en la raíz del proyecto ejecutaremos el siguiente comando para desplegarlo
>>```python manage.py runserver```
 
### Nos dirigimos al puerto por defecto en el que se encuentra el proyecto
>>```http://127.0.0.1:8000/```

# Acciones básicas:


## Añadir cambios
>>```git add .```  

>>### Añade todos los cambios
>>```git add FileName.py``` 
>>### Añade cambios de un fichero

### Mensaje Descriptivo de los cambios añadidos
>>```git commit -m "message descriptivo"``` 

### Subir cambios al remoto
>>```git push origin branchName```

 >> ### ```branchName```  
 
 nombre de la rama remota a la que subir los cambios
