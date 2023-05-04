# This program prints Hello, world!
import boto3
print('Hello, world!')
ssm_client = boto3.client('ssm',region_name='us-east-1')
response = ssm_client.send_command(
            InstanceIds=['i-186ce5b8'],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': ['date']}, )

command_id = response['Command']['CommandId']
print(command_id)
