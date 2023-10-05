# checking S3 file existence

import boto3
import os


def get_resource(config: dict={}):
    """Loads the s3 resource.

    Expects AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to be in the environment
    or in a config dictionary.
    Looks in the environment first."""

    s3 = boto3.resource('s3',
                        aws_access_key_id=os.environ.get(
                            "AWS_ACCESS_KEY_ID", config.get("AWS_ACCESS_KEY_ID")),
                        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY", config.get("AWS_SECRET_ACCESS_KEY")))
    return s3


def get_bucket(s3, s3_uri: str):
    """Get the bucket from the resource.
    A thin wrapper, use with caution.

    Example usage:

    >> bucket = get_bucket(get_resource(), s3_uri_prod)"""
    return s3.Bucket(s3_uri)


def isfile_s3(bucket, key: str) -> bool:
    """Returns T/F whether the file exists."""
    objs = list(bucket.objects.filter(Prefix=key))
    return len(objs) == 1 and objs[0].key == key


def isdir_s3(bucket, key: str) -> bool:
    """Returns T/F whether the directory exists."""
    objs = list(bucket.objects.filter(Prefix=key))
    return len(objs) > 1
