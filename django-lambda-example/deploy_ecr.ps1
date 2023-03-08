. ./env.ps1

$ecrUri = "$($AWS_ACCOUNT_ID).dkr.ecr.$($AWS_REGION).amazonaws.com/$($ECR_REPO)"

zappa update dev -d "$($ecrUri):$($TAG)"