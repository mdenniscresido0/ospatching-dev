import boto3
import csv
import sys
import os
import pandas as pd

def mainFunction():


    
    #inputException = os.environ['Product Exception']
    inputRegion = os.environ['Region']
    inputServerType = os.environ['Server Type']
    inputProduct = os.environ['Product Name']


    mainRegion=caseRegion(inputRegion)
    mainServerType=caseServerType(inputServerType)
    mainProduct=caseProductName(inputProduct)
    mainException=""

    mainCommand=filterData(mainRegion, mainServerType, mainProduct, mainException)
    print(mainCommand)
    print('Hello, world!')


def filterData(runRegion, runServerType, runProduct, runException):

    filter_df = pd.read_csv('sample_os_patching.csv')
    filterProduct = filter_df.query('batch == @runProduct')

    if runServerType == "all" and runRegion == "all":
        filterCSVTable = filterProduct
    elif runServerType == "all" and runRegion != "all":
        filterCSVTable = filterProduct.query('reg_lookup == @runRegion')
    elif runServerType != "all" and runRegion != "all":
        filterCSVTable = filterProduct.query('server_lookup == @runServerType')
    else:
        filterCSVTable = filterProduct.query('reg_lookup == @runRegion & server_lookup == @runServerType')

    if runException == "":
        filterCSVTable = filterCSVTable
    else:
        runExceptionList = runException.split(",")
        for runProductFilter in runExceptionList:
            filterDataFinal = filterCSVTable.query('product != @runProductFilter')
            filterCSVTable = filterDataFinal        
    
    for index, row in filterCSVTable.iterrows():

        print(row['product'], row['batch'], row['reg'], row['server_lookup'], row['key'], row['value'])


#def runSSMCommand():
    #print

def caseProductName(productName):
    if productName == 'Ajera':
        return "ajera"
    elif productName == 'Citrix':
        return "citrix"
    elif productName == 'DFME_Maconomy-ESSENTIALS':
        return "dfme"
    elif productName == 'DFVE_Vision-Vantagepoint-ESSENTIALS':
        return "dfve"
    elif productName == 'MacEnt-Pod-5_and_14':
        return "mn5-14"
    elif productName == 'MacEnt-Pod-3_and_11':
        return "mn3-11"
    elif productName == 'Maconomy-ENTERPRISE':
        return "macent"
    elif productName == 'Vision-Vantagepoint-ENTERPRISE':
        return "vtent"
    elif productName == 'PIM':
        return "pim"
    elif productName == 'Deltek-Dev':
        return "dev"

def caseServerType(serverType):
    if serverType == 'DB':
        return "db"
    elif serverType == 'NonDB':
        return "nondb"
    elif serverType == 'ALL':
        return "all"

        
def caseRegion(region):
    if region == 'US':
        return "us"
    elif region == 'EU':
        return "eu"
    elif region == 'CA':
        return "ca"
    elif region == 'AP':
        return "ap"
    elif region == 'ALL':
        return "all"        
 

def caseDocument(documentType):
    if documentType == 'db':
        return "AWS-RunPowerShellScript"
    elif documentType == 'nondb':
        return "AWS-RunPowerShellScript"



mainFunction()
