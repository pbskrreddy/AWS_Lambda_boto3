# JSON--------->S3--------->LAMBDA-------->DynamoDB
# suppose  a we have json and upload a json to s3 bucket, then lambda will trigger the s3 objects then store into dynamoDB.

import boto3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3'][bucket]['name']
    json_file_name = event['Records'][0]['s3']['oject']['key']
    print(bucket)
    print(json_file_name)
    print(str(event))
    retrun 'Hello from lambda'