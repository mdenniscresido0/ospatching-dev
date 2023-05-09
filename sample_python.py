# This program prints Hello, world!
import boto3
import csv
import sys
import pandas as pd

print('Hello, world!')


try:
    
    exception = "pim5,pim6,pim1"

    df = pd.read_csv('sample_os_patching.csv')

    filter_val = df.query('batch == "pim" & server_lookup == "db"')
    
    if exception == "":
        filter_val = filter_val
    else:
        exception_list = exception.split(",")

    
    for index, row in filter_val.iterrows():
        print(row['product'], row['batch'], row['reg'], row['server_lookup'], row['key'], row['value'])
    

except IndexError:
    print('except block ran')
