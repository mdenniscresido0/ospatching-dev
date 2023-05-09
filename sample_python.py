# This program prints Hello, world!
import boto3
import csv
import sys

print('Hello, world!')


try:
    f = open('sample_os_patching.csv')
    csv_f = csv.reader(f)

    product = 'pim'
    server = 'db'
    exception = ''
    #exception = 'pim5,pim6,pim1'


    result = filter(lambda p: (product == p[1] and server == p[4]), csv_f)
    #result = filter(lambda p: (exception_list[0] != p[0]), result)
    #result = filter(lambda p: (exception_list[1] != p[0]), result)

    if exception == "":
        result = result
    else:
        exception_list = exception.split(",")
        print(exception_list)
        exception_count = len(exception_list)

        if exception_count == 1:
            result = filter(lambda p: (exception_list[0] != p[0]), result)
        elif exception_count == 2:
            result = filter(lambda p: (exception_list[0] != p[0]), result)
            result = filter(lambda p: (exception_list[1] != p[0]), result)
        elif exception_count == 3:
            result = filter(lambda p: (exception_list[0] != p[0]), result)
            result = filter(lambda p: (exception_list[2] != p[0]), result)
            result = filter(lambda p: (exception_list[2] != p[0]), result)     
        else:
            sys.exit("Invalid input")
                  
    for e in result:

        #print(type(e))
        print(e[0], e[1], e[2], e[3], e[4], e[5], e[6])
except IndexError:
    print('except block ran')
