from datetime import datetime
import requests 
import json
import boto3


def handler(event, context):

	r= requests.get('https://www.eltiempo.com/')
	r.status_code
	r.headers['content-type']
	r.encoding
	s3 = boto3.client('s3')
	txt_data = r.text
	bucket = 'arn:aws:s3:::news043'
	print ('Inicio evento !!!!! \n\n') 
	print('Ejemplo evento')
	print ('\n\nFin evento !!!!! \n') 
	year = datetime.today().strftime('%Y')
	month = datetime.today().strftime('%m')
	day = datetime.today().strftime('%d')
	directory_name = 'year='+year+'/month='+month+'/day='+day 
	s3.put_object(Body=txt_data, Bucket='news043', Key=(directory_name+'/'+'El_tiempo.txt'))
	#object = s3.Object('news043','El_tiempo.txt')
	#result = object.put(Body=txt_data)
	#bucket.key ('abc / 123 /')

	print('Ejemploooooooo')
	print("hello from zappa")
	return {
        	'statusCode': 200,
        	'body': json.dumps('Hello from Lambda!')
    	}
