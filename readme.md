# LaunchKit

**LaunchKit** is a Platform-as-a-Service (PaaS) that lets you deploy backend, frontend, and full-stack apps on AWS with a unified CLI, API server, and web dashboard.

## 🚀 Quickstart

### Prerequisites

- Docker & Docker Compose  
- Node.js (v18+) & npm  
- Python (v3.10+) & Poetry or pip

### 1. Clone & bootstrap

```bash
git clone https://github.com/your-org/launchkit.git
cd launchkit
```

### 2. Copy your env

```bash
cp .env.example .env
# Edit .env to set DATABASE_URL, REDIS_URL, VITE_API_URL, SECRET_KEY, etc.
```

### 3. Spin up services

```bash
docker-compose up -d
```

Visit http://localhost:3000 to see the dashboard.

### 4. Running the CLI locally

```bash
cd cli
poetry install        # or pip install -e
launchkit hello world # -> Hello, LaunchKit!
```

### Repo Structure
```bash
.
├── cli/                 # Typer-based CLI
├── backend/             # FastAPI service
├── frontend/            # React+TypeScript dashboard
├── infrastructure/      # CDK & Terraform stubs
├── .env.example         # sample env vars
├── docker-compose.yml   # local dev orchestration
├── .gitignore
├── LICENSE
└── README.md
```