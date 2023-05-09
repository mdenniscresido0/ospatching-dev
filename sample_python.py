# This program prints Hello, world!
import boto3
import csv
import sys
import pandas as pd

print('Hello, world!')


try:

    dataFrame = pd.read_csv('sample_os_patching.csv')
    print("DataFrame...\n",dataFrame)

    # select rows containing text "Lamborghini"
    dataFrame = dataFrame[dataFrame['batch'].str.contains('pim')]
    print("\nFetching rows with text Lamborghini ...\n",dataFrame)

except IndexError:
    print('except block ran')
