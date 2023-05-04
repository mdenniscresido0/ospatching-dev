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



f = open('sample_os_patching.csv')
csv_f = csv.reader(f)
filtered = filter(lambda p: ('pim' == p[1] and 'db' == p[4]) , csv_f)

for row in filtered:
  print(row)
