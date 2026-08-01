<div align="center">

# ☁️ CloudSense AI

### AI-Powered AWS Cloud Infrastructure Management Platform

<p align="center">

A modern cloud management platform built with **FastAPI**, **React**, **TypeScript**, and **AWS** that simplifies infrastructure monitoring, cloud operations, reporting, and intelligent cloud management through an extensible AI Copilot architecture.

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=FF9900)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</p>

</div>

---

# 📖 Overview

CloudSense AI is a full-stack cloud infrastructure management platform that enables users to monitor, manage, and analyze AWS resources through a unified dashboard.

The platform automatically discovers AWS resources, provides infrastructure insights, tracks operational metrics, manages incidents, generates reports, and includes an extensible AI Copilot architecture for intelligent cloud assistance.

The current release focuses on **Amazon Web Services (AWS)** while maintaining a modular architecture that can be extended to additional cloud providers in future versions.

---

# ✨ Features

## 🔐 Authentication & Security

- Secure user authentication
- JWT-based authorization
- Protected application routes
- User-specific AWS account management
- Encrypted AWS credential storage

---

## ☁️ AWS Integration

CloudSense AI securely connects to AWS using the official AWS SDK (Boto3) and automatically discovers cloud resources.

### Currently Supported Services

- Amazon EC2
- Amazon S3
- Amazon RDS
- AWS Lambda
- Amazon VPC
- Amazon EBS

Infrastructure information is fetched directly from AWS in real time.

---

## 📊 Dashboard

The dashboard provides a centralized overview of your AWS environment.

Features include:

- Resource summaries
- Infrastructure statistics
- Cloud health overview
- Operational metrics
- Live AWS resource counts

---

## 🏗 Infrastructure Monitoring

Monitor AWS infrastructure through a centralized interface.

Includes:

- EC2 Instances
- S3 Buckets
- RDS Databases
- Lambda Functions
- VPC Networks
- EBS Volumes

Cloud resources are discovered dynamically from the connected AWS account.

---

## ⚙️ Operations

Operational dashboard providing:

- Resource health
- Infrastructure overview
- Performance monitoring
- Operational analytics
- Cloud activity summaries

---

## 🚨 Incident Management

Monitor and review infrastructure incidents.

Features include:

- Active incidents
- Severity tracking
- Estimated impact
- Resolution progress
- Incident summaries

---

## 📈 Reports & Analytics

Generate operational reports including:

- Infrastructure reports
- Resource summaries
- Operational analytics
- Performance insights
- Cloud statistics

---

## 🔗 Integrations

CloudSense AI follows a modular architecture designed for multi-cloud support.

### Current

- ✅ Amazon Web Services (AWS)

### Planned

- Microsoft Azure
- Google Cloud Platform
- Oracle Cloud
- Kubernetes
- Third-party monitoring tools

---

## 🤖 AI Copilot

CloudSense AI includes a modular AI Copilot architecture designed to assist users with cloud infrastructure analysis.

Current capabilities include:

- Cloud context generation
- Prompt engineering layer
- Conversational workflow
- Modular LLM integration architecture
- Infrastructure-aware responses

The AI layer is designed for future integration with enterprise-grade Large Language Models.

---

# 🏛 Architecture

```text
                        CloudSense AI

                 React + TypeScript Frontend
                           │
                     REST API Requests
                           │
                           ▼
                   FastAPI Backend Services
                           │
     ┌──────────────┬──────────────┬──────────────┐
     │              │              │              │
 Authentication   Dashboard     AI Copilot   AWS Discovery
     │              │              │              │
 PostgreSQL     Infrastructure  Prompt Layer    boto3 SDK
     │           Operations      Context Engine     │
     │           Reports         LLM Layer          │
     │           Incidents                           │
     │                                              ▼
     └──────────────► Amazon Web Services ◄─────────┘
```

---

# 🛠 Technology Stack

## Languages

- Python
- TypeScript
- SQL

---

## Frontend

- React.js
- TypeScript
- Tailwind CSS
- Axios
- React Router
- Lucide React

---

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Boto3

---

## Database

- PostgreSQL
- SQLAlchemy ORM

---

## Cloud

Amazon Web Services

- EC2
- S3
- RDS
- Lambda
- VPC
- EBS

---

## DevOps & Tools

- Docker
- Git
- GitHub

---

# 📂 Project Structure

