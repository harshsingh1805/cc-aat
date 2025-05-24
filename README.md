
This is a basic template for deploying machine learning models as a web application using **Flask**.

## Getting Started
(Run the bash code in your VSCode's terminal)

### 1. Clone the Repository
Clone the repository to your local machine (make sure u have git installed):

### 2. Eun docker locally
docker build -t loan-predictor .

docker run -p 5000:5000 loan-predictor


------------------------------------------------------------------------------------------------------
# ☁️ Azure Deployment Guide (Using Docker Container)

This app was deployed using **Azure App Service (Linux)** with a custom Docker image. Here is how the deployment was done:

---

### 🔁 Step-by-Step Azure Deployment Process

#### 📌 Step 1: Build and Push Docker Image to Docker Hub

> Ensure your Docker image is ready and pushed publicly to Docker Hub.

```bash
docker build -t harsh1805/loan-predictor .
docker push harsh1805/loan-predictor
```

#### ☁️ Step 2: Log in to Azure via CLI

```bash
az login
```

#### 📦 Step 3: Create a Resource Group

```bash
az group create --name LoanPredictorGroup --location westindia
```

#### 🏗️ Step 4: Register the Web App Provider (if needed)

```bash
az provider register --namespace Microsoft.Web
```

#### 🏭 Step 5: Create App Service Plan (Linux)

```bash
az appservice plan create `
  --name LoanPredictorPlan `
  --resource-group LoanPredictorGroup `
  --is-linux `
  --sku B1 `
  --location westindia
```

#### 🌐 Step 6: Create Web App with Docker Container

```bash
az webapp create `
  --resource-group LoanPredictorGroup `
  --plan LoanPredictorPlan `
  --name loan-predictor-azure123 `
  --docker-custom-image-name harsh1805/loan-predictor
```

#### 🔎 Step 7: Get the Public URL

```bash
az webapp show `
  --resource-group LoanPredictorGroup `
  --name loan-predictor-azure123 `
  --query defaultHostName `
  -o tsv
```

Copy the URL and open it in your browser — your app is now live on Azure!
