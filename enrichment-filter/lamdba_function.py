import json
#SQS will give one message at a time to lamda this function, because we set batch size = 1 in sqs properties
def lambda_handler(event, context):
    try:
        print('Event: ', event)
        print('context: ', context)
        print(event)
        message =  json.loads(event[0]['body'])
        print(message)
        if (message['startDate'] == message['endDate']):#One msg at a time is feeded here in the lamda fuction from SQS
            message = {}
        return {
            'message': message
        }
    except Exception as e:
        return {
            'Error message': str(e)
        }