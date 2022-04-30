import json
import os


def create_client(event, context):

    # client = json.loads(event['body'])

    data = {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Crackers clients created!'})
    }

    print('CREATE CLIENT CALLED!')

    return data


def get_client(event, context):

    client = {
        'id'              : 1,
        'clientFirstName' : 'Billy',
        'clientLastName'  : 'Paul',
        'cardNumber'      : 1980247972641,
        'cardBalance'     : 200,
        'currency'        : 'CFC',
        'cardDateFrom'    : '2022-04-05',
        'cardDateTo'      : '2024-04-04',
        'dateJoined'      : '2022-04-05'
    }

    data = {
        'statusCode' : 200,
        'headers'    : {},
        'body'       : json.dumps(client)
    }

    print('GET CLIENT REQUESTED!')

    return data
    