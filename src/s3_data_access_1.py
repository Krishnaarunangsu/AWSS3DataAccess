import io

import boto3
import pandas as pd
import csv

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAUFRW6ZOVLSFQENWC',
    aws_secret_access_key='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',
    region_name='ap-south-1'
) #1

obj = s3.get_object(Bucket='arunbucketsage', Key='Person_details.csv') #2
data = obj['Body'].read().decode('utf-8').splitlines() #3
records = csv.reader(data) #4
headers = next(records) #5
print('headers: %s' % (headers))
for eachRecord in records: #6
     print(eachRecord)