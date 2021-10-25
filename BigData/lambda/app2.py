from datetime import datetime
import requests 
import json
import boto3
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def handler(event, context):

	s3 = boto3.client('s3')

	url = 'https://www.eltiempo.com/'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	noticias = [list(),list(),list()]

	for a in soup.find_all('a',class_='title page-link', href=True, text=True):
		seccion = ""
		slashEncontrado = 0
		# Ciclo para extraer la sección del href
		for char in a['href']:
			if char == '/':
				slashEncontrado = slashEncontrado+1
			if slashEncontrado == 1:
				seccion = seccion+char
		etiqueta = a.text
		title = etiqueta.replace(',',"")
		noticias[0].append(title)
		noticias[1].append(seccion[1:])
		noticias[2].append(url+a['href'])

	# The scraped info will be written to a CSV here.
	#with open("noticias.csv", "a") as fopen:  # Open the csv file.
	#    csv_writer = csv.writer(fopen)
	#    csv_writer.writerow(["Titulo", "Seccion", "Enlace"])
	#	csv_writer.writerow(noticias[0])
	print(noticias)
	df = pd.DataFrame(noticias).transpose()
	#pd.to_csv("noticias.csv")


	year = datetime.today().strftime('%Y')
	month = datetime.today().strftime('%m')
	day = datetime.today().strftime('%d')
	directory_name = 'year='+year+'/month='+month+'/day='+day 
	df.to_csv('s3://news043final/'+directory_name+'/'+'Analisis_El_tiempo.csv', index=False)



	return {
        	'statusCode': 200,
        	'body': json.dumps('Hello from Lambda!')
    	}