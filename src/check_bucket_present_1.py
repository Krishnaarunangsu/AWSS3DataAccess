from re import T
import boto3

s3_resource=boto3.resource('s3')
print(f's3_resource is:{s3_resource}')
print('***************************************')

total_s3_buckets=s3_resource.buckets.all()
print(f'Total No of s3 vuckets:{type(total_s3_buckets)}')
size=sum(1 for _ in s3_resource.buckets.all())
print(f'Bucket list length is:{size}')
print('***************************************')
for bucket in total_s3_buckets:
    print(f'Bucket Name is:{bucket.name}')
    print('######################################')