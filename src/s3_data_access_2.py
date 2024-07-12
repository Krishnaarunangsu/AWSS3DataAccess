import pandas as pd
# import csv
from smart_open import smart_open # utils for large files

AWS_KEY = 'AKIAUFRW6ZOVLSFQENWC' # AWS_ACCESS_KEY_ID
AWS_SECRET = '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' # AWS_SECRET_ACCESS_KEY

BUCKET_NAME = 'arunbucketsage'
OBJECT_KEY = 'Person_details.csv'

# path = 's3://{}:{}@{}/{}'.format(AWS_KEY, AWS_SECRET, BUCKET_NAME, OBJECT_KEY)

path=f's3://{AWS_KEY}:{AWS_SECRET}@{BUCKET_NAME}/{OBJECT_KEY}'
df = pd.read_csv(smart_open(path))
# df = pd.read_csv('https://s3-ap-south-1.amazonaws.com/arunbucketsage/Person_details.csv')
print(df)
