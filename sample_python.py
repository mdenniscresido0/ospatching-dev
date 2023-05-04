# This program prints Hello, world!
import boto3
import csv

print('Hello, world!')
ssm_client = boto3.client('ssm',region_name='us-east-1')
response = ssm_client.send_command(
            InstanceIds=['i-01571d416d841669e'],
            Comment='test-command',
            DocumentName="AWS-RunPowerShellScript",
            Parameters={'commands': ['date']}, )

command_id = response['Command']['CommandId']
print(command_id)



f = open('attendees1.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print(row)
