import botocore
import boto3

client = boto3.client('aws_service_name')

try:
    client.some_api_call(SomeParam='some_param')

except botocore.exceptions.ClientError as error:
    # Put your error handling logic here
    raise error

except botocore.exceptions.ParamValidationError as error:
    raise ValueError(f'The parameters you provided are incorrect: {error}')