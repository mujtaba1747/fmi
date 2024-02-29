import fmi
import json
# import subprocess

def lambda_handler(event, context):
    # Replace 'your_command_here' with the actual shell command you want to run
    print(fmi)
    return {
        'statusCode': 200,
        'body': json.dumps('Imported FMI in lambda!')
    }