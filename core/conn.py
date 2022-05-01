import os

import boto3


class DBConnect:

    def __init__(self):
        self.db = None

    def create_db(self):
        pass

    def db_details(self):

        dynamodb   = boto3.resource('dynamodb')
        table_name = os.environ.get('CLIENTS_TABLE')

        db_data = {
            'db_name'    : dynamodb,
            'table_name' : table_name
        }

        return db_data
