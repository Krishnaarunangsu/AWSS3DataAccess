import boto3

s3_resource = boto3.resource('s3')

try:
    s3_resource.create_bucket(BucketName='myTestBucket')

except s3_resource.meta.client.exceptions.BucketAlreadyExists as err:
    x=err.response["Error"]["BucketName"]
    print(f'Bucket {x} already exists!')
    raise err