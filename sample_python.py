# This program prints Hello, world!
import boto3
import csv

print('Hello, world!')


try:
    f = open('sample_os_patching.csv')
    csv_f = csv.reader(f)

    product = 'pim'
    server = 'db'
    exception='pim5, pim6'
    exception_list = exception.split(",")
       
    
    result = filter(lambda p: (product == p[1] and server == p[4]), csv_f)
    listResult = result
    for x in exception_list:
        resultF = filter(lambda p: (x != p[0]), listResult)
        listResult = resultF
        
    
    #result = filter(lambda p: (product == p[1] and server == p[4]), resultI)


    for e in listResult:

        print(type(e))
        print(e[0], e[2])

except IndexError:
    print('except block ran')
    

