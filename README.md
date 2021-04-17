# Operationalizing Machine Learning in Azure

## Overview
In this project we aim to predict if a client will subscribe into bank services based on various independent variables from the customers which can be found in this [Bankmarketing Datset](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv). We build an end to end solution from dataset preparation, model training, deployment, and model monitoring. In addition, we also create a pipeline to automate the process.

## Architectural Diagram


## Key Steps

### Step 1 Authentication
In this step, I used lab provided by Udacity. So that I dont need to setup the authentication.

### Step 2 Automated ML Experiment

This step start with uploading [Bankmarketing Datset](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) into the Azure ML Studio. 

![Bankmarketing Dataset]()  
*Figure 1: Bank Marketing Dataset*

After that, I used the data to performed Automated Machine Learning Experiment using Classification with **y** as a target variable. This variable show that the customer will subscribe or not into the bank services.

![AutomatedML Running]()  
*Figure 2: Automated ML Running*

As a result, the best model for this experiment is VotingEnsemble with 91.75 % model accuracy.

![Best Model Resutls]()  
*Figure 3: Automated ML Results*

### Step 3 Deploy the best model

In this step, the VotingEnsemble model was deployed. This deployment will allow interaction with the HTTP API service and interact with the model by sending the data over POST request. The deployment was using the Azure Container Instance (ACI) and enabling the authentication.

![Model Deployed]()  
*Figure 4: Model Successfully deployed*

### Step 4 Enable logging

In this step we will 

### Step 5 Swagger Documentation


### Step 6 Consume model endpoints
### Step 7 Create and publish a pipeline
