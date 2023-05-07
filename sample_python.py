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




product = 'pim'
server = 'db'
with open('sample_os_patching.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if row:
            if product == row[0] and server == row[4]:
                cfd_checked_before = "Yes"
                print(row[0],row[1],row[2],row[3],row[4],row[5])
