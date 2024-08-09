
# Proyecto Django - Prueba Técnica

Este proyecto es una prueba técnica que utiliza Django. A continuación, se detallan los pasos necesarios para levantar el servicio. 

## Requisitos

- Python 3.10
- Django
- Pillow

## Instalación

1. Ejecutar los siguientes comandos

   ```bash
   git clone https://github.com/DryMemoG/examentecnico-MINFIN.git
   cd examentecnico-MINFIN/pruebatecnica
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

2. Acceder a través de [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