```text
CloudSense-AI

├── backend
│   ├── app
│   │   ├── ai_copilot
│   │   ├── auth
│   │   ├── cloud
│   │   ├── dashboard
│   │   ├── infrastructure
│   │   ├── operations
│   │   ├── incidents
│   │   ├── reports
│   │   ├── integrations
│   │   ├── models
│   │   ├── database
│   │   ├── core
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── api
│   │   ├── components
│   │   ├── layouts
│   │   ├── pages
│   │   ├── hooks
│   │   └── App.tsx
│   │
│   └── package.json
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/himani-1211/CloudSense-AI.git
cd CloudSense-AI
```

---

# ⚙️ Backend Setup

Navigate to the backend directory.

```bash
cd backend
```

Create a virtual environment.

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the backend server.

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

FastAPI Interactive Documentation:

```
http://localhost:8000/docs
```

---

# 💻 Frontend Setup

Navigate to frontend.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Start the development server.

```bash
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 🐳 Docker

CloudSense AI uses **Docker Compose** to provision the PostgreSQL database used by the backend.

Start Docker services.

```bash
docker compose up -d
```

Stop Docker services.

```bash
docker compose down
```

Docker automatically provisions:

- PostgreSQL Database
- Persistent Database Storage
- Local Docker Network

---

# 🔐 Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
# DATABASE

DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>

POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<database_name>
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# JWT AUTHENTICATION

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

# ENCRYPTION

ENCRYPTION_KEY=your_encryption_key

# AWS

AWS_DEFAULT_REGION=ap-south-1
```

> **Important**
>
> AWS Access Keys are securely stored after users connect their AWS account through the application and should never be hardcoded.

---

# 📡 REST API Modules

CloudSense AI follows a modular backend architecture.

| Module | Description |
|---------|-------------|
| Authentication | User Authentication & Authorization |
| Dashboard | Cloud Dashboard Statistics |
| Infrastructure | AWS Resource Discovery |
| Operations | Operational Monitoring |
| Incidents | Incident Management |
| Reports | Cloud Reporting |
| Integrations | Cloud Integrations |
| AI Copilot | Intelligent Cloud Assistant |

---

# ⚡ Performance Optimizations

CloudSense AI includes several backend optimizations for improved responsiveness.

### Parallel AWS Resource Discovery

AWS resources are discovered concurrently using Python's `ThreadPoolExecutor`.

Benefits include:

- Reduced infrastructure discovery latency
- Faster dashboard loading
- Improved API responsiveness
- Better scalability across AWS services

---

### Modular Backend Architecture

The backend follows a layered architecture.

```
API Router
     │
Business Service
     │
Cloud Service Layer
     │
AWS SDK (Boto3)
```

This separation improves maintainability, scalability, and code organization.

---

# 🤖 AI Copilot

CloudSense AI includes an extensible AI Copilot architecture.

Current implementation:

- Conversational interface
- Context generation
- Prompt engineering layer
- Modular LLM integration architecture
- Infrastructure-aware workflow

Future enhancements:

- Amazon Bedrock Integration
- Intelligent Cloud Recommendations
- Root Cause Analysis
- Cloud Cost Optimization
- Security Best Practices
- AI-powered Operational Insights

---

# 📈 Current Project Status

### ✅ AWS MVP Completed

Implemented modules:

- Authentication
- AWS Integration
- Dashboard
- Infrastructure
- Operations
- Incident Management
- Reports
- Integrations
- AI Copilot Architecture

---

# 🛣️ Roadmap

### Completed

- User Authentication
- AWS Resource Discovery
- Infrastructure Monitoring
- Operational Dashboard
- Incident Management
- Reports
- AI Copilot Backend Architecture
- Parallel AWS Discovery

### In Progress

- Enterprise LLM Integration
- Intelligent AI Copilot
- Enhanced Infrastructure Analysis

### Planned

- Microsoft Azure Integration
- Google Cloud Platform Integration
- Oracle Cloud Integration
- Kubernetes Monitoring
- CloudWatch Metrics
- Cost Optimization Dashboard
- Compliance Monitoring

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more details.

---

# 👩‍💻 Author

**Himani Joshi**

B.Tech – Artificial Intelligence & Machine Learning

GitHub

https://github.com/himani-1211

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support helps improve the project and encourages future development.

---

<div align="center">

### ☁️ CloudSense AI

**Building Intelligent Cloud Operations, One Service at a Time.**

Built with ❤️ using **FastAPI**, **React**, **TypeScript**, **PostgreSQL**, **Docker**, and **AWS**.

</div>