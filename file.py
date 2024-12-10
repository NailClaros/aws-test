import boto3
import os
from dotenv import load_dotenv
load_dotenv()

s3 = boto3.client('s3')

S3_BUCKET = os.getenv('S3_BUCKET')
if not S3_BUCKET:
    raise ValueError("S3_BUCKET environment variable is not set!")

s3.upload_file('ex.wav', S3_BUCKET, 'ex.wav')
s3.upload_file('img.png', S3_BUCKET, 'ex.png ..')
print("File uploaded successfully!")