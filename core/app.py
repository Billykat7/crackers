import json
import os


def read_card_handler(event, context):

    dbname  = os.getenv('dbname')
    api_url = os.getenv('api_url')

    return {
        "card": event,
        "statusCode": 200,
        "body": json.dumps({
            "message": "Crackers are here for the AWS Serverless.",
        }),
    }
