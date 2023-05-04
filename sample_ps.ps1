Import-Module AWSPowerShell
$date=get-date

echo "Today is $date."


Send-SSMCommand -Region us-east-1 -DocumentName "AWS-RunPowerShellScript" -Parameter @{commands = "date"} -InstanceId i-01571d416d841669e
