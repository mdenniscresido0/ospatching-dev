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



#f = open('sample_os_patching.csv')
#csv_f = csv.reader(f)

product = 'pim'
server = 'db'
#filtered = filter(lambda p: ('pim' == p[1] and 'db' == p[4]) , csv_f)
#result = filter(lambda p: (product == p[1] and server == p[4]) , csv_f)

#print(list(result))
#for e in result:
   # print(e)

with open('sample_os_patching.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)#, delimiter=',')
    lines = [i for i in csv_reader]
    header = lines[0]
    results = filter(lambda row: (product == row[1] and server == row[4]), lines[1:])
    

    for res in range(100):
        print(res)
        print(results[res])
