
const AWS = require('aws-sdk');
var url = require('url');
var https = require('https');
var util = require('util');
const p = require('phin');

const reqURL = `https://hooks.slack.com/services/{example-webhook}`;

async function notifySlack() {

const message = {
    'channel': '<Notification Slack channel>',
    'username': 'Build Server',
    'text': 'Jenkins: Open Jenkins Build server here',
    'icon_emoji': ':aws:',
    'attachments': [{
        'color': '#8697db',
        'fields': [
            {
            'title': 'EC2 server',
            'value': 'EC2 server Starting...',
            'short': true
            }
        ]
    }]
};

  return p({
    url: reqURL,
    method: 'POST',
    data: message
  });
}

exports.handler = async (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
   const ec2 = new AWS.EC2({ region: event.instanceRegion });
    
    ec2.startInstances({ InstanceIds: [event.instanceId] }).promise()
        .then(() => callback(null, `Successfully started ${event.instanceId}`))
        .catch(err => callback(err));
  
  const req = await notifySlack();

};