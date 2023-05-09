def mainFunction():
    import boto3
    import csv
    import sys
    import pandas as pd
    import os

    assert sys.version_info >= (3, 10)
    
    inputException = os.environ['Product Exception']
    inputRegion = os.environ['Region']
    inputServerType = os.environ['Server Type']
    inputProduct = os.environ['Product Name']


    mainRegion=caseRegion(inputRegion)
    mainServerType=caseServerType(inputServerType)
    mainProduct=caseProductName(inputProduct)
    mainException=inputException

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
    match productName:
        case "Ajera":
            return "ajera"
        case "Citrix":
            return "citrix"
        case "DFME_Maconomy-ESSENTIALS":
            return "dfme"
        case "DFVE_Vision-Vantagepoint-ESSENTIALS":
            return "dfve"
        case "MacEnt-Pod-5_and_14":
            return "mn5-14"
        case "Pod-MN11":
            return "mn11"
        case "Pod-MN3":
            return "mn3"
        case "Maconomy-ENTERPRISE":
            return "macent"
        case "Vision-Vantagepoint-ENTERPRISE":
            return "vtent"
        case "PIM":
            return "pim"
        case "Deltek-Dev":
            return "dev"

def caseServerType(serverType):
    match serverType:
        case "DB":
            return "db"
        case "NonDB":
