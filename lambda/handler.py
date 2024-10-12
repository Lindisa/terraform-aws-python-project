# lambda/handler.py

import json
import boto3

def lambda_handler(event, context):
    print("Received S3 event:", json.dumps(event, indent=2))
    # Add your processing logic here
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
