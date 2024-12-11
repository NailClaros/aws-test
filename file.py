import boto3
import os
from dotenv import load_dotenv
import base64
import requests
load_dotenv()

s3 = boto3.client('s3')

S3_BUCKET = os.getenv('S3_BUCKET')
if not S3_BUCKET:
    raise ValueError("S3_BUCKET environment variable is not set!")

s3.upload_file('ex.wav', S3_BUCKET, 'ex.wav')
s3.upload_file('img.png', S3_BUCKET, 'ex.png')
print("File uploaded successfully!")

print("Retriving file! -- ex.wav for api use")
def get_s3_file_binary(bucket_name, object_key):
    try:
        # Fetch binary content from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        file_binary = response['Body'].read()
                
        # Encode binary data to base64
        return base64.b64encode(file_binary).decode('utf-8')
    except Exception as e:
        print(f"Error reading audio file from S3: {e}")
        return None

file_binary = get_s3_file_binary(S3_BUCKET, 'ex.wav')

url = "https://shazam.p.rapidapi.com/songs/v2/detect"
querystring = {"timezone": "America/Chicago", "locale": "en-US"}
headers = {
    "x-rapidapi-key": os.getenv('key_n'),
    "x-rapidapi-host": "shazam.p.rapidapi.com",
    "Content-Type": "application/octet-stream"
}


# Sending the binary audio content as payload
response = requests.post(url, data=file_binary, headers=headers, params=querystring, timeout=10)

# Log the raw response for debugging
print(f"Response Content: {response.text}")


print("Retriving file! -- ex.png")
response = s3.get_object(Bucket=S3_BUCKET, Key='ex.png')
if not response:
    raise ValueError("File not retrieved!")

print("File retrieved successfully!")


