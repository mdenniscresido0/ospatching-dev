# This program prints Hello, world!
import boto3
import pandas

print('Hello, world!')
ssm_client = boto3.client('ssm',region_name='us-east-1')
response = ssm_client.send_command(
            InstanceIds=['i-186ce5b8'],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': ['date']}, )

command_id = response['Command']['CommandId']
print(command_id)

pandas.set_option('expand_frame_repr', False)
df = pandas.read_csv('./sample_os_patching.csv')
print('---Here are all 7 lines---')
print(df)
print('---Here are the first 5 lines---')
print(df.head())
