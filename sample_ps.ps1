$servername=$env:ComputerName
$date=get-date

Write-Output "Today is $date. This is executed in server: $servername"


Send-SSMCommand -Region us-east-1 -DocumentName "AWS-RunPowerShellScript" -Parameter @{commands = "date"} -InstanceId i-186ce5b8
