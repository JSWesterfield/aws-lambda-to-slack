import json
import os
import urllib

# initial challenge, def lambda_handler(event, context) is the entrypoint of every lambda function. 
# The event parameter gives you info about the event that triggered the function (the slack API post request in our case)

# def lambda_handler(event, context):
#     slack_event = json.loads(event["body"])
#     challenge = slack_event["challenge"]
#     return {
#         'statusCode': 200,
#         'body': challenge
#     }

def is_bot(event): 
    return 'bot_profile' in event['event']

def has_file(event):
    return 'files' in event['event']

def message_has_resume(event): 
    return not is_bot(event) and has_file(event)

def send_text_response(event, response_text):
    SLACK_URL = "https://slack.com/api/chat.postEphmeral" # use chat.postMessage if we want visible for everyBody
    channel_id = event["event"]["channel"]
    user = event["event"]["user"]
    bot_token = os.environ["BOT_TOKEN"]
    data = urllib.parse.urlencode({
        "token": bot_token,
        "channel": channel_id,
        "text": response_text,
        "user": user,
        "link_names": True
    })
    data = data.encode("ascii")
    request = urllib.request.Request(
        SLACK_URL, 
        data=data,
        method="POST"
    )
    res = urllib.request.urlopen(request).read()
    print('res:', res)

def lambda_handler(event, context): 
    event = json.loads(event["body"])
    if message_has_resume(event):
        send_text_response(event, "Hello from slack bot via AWS Lambda function.")

        return {
            'statusCode': 200,
            'body': 'OK'
        }