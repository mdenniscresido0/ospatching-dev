#!/bin/bash
# ------------------------------------------------------------------------
# ./OSPatching_Automation.sh
# Michael Dennis M. Cresido, 03/27/2023
#
# This Shell script is to automate the process in creating
# SSM command during OS patching. This is a back-end script that will
# call the patching script and will be deployed using Jenkins.
# Jenkins will be used to create paramaterized deployment and to 
# add approval process.
#
# ------------------------------------------------------------------------
# Version 1.0 - Script is completed
#

caseProductNameFunction(){
    case "$1" in
   "Ajera") echo "ajera"
   ;;
   "Citrix") echo "citrix"
   ;;
   "DFME_Maconomy-ESSENTIALS") echo "dfme"
   ;;
   "DFVE_Vision-Vantagepoint-ESSENTIALS") echo "dfve"
   ;;
   "Pod-MN11") echo "mn11"
   ;;
   "Pod-MN3") echo "mn3"
   ;;
   "Pod-MN5") echo "mn5"
   ;;
   "Pod-MN14") echo "mn14"
   ;;
   "Maconomy-ENTERPRISE") echo "macent"
   ;;
   "Vision-Vantagepoint-ENTERPRISE") echo "vtent"
   ;;
   "PIM") echo "pim"
   ;;
   "Deltek-Dev") echo "dev"
   ;;
esac
}

caseServerTypeFunction(){
    case "$1" in
   "DB") echo "db"
   ;;
   "NonDB") echo "nondb"
   ;;
   "ALL") echo "all"
   ;;   
esac   
}

caseRegionFunction(){
    case "$1" in
   "US") echo "us"
   ;;
   "CA") echo "ca"
   ;;
   "AP") echo "ap"
   ;;  
   "EU") echo "eu"
   ;;      
esac   
}

caseDocumentNameFunction(){
    case "$1" in
   "flexplus") echo "AWS-RunPowerShellScript" #"Flexplus-SSM-OSPatching"
   ;;
   "costpoint") echo "placeholder"
   ;;
   "deltekdev") echo "AWS-RunPowerShellScript" #"Deltekdev-SSM-OSPatching"
   ;;
   "dco") echo "AWS-RunPowerShellScript" #"DCO-SSM-OSPatching"
   ;;
   "goss") echo "placeholder"
   ;;
esac
}


caseEnvironmentFunction(){
    case "$1" in
   "flexplus") echo "flexplus-cli"
   ;;
   "costpoint") echo "costpoint-cli"
   ;;
   "deltekdev") echo "deltekdev-cli"
   ;;
   "dco") echo "DCO-cli"
   ;;
   "goss") echo "oss-cli"
   ;;
esac
}


filterFunction(){
    filterBatch="$1" #$1 = Batch filter
    filterRegion="$2" #$2 = Region filter
    filterServerType="$3" #$3 = Server type filter
    filterEnvironment="$4" #$4 = Environment

    filterSourcePath="./sample_os_patching.csv";
    filterFilePath="./sample_os_patching_filter";
    
    

    sleep 0.5
    if [ $filterServerType = "all" ];
        then echo "All servers will be patch";
            filterNonDBSpecificPath="$filterFilePath-nondb.csv"
            filterDBSpecificPath="$filterFilePath-db.csv"

            
            
            awk -v batch="$filterBatch" -v region="$filterRegion" -v type=$filterServerType -F',' '$2==batch && $4==region && $5=="db"' $filterSourcePath > $filterDBSpecificPath
            awk -v batch="$filterBatch" -v region="$filterRegion" -v type=$filterServerType -F',' '$2==batch && $4==region && $5=="db"' $filterSourcePath > $filterNonDBSpecificPath

            commandOutputDB=$(commandSSMDocument "$filterEnvironment" $filterDBSpecificPath)
            echo $commandOutputDB
            sleep 60
            #rm $filterDBSpecificPath
           


            commandOutputNonDB=$(commandSSMDocument "$filterEnvironment" $filterNonDBSpecificPath)
            echo $commandOutputNonDB

            #rm $filterNonDBSpecificPath
            sleep 2


    else echo "These are the server that will be patched: $filterServerType";
        filterSpecificPath="$filterFilePath-$filterServerType.csv";
        awk -v batch="$filterBatch" -v region="$filterRegion" -v type=$filterServerType -F',' '$2==batch && $4==region && $5==type' $filterSourcePath > $filterSpecificPath

        login_enabled=`aws iam get-login-profile --user-name "MichaelDennisCresido"`
        echo $login_enabled
        commandOutput=$(createSSMCommandFunction "$filterEnvironment" $filterSourcePath)
        echo $commandOutput

        sleep 2
        #rm $filterSpecificPath
    
    fi;
}

createSSMCommandFunction(){

    sleep 1
    dateToday=$(date '+%Y-%m-%d')
    commandSSMDocument=$(caseDocumentNameFunction "$1")
    commandProfile=$(caseEnvironmentFunction "$1")
    commandPath=$2
    echo "SSM Document Name: $commandSSMDocument"
    echo "Profile name: $commandProfile"
    echo "FilePath: $commandPath"
    while IFS="," read -r col1 col2 col3 col4 col5 col6 col7
        do
            commandProduct="$col1"
            commandBatch="$col2"
            commandRegion="$col3"
            commandServerType="$col5"
            commandTagKey="tag:$col6"
            commandTagValue="$col7"
            echo $commandProduct
            echo $commandBatch
            echo $commandRegion
            echo $commandTagKey
            echo $commandTagValue

            commandComment="$commandBatch-$commandProduct-$dateToday"

            command="date"

            
            echo "Product: $commandProduct"        
            echo "Batch name: $commandBatch"  
            echo "Region: $commandRegion"
            echo "Tag Key: $commandTagKey"
            echo "Tag Value: $commandTagValue"
            echo "Comment: $commandComment"

            #aws ssm send-command --region $commandRegion --document-name "$commandSSMDocument" --parameters 'commands=["$command"]' --targets "Key=$commandTagKey,Values=$commandTagValue" --comment "$commandComment"
        done < <(tail "$commandPath")


    #aws ssm send-command --profile $commandProfile --region $commandRegion --document-name "$commandSSMDocument" --parameters 'commands=["$command"]' --targets "Key=$commandTagKey,Values=$commandTagValue" --comment "$commandComment"


}


mainFunction(){


    #Setting up case parameters
    
    mainEnvironment=$1
    mainRegion=$(caseRegionFunction "$2")
    mainServerType=$(caseServerTypeFunction "$3")
    mainProduct=$(caseProductNameFunction "$4")
    filterLogs=$(filterFunction "$mainProduct" "$mainRegion" "$mainServerType" "$mainEnvironment")

    echo $filterLogs




}

#First variable $1 = AWS Environment
#Second variable $2 = Region
#Third variable $3 = Server Type
#Fourth variable $4 = Product Name

mainFunction $1 $2 $3 $4

