import wget
from datetime import datetime
import json
import boto3
import wget
import os
import pandas as pd


def handler(event, context):

	s3 = boto3.client('s3')


	empresas=[('Avianca','https://query1.finance.yahoo.com/v7/finance/download/AVHOQ?period1=1603577453&period2=1635113453&interval=1d&events=history&includeAdjustedClose=true'),
		('Ecopetrol','https://query1.finance.yahoo.com/v7/finance/download/EC?period1=1603577394&period2=1635113394&interval=1d&events=history&includeAdjustedClose=true'),
		('Aval','https://query1.finance.yahoo.com/v7/finance/download/AVAL?period1=1603573317&period2=1635109317&interval=1d&events=history&includeAdjustedClose=true'),
		('Cementos_Argos','https://query1.finance.yahoo.com/v7/finance/download/CMTOY?period1=1603577562&period2=1635113562&interval=1d&events=history&includeAdjustedClose=true')]

	year = datetime.today().strftime('%Y')
	month = datetime.today().strftime('%m')
	day = datetime.today().strftime('%d')

	directory_name = 'year='+year+'/month='+month+'/day='+day 

	for (nombre,url) in empresas:	
		
		df = pd.read_csv(url)
		df.to_csv('s3://yahooactions/'+'stocks/company='+nombre+'/'+directory_name+'/'+nombre+'.csv', index=False)


		#s3.put_object(Body=info_actions, Bucket='yahooactions', Key=('stocks/company='+nombre+'/'+directory_name+'/'+nombre+'.csv'))





	print("hello from zappa")
	return {
        	'statusCode': 200,
        	'body': json.dumps('Hello from Lambda!')
    	}




