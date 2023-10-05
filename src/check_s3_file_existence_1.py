import boto3

__author__ = "Jagannath"

s3_client=boto3.client('s3')

bucket_name='arunbucketsage'
file_name='Person_details.csv'

# check if the file exists in the bucket
try:
    file_content=s3_client.head_object(Bucket=bucket_name, Key=file_name)
    print(f'File Exists:{file_name}')
    print('****************************************')
    print(f'File Content:\n{file_content}')    
except FileNotFoundError as fe:
    print('File Not Found:{fe.message}')    

