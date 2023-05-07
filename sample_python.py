# This program prints Hello, world!
import boto3
import csv

print('Hello, world!')


try:
    f = open('sample_os_patching.csv')
    csv_f = csv.reader(f)

    product = 'pim'
    server = 'db'
    exception='pim5,pim6'
    exception_list = exception.split(",")
    
    print(exception_list[0])
    print(exception_list[1])
       
    
    result = filter(lambda p: (product == p[1] and server == p[4]), csv_f)
    resultF = filter(lambda p: (exception_list[0] != p[0]), result)
    resultF = filter(lambda p: (exception_list[1] != p[0]), resultF)
    #for x in exception_list:
        #resultF = filter(lambda p: (x != p[0]), result)
        #result = resultF
        
        
    
    #result = filter(lambda p: (product == p[1] and server == p[4]), resultI)


    for e in resultF:

        #print(type(e))
        print(e[0], e[1], e[2], e[3], e[4], e[5], e[6])

except IndexError:
    print('except block ran')
    

