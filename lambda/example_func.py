import json
import boto3

def lambda_handler(event, context):
    print(event)
    return event