# Parcial Scrapping Web
# Por: Jofre Eduardo Oliveros y Juan Pablo Blanco
# Universidad Sergio Arboleda

El presente proyecto tiene como objetivo desarrollar funciones en python que por medio de herramientas como aws y zappa, permitan extraer información precisa de sitios web para posteriormente escribir los resultados en distintos servicios de Amazon Web Services como lo son Athena y S3.

### Pre-requisitos 📋

Los pre-requisitos para desplegar el proyecto se podrán visualizar en el archivo [requeriments.txt](https://github.com/juanpa54/Parcial2BigData/blob/d7520e58c6fe7b0f53f9715a47f8baf31f31131a/requirements.txt), allí encontrará las bibliotecas necesarias.

### 1. Función aws Lambda que realiza scrapping en Yahoo Finances 💰💲

La función que se encarga de realizar el scrapping en Yahoo Finnances es [app3.py](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/BigData/lambda/app3.py), si se desea ejecutar se deberá modificar en el código el nombre del bucket en el que se guardarán los datos. Esta función descargará tres archivos csv con las acciones de Avianca, Ecopetrol, Grupo Aval y Cementos Argos.

En S3 quedará la información en la forma "s3://**nombreDeTuBucket**/stocks/company=xxx/year=xxx/month=xxx/day=xxx".

Posteriormente con la información en S3 se realizó la respectiva tabla en Athena.
![Tabla Yahoo Finances](https://github.com/juanpa54/Parcial2BigData/blob/7521044c1a6e2b584d452ba03b14ac8ee88c204c/tabla1.png)

Además se crearon las respectivas particiones por empresa, año, mes y día como se observa en la imagen.
![Ver Particiones](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/caracteristicasTabla1.jpg)

Para la actualización de las particiones se creó el lambda [lambdaYahoo](https://github.com/juanpa54/Parcial2BigData/blob/569bf4864316b58b3b14e5996c24594f63e80d7f/BigData/lambda/particionesYahoo.txt) con un disparador al bucket que contiene la información del scrapping.

### 2. Función aws Lambda que realiza scraping a eltiempo.com 📰

La función que se encarga de descargar la información de la página El Tiempo es [app.py](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/BigData/lambda/app.py), por otra parte se tiene el lambda [app2.py](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/BigData/lambda/app2.py), el cual se encargará de realizar scrapping para extraer el titulo, sección y enlace de cada noticia y escribirlo en un bucket de aws de la forma "s3://**nombreDeTuBucket**/headlines/raw//year=xxx/month=xxx/day=xxx" en formato csv.

Posteriormente con la información en S3 se realizó la respectiva tabla en Athena.
![Tabla Noticias](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/tabla2.jpg)

Además se crearon las respectivas particiones por año, mes y día

![Ver Particiones](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/caracteristicasTabla2.jpg)


### Instalación 🔧

Para desplegar el proyecto en tu ordenador deberás crear un entorno de programación python con el siguiente comando. (comandos suponiendo un S.O Windows)

```
py -m venv nombreDelEntorno
```

Posteriormente se deberá activar el entorno creado.

```
nombreDelEntorno\Scripts\activate
```

Después se deberán instalar las librerias de los prerequisitos con el comando:

```
pip install nombreLibreria==version
```

Luego en tu carpeta **.aws** deberás actualizar las credenciales de tu cuenta de Amazon Web Services. El paso a seguir será instalar los archivos de la carpeta [lambda](https://github.com/juanpa54/Parcial2BigData/tree/main/BigData/lambda) que encontrarás en este repositorio.

Ten en cuenta que deberás actualizar los nombres de tu bucket en S3 para cada función. Para lanzar un lambda deberás ingresar el siguiente comando

```
zappa deploy nombreDev
```

Si deseas lanzar la función de recoger datos de la página El Tiempo y escribirlos en S3 será dev2.
Si deseas lanzar la función de extraer titulares, secciones y url de la página El Tiempo y escribirlos en S3 en formato csv será dev.
Si deseas lanzar la función de recoger datos de acciones de empresas en Yahoo Finances y escribirlos en S3 será dev3.

### ...Esperamos que disfrutes el proyecto, cualquier comentario escribir a [juan.blanco01@correo.usa.edu.co] o a [jofre.oliveros01@correo.usa.edu.co] 😊

