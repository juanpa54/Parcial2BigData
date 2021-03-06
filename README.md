# Parcial Scrapping Web
# Por: Jofre Eduardo Oliveros y Juan Pablo Blanco
# Universidad Sergio Arboleda

El presente proyecto tiene como objetivo desarrollar funciones en python que por medio de herramientas como aws y zappa, permitan extraer informaci贸n precisa de sitios web para posteriormente escribir los resultados en distintos servicios de Amazon Web Services como lo son Athena y S3.

### Pre-requisitos 馃搵

Los pre-requisitos para desplegar el proyecto se podr谩n visualizar en el archivo [requeriments.txt](https://github.com/juanpa54/Parcial2BigData/blob/d7520e58c6fe7b0f53f9715a47f8baf31f31131a/requirements.txt), all铆 encontrar谩 las bibliotecas necesarias.

### 1. Funci贸n aws Lambda que realiza scrapping en Yahoo Finances 馃挵馃挷

La funci贸n que se encarga de realizar el scrapping en Yahoo Finnances es [app3.py](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/BigData/lambda/app3.py), si se desea ejecutar se deber谩 modificar en el c贸digo el nombre del bucket en el que se guardar谩n los datos. Esta funci贸n descargar谩 tres archivos csv con las acciones de Avianca, Ecopetrol, Grupo Aval y Cementos Argos.

En S3 quedar谩 la informaci贸n en la forma "s3://**nombreDeTuBucket**/stocks/company=xxx/year=xxx/month=xxx/day=xxx".

Posteriormente con la informaci贸n en S3 se realiz贸 la respectiva tabla en Athena.
![Tabla Yahoo Finances](https://github.com/juanpa54/Parcial2BigData/blob/7521044c1a6e2b584d452ba03b14ac8ee88c204c/tabla1.png)

Adem谩s se crearon las respectivas particiones por empresa, a帽o, mes y d铆a como se observa en la imagen.
![Ver Particiones](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/caracteristicasTabla1.jpg)

Para la actualizaci贸n de las particiones se cre贸 el lambda [lambdaYahoo](https://github.com/juanpa54/Parcial2BigData/blob/569bf4864316b58b3b14e5996c24594f63e80d7f/BigData/lambda/particionesYahoo.txt) con un disparador al bucket que contiene la informaci贸n del scrapping.

### 2. Funci贸n aws Lambda que realiza scraping a eltiempo.com 馃摪

La funci贸n que se encarga de descargar la informaci贸n de la p谩gina El Tiempo es [app.py](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/BigData/lambda/app.py), por otra parte se tiene el lambda [app2.py](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/BigData/lambda/app2.py), el cual se encargar谩 de realizar scrapping para extraer el titulo, secci贸n y enlace de cada noticia y escribirlo en un bucket de aws de la forma "s3://**nombreDeTuBucket**/headlines/raw//year=xxx/month=xxx/day=xxx" en formato csv.

Posteriormente con la informaci贸n en S3 se realiz贸 la respectiva tabla en Athena.
![Tabla Noticias](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/tabla2.jpg)

Adem谩s se crearon las respectivas particiones por a帽o, mes y d铆a

![Ver Particiones](https://github.com/juanpa54/Parcial2BigData/blob/b8a33f53c608643d96b2f48789f4071d09175672/caracteristicasTabla2.jpg)


### Instalaci贸n 馃敡

Para desplegar el proyecto en tu ordenador deber谩s crear un entorno de programaci贸n python con el siguiente comando. (comandos suponiendo un S.O Windows)

```
py -m venv nombreDelEntorno
```

Posteriormente se deber谩 activar el entorno creado.

```
nombreDelEntorno\Scripts\activate
```

Despu茅s se deber谩n instalar las librerias de los prerequisitos con el comando:

```
pip install nombreLibreria==version
```

Luego en tu carpeta **.aws** deber谩s actualizar las credenciales de tu cuenta de Amazon Web Services. El paso a seguir ser谩 instalar los archivos de la carpeta [lambda](https://github.com/juanpa54/Parcial2BigData/tree/main/BigData/lambda) que encontrar谩s en este repositorio.

Ten en cuenta que deber谩s actualizar los nombres de tu bucket en S3 para cada funci贸n. Para lanzar un lambda deber谩s ingresar el siguiente comando

```
zappa deploy nombreDev
```

Si deseas lanzar la funci贸n de recoger datos de la p谩gina El Tiempo y escribirlos en S3 ser谩 dev2.
Si deseas lanzar la funci贸n de extraer titulares, secciones y url de la p谩gina El Tiempo y escribirlos en S3 en formato csv ser谩 dev.
Si deseas lanzar la funci贸n de recoger datos de acciones de empresas en Yahoo Finances y escribirlos en S3 ser谩 dev3.

### ...Esperamos que disfrutes el proyecto, cualquier comentario escribir a [juan.blanco01@correo.usa.edu.co] o a [jofre.oliveros01@correo.usa.edu.co] 馃槉

