. ps-scripts/env.ps1

$ecrUri = "$($AWS_ACCOUNT_ID).dkr.ecr.$($AWS_REGION).amazonaws.com/$($ECR_REPO)"

# Build the Docker image
Write-Output "Docker Building: $($IMAGE_NAME):$($TAG)"
zappa save-python-settings-file dev
docker build -t "$($IMAGE_NAME):$($TAG)" .

# Tag the Docker image with the ECR repository URI
Write-Output "Docker Tagging: $($IMAGE_NAME):$($TAG) -> $($ecrUri):$($TAG)"
docker tag "$($IMAGE_NAME):$($TAG)" "$($ecrUri):$($TAG)"

# Authenticate to ECR using the AWS CLI
Write-Output "Authenticating Docker: $($ecrUri)"
aws ecr get-login-password | docker login --username AWS --password-stdin "$($ecrUri)"

# Push the Docker image to ECR
Write-Output "Docker Pushing: $($ecrUri):$($TAG)"
docker push "$($ecrUri):$($TAG)"