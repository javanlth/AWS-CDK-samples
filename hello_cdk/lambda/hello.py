import json

def handler(event, context):
    #print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        #'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
        'body': 'Hello world!',
    }


def main(event, context):
    # save event to logs
    print(event)

    return {
        'statusCode': 200,
        'body': event
    }
