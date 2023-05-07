# This program prints Hello, world!
import boto3
import csv

print('Hello, world!')


try:
    f = open('sample_os_patching.csv')
    csv_f = csv.reader(f)

    product = 'pim'
    server = 'db'
    exception='pim5, pim6, pim7'
    exception_list = exception.split(",")
       
    
    result = filter(lambda p: (product == p[1] and server == p[4]), csv_f)
    for x in exception_list:
        result = filter(lambda p: (x != p[0]), result)
        
    
    #result = filter(lambda p: (product == p[1] and server == p[4]), resultI)


    for e in result:

        print(type(e))
        print(e[0], e[2])

except IndexError:
    print('except block ran')
    

