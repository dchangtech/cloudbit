import boto3
import json
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)