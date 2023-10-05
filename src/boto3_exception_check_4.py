import botocore
import boto3



client = boto3.client('sqs')
queue_url = 'SQS_QUEUE_URL'

try:
    client.send_message(QueueUrl=queue_url, MessageBody=('some_message'))

except botocore.exceptions.ClientError as err:
    if err.response['Error']['Code'] == 'InternalError': # Generic error
        # We grab the message, request ID, and HTTP code to give to customer support
        error_message=err.response['Error']['Message']
        request_id=err.response['ResponseMetadata']['RequestId']
        http_code=err.response['ResponseMetadata']['HTTPStatusCode']
        print(f'Error Message: {error_message}')
        print('Request ID: {request_id}')
        print('Http code: {http_code}')
    else:
       raise err