import json
import os
import urllib

# initial challenge, def lambda_handler(event, context) is the entrypoint of every lambda function. 
# The event parameter gives you info about the event that triggered the function (the slack API post request in our case)
def lambda_handler(event, context):
    slack_event = json.loads(event["body"])
    challenge = slack_event["challenge"]
    return {
        'statusCode': 200,
        'body': challenge
    }
