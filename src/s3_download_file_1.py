# Downloading a file from an S3 bucket using Python and Boto3
import boto3
import botocore


s3_resource=boto3.resource('s3')
bucket_name=''
file_name=''
local_file_path=''
bucket=None

def bucket_file_download(bucket):
    """
    """
    try:
        bucket.download_file(file_name, local_file_path)
        print('File Downloaded successfully')
    except botocore.exceptions.ClientError as ce:
        if ce.response['Error']['Code']=="404":
            print('File Not Found')



try:
    bucket=s3_resource.Bucket(bucket_name)
    if bucket is not None:
        bucket_file_download(bucket)

except:
    print('Bucket does not exist')    
