# This program prints Hello, world!
import boto3
import csv
import sys
import pandas as pd

print('Hello, world!')


try:

    df = pd.read_csv('sample_os_patching.csv')

    filter = df.query('batch == "pim" & server_lookup == "db"')
    filtered = filter.query('product != "pim3"')
    for index, row in filtered.iterrows():
        print(row['product'], row['batch'], row['reg'], row['server_lookup'], row['key'], row['value'])
    

except IndexError:
    print('except block ran')
