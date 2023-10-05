# Checking if an object exists on S3 using the AWS SDK for pandas

import boto3
import pandas as pd

s3_resource=boto3.resource('s3')
bucket_name=''
object_key=''

try:
    exists=pd.read_csv('s3://'+bucket_name+'/'+object_key,nrows=0).shape[1] > 0
    print(exists)
except:
    pass    