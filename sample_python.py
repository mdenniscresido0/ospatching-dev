# This program prints Hello, world!
import boto3
import csv
import sys
import pandas as pd

print('Hello, world!')


try:

    df = pd.read_csv('sample_os_patching.csv')

    filter = df.query('batch=="pim" & server_lookup=="db"')
    for index, row in df.iterrows():
        print(row['batch'], row['reg'], row['server_lookup'])
    

except IndexError:
    print('except block ran')
