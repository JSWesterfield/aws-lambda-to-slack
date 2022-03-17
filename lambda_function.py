import json
import os
import urllib

def lambda_handler(event, context):
    slack_event = json.loads(event["body"])
    challenge = slack_event["challenge"]
    return {
        'statusCode': 200,
        'body': challenge
    }
