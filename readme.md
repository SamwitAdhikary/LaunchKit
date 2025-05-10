# LaunchKit

**LaunchKit** is a modern, framework-agonistic Platform-as-a-Service (PaaS) that makes deploying any application to the cloud as easy as running a single command. Whether you're building in Django, Node.js, Go, Rust, or a static site, LaunchKit handles everything - from project initialization through deployment, scaling, custom domains, SSL, monitoring, and team collaboration - so you can focus on writing code, not provisioning servers.

---

## 🚀 Why LaunchKit?

### 1. One CLI to Rule Them All

Automate every setp with the `launchkit` command:

```bash
launchkit init       # Scaffold your project
launchkit deploy     # Build, push, and release
launchkit env list   # Manage environments
launchkit domain add # Provision SSL and DNS
launchkit logs       # Stream real-time logs
launchkit rollback   # Instantly roll back release
```
---

### 2. Universal Framework Support
Out-of-the-box detection for Django, Rails, Node.js, React, Veu, Go, Rust, static sites, and more coming every sprint.

### 3. Rich Web Dashboard
Visualize your applications, inspect logs & metrics, manage domains, and collaborate with your team in beautiful React interface.

### 4. Self-Hosted, Open & Extensible
Full source code for CLI, API server, dashboard, and IaC (CDK/Terraform). Fork it, extend it, or integrate it into your enterprise toolchain.

### 5. Infrastructure as Code
AWS CDK (TypeScript) stacks and Terraform modules for VPC, RDS, ECS/Fargate, S3, CloudFront, and Route 53 - ready to customize.

### 6. Built-in CI/CD & Migrations
Alembic migrations for your database, real-time deployment logs, zero-downtime releases, and instant rollbacks.

---

## 🔧 Tech Stack

| Component | Technology |
| -------- | ------- |
| CLI | Python, Typer, HTTPX, Keyring |
| Backend | FastAPI, SQLAlchemy, Alembic, PostgreSQL, Redis, Pydantic |
| Frontend | React, TypeScript, Vite, Axios |
| Infra | AWS CDK (TypeScript), Terraform (HCL) |
| Container | Docker, Docker Compose |

---

## 📁 Repository Structure

```bash
launchkit/
├── cli/                # Typer-based CLI tool
├── backend/            # FastAPI API server & database migrations
├── frontend/           # React + Vite web dashboard
└── infrastructure/     # AWS CDK & Terraform IaC
```
Each component is self-contained, with its own tests, and configurations.

---

## 🏁 Getting Started
### Prerequisites
- Git
- Docker & Docker Compose
- Python 3.10+
- Node.js 16+

---

## 1️⃣ Local Development Setup

```bash
# Clone the repo
git clone https://github.com/your-org/launchkit.git
cd launchkit
```

- CLI
```bash
cd cli
pip install -e .
launchkit --help
```

- Backend
```bash
cd backend
# Copy example env and install
cp .env.example .env
pip install -r requirements.txt

# Start dependencies
docker-compose up -d postgres redis

# Run migrations
docker-compose exec backend alembic upgrade head

# Launch the API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Frontend
```bash
cd frontend
# Copy example env and install
cp .env.example .env
npm install

# Start dev server
npm run dev
```

Your Dashboard is now available at [http://localhost:3000](http://localhost:3000) and the API at [http://localhost:8000](http://localhost:8000)

---

## 📚 Features Overview
### CLI Commands

| Command | Description |
| -------- | ------- |
| `launchkit init` | Auto-detect your project and scaffold configs |
| `launchkit login` | Authenticate and store your access token |
| `launchkit deploy` | Build, push, and release your app |
| `launchkit logs` | Stream real-time application logs |
| `launchkit rollback` | Roll back to a previous release |

### Backend API Endpoints

- **Health & Status**: `GET /api/v1/health`
- **Authentication**:
    - `POST /api/v1/auth/register`
    - `POST /api/v1/auth/login`
- **(Coming Soon)** Apps, Deployment, Environments, Domains, Metrics, Team Management

### Web Dashboard Highlights
- **Loing & Registration flows**
- **Dashboard Overview**: app statuses, recent deployments, resource metrics
- **Protected Routes**: only accessible when authenticated
- **Responsive UI** for all devices

---

## 🔍 Testing
```bash
# CLI tests
cd cli
pytest

# Backend tests
cd backend
pytest --cov=app

# Frontend tests
cd frontend
npm run test
```

---

## 🤝 Contributing
We welcome all contributions! To get started:
1. **Fork** the repo and create a feature branch
2. **Write** tests and follow existing code style
3. **Submit** a pull request with a clear description of your changes
4. **Ensure** all CI checks (lint, tests) pass.

<p align="center"> <em>LaunchKit — Deploy anything, effortlessly.</em> </p>