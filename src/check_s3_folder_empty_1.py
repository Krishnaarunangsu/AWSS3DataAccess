# Using Boto3 to check if a folder is empty in an S3 bucket

import boto3

s3_resource=boto3.resource('s3')
bucket_name=''
folder_name=''

try:
    bucket=s3_resource.Bucket(bucket_name)
    objects=bucket.meta.client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    if 'Contents' in objects:
        print('Folder is not empty')
    else:
        print('Folder is empty')
except:
    print('Bucket does not exist')   