# Real-Time Traffic Vehicle Detection System

A comprehensive full-stack application for real-time vehicle detection and traffic monitoring. This thesis project combines modern web technologies with intelligent vehicle detection capabilities to provide a robust monitoring solution.

## Overview

This is a full-stack web application designed to detect and monitor vehicles in real-time. It features:
- Secure authentication via Keycloak
- RESTful API backend built with Flask
- Modern responsive frontend using Next.js
- Containerized deployment with Docker and Kubernetes
- Role-based access control (RBAC)

## Features

- **User Authentication**: OAuth2/OIDC authentication via Keycloak with role-based access levels
- **Vehicle Detection**: Real-time vehicle detection capabilities (framework positioned for ML integration)
- **Responsive UI**: Modern web interface built with React and Next.js
- **Secure API**: CORS-enabled Flask backend with token-based authentication
- **Scalable Infrastructure**: Kubernetes-ready with auto-scaling capabilities
- **Database Integration**: PostgreSQL support with persistent storage
- **Docker Containerization**: Production-ready Docker images for all services

## Tech Stack

### Frontend
- **Framework**: Next.js 15.5.6
- **Language**: TypeScript 5
- **UI Library**: React 19.1.0
- **Styling**: Tailwind CSS 4
- **Linting**: ESLint 9
- **Runtime**: Node.js with Turbopack

### Backend
- **Framework**: Flask (Python)
- **Authentication**: Keycloak (OAuth2/OIDC)
- **CORS**: Flask-CORS
- **HTTP Client**: requests
- **Language**: Python 3

### Infrastructure & DevOps
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Storage**: Persistent Volumes (PostgreSQL)
- **Load Balancing**: Kubernetes Services
- **Auto-scaling**: Kubernetes Horizontal Pod Autoscaler
- **Configuration**: ConfigMaps and Secrets

### Authentication & Security
- **Identity Provider**: Keycloak
- **Realm**: RealtimeTraffic
- **Authentication Method**: OAuth2/OIDC

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd projekt-licencjacki
```

### 2. Backend Setup

```bash
cd backend/app
pip install -r requirements.txt
```

#### Configure Keycloak

Edit `keycloak_config.py` with your Keycloak instance details:

```python
keycloak_admin = KeycloakAdmin(
    server_url="http://your-keycloak-server/",
    username="admin",
    password="your-password",
    realm_name="RealtimeTraffic",
    client_id="your-client-id",
    client_secret_key="your-client-secret",
    verify=False  # For development only
)
```

### 3. Frontend Setup

```bash
cd frontend
npm install
```

## 🏃 Running the Application

### Local Development

#### Start Backend

```bash
cd backend/app
python app.py
```

The API will be available at `http://localhost:5000`

#### Start Frontend

```bash
cd frontend
npm run dev
```

The web interface will be available at `http://localhost:3000`

### Make-based Commands

The project includes a Makefile for build automation:

```bash
# Build Docker image
make build DEPLOYMENT=backend END=backend/
make build DEPLOYMENT=frontend END=frontend/
```

**Note:** Set `DOCKER_USER`, `DOCKER_TOKEN`, and other environment variables before running make commands.

## 🐳 Docker Deployment

### Build Docker Images

```bash
# Frontend
docker build -t underwoodsteam/frontend:latest frontend/

# Backend
docker build -t underwoodsteam/backend:latest backend/

# Database
docker build -t underwoodsteam/database:latest database/
```

### Pull from Docker Hub

```bash
docker pull underwoodsteam/frontend:latest
docker pull underwoodsteam/backend:latest
docker pull underwoodsteam/database:latest
```

## ☸️ Kubernetes Deployment

### Prerequisites

Ensure you have:
1. A running Kubernetes cluster
2. Keycloak deployed and accessible
3. PostgreSQL instance or StatefulSet ready

### Deploy to Kubernetes

```bash
# Deploy database
kubectl apply -f database/deployments/

# Deploy backend
kubectl apply -f backend/deployments/

# Deploy frontend
kubectl apply -f frontend/deployments/
```

### Check Deployment Status

```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

### Access the Application

```bash
# Port forward to frontend service
kubectl port-forward svc/frontend 3000:3000

# Port forward to backend service
kubectl port-forward svc/backend 5000:5000
```

Visit `http://localhost:3000` in your browser.

## Pushing to dev

Before running those commands make sure that you change used image to dev from prod in `(backend/frontend)/deployments/deployment.yml`

```
./run-makefile.sh (frontend/backend)

# if change in k8s deployment file:
kubectl apply -f deployment

# if not:
kubectl rollout restart deployment (backend/frontend)-deployment
```
