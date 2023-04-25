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
   "ALL") echo "all"
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



paramSSMCommandFunction(){

   
    

    inputProfile=$1
    inputRegion=$2
    inputServerType=$3
    inputProduct=$4

    commandSSMDocument=$(caseDocumentNameFunction "$1")
    commandProfile=$(caseEnvironmentFunction "$1")
    commandPath="./sample_os_patching.csv";

    echo "SSM Document Name: $commandSSMDocument"
    echo "Profile name: $commandProfile"
    echo "FilePath: $commandPath"
    while IFS="," read -r col1 col2 col3 col4 col5 col6 col7
        do
             #sleep 0.5
            

            
                commandProduct="$col1"
                commandBatch="$col2"
                commandRegion="$col3"
                commandRegionSorter="$col4"
                commandServerType="$col5"
                commandTagKey="tag:$col6"
                commandTagValue="$col7"
        if [ "$inputServerType" == "all" ] && [ "$inputRegion" == "all"];
            then if [ "$inputProduct" == "$commandBatch" ];
                then ssmCommand=$(createSSMCommand $commandProduct $commandBatch $commandRegion $commandTagKey $commandTagValue $commandComment $commandSSMDocument) 
                    echo $ssmCommand
                fi;
        elif [ "$inputServerType" == "all" ] && [ "$inputRegion" != "all" ];  
            then if [ "$inputRegion" == "$commandRegionSorter" ]  && [ "$inputProduct" == "$commandBatch" ];
                then ssmCommand=$(createSSMCommand $commandProduct $commandBatch $commandRegion $commandTagKey $commandTagValue $commandComment $commandSSMDocument) 
                    echo $ssmCommand

                fi;
        elif [ "$inputServerType" != "all" ] && [ "$inputRegion" == "all" ];
            then if [ "$inputServerType" == "$commandServerType" ]  && [ "$inputProduct" == "$commandBatch" ];
                then ssmCommand=$(createSSMCommand $commandProduct $commandBatch $commandRegion $commandTagKey $commandTagValue $commandComment $commandSSMDocument) 
                    echo $ssmCommand
                fi;     
        else
             if [ "$inputRegion" == "$commandRegionSorter" ]  && [ "$inputProduct" == "$commandBatch" ] && [ "$inputServerType" == "$commandServerType" ];
                then ssmCommand=$(createSSMCommand $commandProduct $commandBatch $commandRegion $commandTagKey $commandTagValue $commandComment $commandSSMDocument) 
            fi;
        fi;
            
        done < <(tail -n 500 "$commandPath")




}

createSSMCommand(){

    commandProduct=$1
    commandBatch=$2
    commandRegion=$3
    commandTagKey=$4
    commandTagValue=$5
    commandComment=$6
    commandSSMDocument=$7
    dateToday=$(date '+%Y-%m-%d')
    
        commandComment="$commandBatch-$commandProduct-$dateToday";

        command="date";

                    
        echo "Product: $commandProduct"        
        echo "Batch name: $commandBatch"  
        echo "Region: $commandRegion"
        echo "Tag Key: $commandTagKey"
        echo "Tag Value: $commandTagValue"
        echo "Comment: $commandComment"
        
        #commandId=$(aws ssm send-command --region $commandRegion --document-name "$commandSSMDocument" --parameters 'commands=["$command"]' --targets "Key=$commandTagKey,Values=$commandTagValue" --comment "$commandComment" --query 'Command.CommandId' --output text)
        #echo "Command ID: $commandId - $commandComment"    

}


mainFunction(){


    #Setting up case parameters
    
    mainEnvironment=$1
    mainRegion=$(caseRegionFunction "$2")
    mainServerType=$(caseServerTypeFunction "$3")
    mainProduct=$(caseProductNameFunction "$4")

    echo $mainRegion $mainServerType $mainProduct

    echo "################################This is in the main function #######################################"
    mainSSMCommandCall=$(paramSSMCommandFunction $mainEnvironment $mainRegion $mainServerType $mainProduct)
    echo $mainSSMCommandCall




}

#First variable $1 = AWS Environment
#Second variable $2 = Region
#Third variable $3 = Server Type
#Fourth variable $4 = Product Name

mainFunction $1 $2 $3 $4
