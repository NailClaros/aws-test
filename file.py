import boto3
import os
s3 = boto3.client('s3')

S3_BUCKET = os.getenv('S3_BUCKET')
s3.upload_file('img.png', S3_BUCKET, 'test.png')