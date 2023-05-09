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
    #result = filter(lambda p: (exception_list[0] != p[0]), result)
    #result = resultF
    #result = filter(lambda p: (exception_list[1] != p[0]), result)
    #result = resultF

    result = filter(lambda p: (exception_list[0] != p[0]), result)
    result = filter(lambda p: (exception_list[1] != p[0]), result)
    

#item_filter = "pim6"
    def filter_set(result, item_filter):
        def iterator_func(x):
            for v in x.values():
                if item_filter != v
                    return True
             return false
        return  filter(iterator_func, result)
    
    filtered_records = filter_set(result, "pim6")    
    #result = filter(lambda p: (exception_list[2] != p[0]), result)

    for e in filtered_records:

        #print(type(e))
        print(e[0], e[1], e[2], e[3], e[4], e[5], e[6])        


except IndexError:
    print('except block ran')
