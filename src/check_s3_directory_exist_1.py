
# Using Boto3 to check if a directory exists in an S3 bucket
import boto3


__author__ = "Jagannath"

s3_resource=boto3.resource('s3')
bucket_name=''
directory_name=''

try:
    bucket=s3_resource.Bucket(bucket_name)
    objects=bucket.objects.filter(Prefix=directory_name)
    if len(objects) >0:
        print('Directory exists')
    else:
        print('Directory does not exixt')
except:
    print('Bucket does not exist')        
