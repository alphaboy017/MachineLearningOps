# MLflow-Project


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/alphaboy017/MLflow-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/alphaboy017/MLflow-Project.mlflow \
MLFLOW_TRACKING_USERNAME=alphaboy017 \
MLFLOW_TRACKING_PASSWORD=2261233cd3fb0adfeeafe605203546596d34800a \
python script.py

Run this to export as env variables:
//Note that 'Export' command works in Linux ONLY
use this for Windows 
$env:MLFLOW_TRACKING_URI = "https://dagshub.com/alphaboy017/MLflow-Project.mlflow"
$env:MLFLOW_TRACKING_USERNAME = "alphaboy017"
$env:MLFLOW_TRACKING_PASSWORD = "your_dagshub_access_token_here" 
```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/alphaboy017/MLflow-Project.mlflow

export MLFLOW_TRACKING_USERNAME=alphaboy017 

export MLFLOW_TRACKING_PASSWORD=2261233cd3fb0adfeeafe605203546596d34800a

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 586177432912.dkr.ecr.eu-north-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=<your-aws-access-key>
    AWS_SECRET_ACCESS_KEY=<your-aws-secret-key>
    AWS_REGION=<your-aws-region>
    AWS_ECR_LOGIN_URI=<your-ecr-login-uri>
    ECR_REPOSITORY_NAME=<your-ecr-repo-name>




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


