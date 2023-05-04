# This program prints Hello, world!
import boto3
import csv

print('Hello, world!')
ssm_client = boto3.client('ssm',region_name='us-east-1')
response = ssm_client.send_command(
            InstanceIds=['i-186ce5b8'],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': ['date']}, )

command_id = response['Command']['CommandId']
print(command_id)



f = open('attendees1.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print(row)
