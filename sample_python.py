import boto3
import csv
import sys
import os
import pandas as pd

def mainFunction():

    inputException = os.environ['Pod Exception']
    inputRegion = os.environ['Region']
    inputServerType = os.environ['Server Type']
    inputProduct = os.environ['Product Name']


    mainRegion=caseRegion(inputRegion)
    mainServerType=caseServerType(inputServerType)
    mainProduct=caseProductName(inputProduct)
    filterData(mainRegion, mainServerType, mainProduct, inputException)



def filterData(runRegion, runServerType, runProduct, runException):

    filter_df = pd.read_csv('sample_os_patching.csv')

    filterProduct = filter_df.query('batch == @runProduct')
    #print(filterProduct)
    if runServerType == "all" and runRegion == "all":
        filterCSVTable = filterProduct
    elif runServerType == "all" and runRegion != "all":
        filterCSVTable = filterProduct.query('reg_lookup == @runRegion')
    elif runServerType != "all" and runRegion == "all":
        filterCSVTable = filterProduct.query('server_lookup == @runServerType')
    else:
        filterCSVTable = filterProduct.query('reg_lookup == @runRegion and server_lookup == @runServerType')
    #print(filterCSVTable)
    if runException == "NA":
        filterCSVTable = filterCSVTable
    else:
        runExceptionList = runException.split(",")
        for runProductFilter in runExceptionList:
            filterDataFinal = filterCSVTable.query('product != @runProductFilter')
            filterCSVTable = filterDataFinal
    
    for index, row in filterCSVTable.iterrows():
        rowProduct = row['product']
        rowBatch = row['batch']
        rowRegion = row['reg']
        rowServerType = row['server_lookup']
        rowKey = row['key']
        rowValue = row['value']
        print(rowProduct,rowBatch,rowRegion,rowServerType,rowKey,rowValue)
        runSSMCommand(rowProduct,rowBatch,rowRegion,rowServerType,rowKey,rowValue)
        


def runSSMCommand(runProduct,runBatch,runRegion,runServerType,runKey,runValue):
    from datetime import date
    runDocument=caseDocument(runServerType)
    
    runToday = date.today()
    runToday = runToday.strftime("%d%m%Y")
    runComment = (runBatch+ "-" +runProduct+ "-" +runToday)
    commandKey = ("tag:" + runKey)
    runCommand='date'

    ssm_client = boto3.client('ssm',region_name=runRegion)
    response = ssm_client.send_command(
                    Targets=[{"Key": commandKey, "Values": [ runValue ]}],
                    Comment=runComment,
                    DocumentName=runDocument,
                    MaxConcurrency='100%',
                    MaxErrors='100%',
                    TimeoutSeconds=900)

    command_id = response['Command']['CommandId']
    print("Command Id:" + command_id)

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
    elif productName == 'MacEnt-Pod-3':
        return "mn3"
    elif productName == 'MacEnt-Pod-11':
        return "mn11"  
    elif productName == 'MacEnt-Pod-4':
        return "mn4"        
    elif productName == 'Maconomy-ENTERPRISE':
        return "macent"
    elif productName == 'Vision-Vantagepoint-ENTERPRISE':
        return "vtent"
    elif productName == 'PIM':
        return "pim"
    elif productName == 'Deltek-Dev':
        return "dev"
    elif productName == 'VF6':
        return "vf6"

def caseServerType(serverType):
    if serverType == 'DB':
        return "db"
    elif serverType == 'NonDB':
        return "nondb"
    elif serverType == 'CTLR':
        return "ctlr"
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
        return "Global-DB-SSM-Document"
    elif documentType == 'nondb':
        return "Global-Non-DB-SSM-Document"
    elif documentType == 'ctlr':
        return "Global-Non-DB-SSM-Document"

mainFunction()
