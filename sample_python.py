# This program prints Hello, world!
import boto3
print('Hello, world!')
ssm_client = boto3.client('ssm',region_name='us-east-1')
response = ssm_client.send_command(
            InstanceIds=['i-01571d416d841669e'],
            DocumentName="AWS-RunPowerShellScript",
            Parameters={'commands': ['date']}, )

command_id = response['Command']['CommandId']
print(command_id)
