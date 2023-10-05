import botocore
import boto3
import logging

# Set up our logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

client = boto3.client('kinesis')

try:
    logger.info('Calling DescribeStream API on myDataStream')
    client.describe_stream(StreamName='myDataStream')

except botocore.exceptions.ClientError as error:
    if error.response['Error']['Code'] == 'LimitExceededException':
        logger.error('API call limit exceeded; backing off and retrying...')
    else:
        raise error