import boto3
from boto3.dynamodb.conditions import Key

table = boto3.resource('dynamodb').Table('quote')


def get():
    response = table.scan(Limit=1)
    return response['Items'][0]


def delete(quote_id):
    table.delete_item(
        Key={
            'quote_id': quote_id,
        }
    )
