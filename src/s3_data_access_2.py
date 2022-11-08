import boto3
import pandas as pd
import csv
from smart_open import smart_open # utils for large files

aws_key = 'AKIAUFRW6ZOVLSFQENWC'
aws_secret = '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'

bucket_name = 'arunbucketsage'
object_key = 'Person_details.csv'

path = 's3://{}:{}@{}/{}'.format(aws_key, aws_secret, bucket_name, object_key)

# df = pd.read_csv(smart_open(path))
df = pd.read_csv('https://s3-ap-south-1.amazonaws.com/arunbucketsage/Person_details.csv')
print(df)
