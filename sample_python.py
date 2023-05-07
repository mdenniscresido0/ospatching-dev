# This program prints Hello, world!
import boto3
import csv

print('Hello, world!')


try:
    f = open('sample_os_patching.csv')
    csv_f = csv.reader(f)

    product = 'pim'
    server = 'db'
    exception='pim5,pim6,pim7'
    exception_list = exception.split(",")
    
    print(exception_list[0])
    print(exception_list[1])
       
    
    result = filter(lambda p: (product == p[1] and server == p[4]), csv_f)
    c = int(0)
    for exception_item in exception_list:
        c = c + 1
        print(exception_item + ' - ' + c)
        resultFinal = filter(lambda p: (exception_item != p[0]), result)
        result = resultFinal
        
        
    
    #result = filter(lambda p: (product == p[1] and server == p[4]), resultI)


    for e in result:

        #print(type(e))
        print(e[0], e[1], e[2], e[3], e[4], e[5], e[6])

except IndexError:
    print('except block ran')
    

