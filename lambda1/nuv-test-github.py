import json
 
def lambda_handler(event, context):
    # TODO implement
    print('event')
    print('Hola mundo!)
          
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
 
 
