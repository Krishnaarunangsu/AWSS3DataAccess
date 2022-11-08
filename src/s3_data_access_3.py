import boto3
import pandas as pd
import csv
from smart_open import smart_open # utils for large files
import s3fs
import os
import io

aws_key = ''
aws_secret = ''

bucket_name = 'arunbucketsage'
object_key = 'Person_details.csv'

key = 'AKIAUFRW6ZOVLSFQENWC'
secret = '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'
region = 'ap-south-1'


s3 = boto3.client(
    's3',
    aws_access_key_id=key,
    aws_secret_access_key=secret,
    region_name=region
) #1

# s3 = boto3.client(
#     's3',
#     aws_access_key_id='AKIAUFRW6ZOVLSFQENWC',
#     aws_secret_access_key='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',
#     region_name='ap-south-1'
# ) #1

# obj = s3.get_object(Bucket='arunbucketsage', Key='Person_details.csv') #2
obj = s3.get_object(Bucket='arunbucketsage', Key='Person_details.csv')
df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='utf-8')
print(df)
# Setup credentials
# os.environ['AWS_ACCESS_KEY_ID'] = key
# os.environ['AWS_SECRET_ACCESS_KEY'] = secret
# os.environ['AWS_DEFAULT_REGION'] = region
#
#
# # File parameters
# # s3_file = 's3://bucket-name/path/to/file/titanic.csv'
# s3_file = 's3://bucket-name/object_key'
#
# # Import example file
# df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# print(df.head())
# ##### Write file #####

# df.to_csv(s3_file)

##### Read file #####
# df_s3 = pd.read_csv(s3_file)
