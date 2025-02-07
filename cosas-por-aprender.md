Cosas por aprender

* Python
* Django
    * django rest framework
    * django test
    * sessiones
    * forms
    * models
    * templates
    * views
* testing con selenium
* Git
    * checkout
    * push
    * pull
    * branch
    * commit 
    * add
* github
    * pull request
    * reviews
* mariadb
* Docker
    * dockerfile
    * dockerignore
    * build
    * run
* docker-compose
    * up
    * down
    * build
    * run
    * exec
    * logs
* makefile





API de Django para obtener Tipo de Cambio MXN/USD

Objetivo: El objetivo de esta prueba es evaluar tus habilidades para construir una API RESTful utilizando Django. Se espera que desarrolles una API que obtenga el tipo de cambio MXN/USD desde una fuente externa oficial como el Diario Oficial de la Federación (DOF) o el Banco de México (Banxico). Además, la API debe contar con un sistema de autenticación y pruebas automatizadas para validar su funcionalidad.

Requisitos:
1. Configuración del Proyecto

    #Crea un proyecto en Django y configura una aplicación que gestione la API.
    #Configura una base de datos (puede ser SQLite para simplicidad).

2. Autenticación

    #Implementa un sistema de autenticación.
    #Los usuarios deberán autenticarse para poder acceder al endpoint del tipo de cambio.

3. Endpoint para Obtener el Tipo de Cambio

    #Crea un endpoint que permita obtener el tipo de cambio MXN/USD desde el DOF y Banxico.
    #Puedes hacer uso de la API pública de Banxico o realizar web scraping si la fuente no ofrece una API directa.
    #El endpoint debería devolver el tipo de cambio más reciente en formato JSON. Ejemplo de respuesta:

    json

    {
        "date": "2024-09-01",
        "exchange_rate": 17.50
    }

4. Pruebas Automatizadas

    #Implementa pruebas automatizadas para validar el funcionamiento de la API.

5. Documentación

    Crea un README.md.

6. Cache

    Cachear la respuesta del tipo de cambio para evitar múltiples consultas a la fuente externa en un corto periodo de tiempo.
    Implementar paginación en el caso de que la API devuelva un histórico de tipos de cambio (en lugar de solo el más reciente).
    Desplegar la API en una plataforma como Heroku o Railway (incluir instrucciones de despliegue si lo haces).
