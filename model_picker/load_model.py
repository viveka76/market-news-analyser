import boto3
import json

secret_manager_client = boto3.client('secretsmanager')
response = secret_manager_client.get_secret_value(SecretId='kodekloud_api')
secret = json.loads(response['SecretString'])
print(secret)

