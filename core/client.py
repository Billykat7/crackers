import simplejson as json

from boto3.dynamodb.conditions                  import Key

from conn                                       import DBConnect


db_data    = DBConnect().db_details()
dynamodb   = db_data['db_name']
table_name = db_data['table_name']


def create_client(event, context):

    client_i   = json.loads(event['body'])
    table      = dynamodb.Table(table_name)
    response   = table.put_item(TableName = table_name, Item = client_i)
    print(response)

    data = {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps(response)
    }

    return data


def get_client(event, context):

    table      = dynamodb.Table(table_name)
    client_id  = int(event['pathParameters']['id'])
    response   = table.query(KeyConditionExpression=Key('id').eq(client_id))

    data = {
        'statusCode' : 200,
        'headers'    : {},
        'body'       : json.dumps(response['Items'])
    }

    return data
    