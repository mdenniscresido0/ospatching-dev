# This program prints Hello, world!
import boto3
import csv

print('Hello, world!')


try:
    f = open('sample_os_patching.csv')
    csv_f = csv.reader(f)

    product = 'pim'
    server = 'db'
    exception='pim5'
        #filtered = filter(lambda p: ('pim' == p[1] and 'db' == p[4]) , csv_f)
    resultI = filter(lambda p: (exception != p[0]), csv_f)
    result = filter(lambda p: (product == p[1] and server == p[4]), resultI)


    for e in result:

        print(type(e))
        print(e[0], e[2])

except IndexError:
    print('except block ran')
    

