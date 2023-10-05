import boto3


__author__ = "Jagannath"

s3_client = boto3.client('s3')
paginator = s3_client.get_paginator('list_objects_v2')
try:
    result_iterator = paginator.paginate(Bucket='arunbucketsage')
    for result in result_iterator:
        print('Coming Here')
        for obj in result.get('Contents', []):
            print(f'Coming Here Inside:{obj}')
            print('********************************')
            if obj['Key'].endswith('/'):
                print('Coming Here If')
                print(obj['Key'])
except:
    raise    

