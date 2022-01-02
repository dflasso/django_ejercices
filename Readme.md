# Python

## Instalar python


## Crear un entorno virtual
``` sudo apt-get install python3.9-venv ```

``` cd <path_folder_project> ```

``` python3.9  -m venv .env ```

### Activar entorno virutal

En un entorno virtual se instala todas las librerias, permite manejar varios proyectos con versiones de librerias diferentes

``` cd <path_folder_project> ```

``` source .env/bin/activate ```

Si funciona el terminal debe tener comenzar con:
``` (.env) ```
### Ver Librerias del entorno virutal

``` pip freeze ```

### Desactivar entorno virutal
``` deactivate ```

## Django
### Instalación
#### Linux

``` pip install django -U ```

### Creación de un proyecto

``` django-admin startproject <nombre_proyecto> <path_ubicacion_proyecto> ```
#### Estructura de archivos

1. <folder_nombre_proyecto>
    1. **__init__.py**: declara el proyecto como un módulo de python
    2. **settings.py**: contiene todas las configuraciones del proyecto
        - [BASE_DIR = Path(__file__).resolve().parent.parent] : lugar donde correo el proyecto
        - SECRET_KEY: hash para las contraseñas y conexiones a las bases de datos
        - DUBUG: agrega información util solo en desarrollo
        - ALLOWED_HOSTS: servidores permitidos a interacturar con la app
        - DATABASES: Base de datos, por default trabaja con sqlite3
        - AUTH_PASSWORD_VALIDATORS: si se utiliza el módulo de autenticación utiliza esos filtros de contraseñas
    3. **urls.py**: declara endpoitns del proyecto
    4. **wsgi.py**: archivo usado durante el deployment
2. **manage.py**: interfaz sobre django-admin


#### Vistas

1. Agregar endpoint en el archivo **urls.py**
``` 
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('plain_text/', views.plain_text),
    path('json/', views.json),
]
 ```
2. Crear respuesta en texto plano:

```
from django.http import HttpResponse
from datetime import datetime

def plain_text():
    return HttpResponse('Oh, hi! Current serer time is {now}'.format(
		now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	))
```

3. Crear respuesta en texto json:
```

from django.http import JsonResponse

def json(request):
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})
```
Otra opcion

```

from django.http import HttpResponse
import json

def json2(request):
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    data = { "numbers" : sorted(numbers)}
    return HttpResponse( json.dumps(data ) , content_type='application/json' )
```