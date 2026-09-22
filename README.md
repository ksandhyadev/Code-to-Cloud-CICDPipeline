# Production-Ready Code-to-Cloud Automated CI/CD Pipeline

A fully automated, production-grade DevOps CI/CD pipeline built with **Python Flask**, **Docker**, **GitHub Actions**, and **AWS EC2**.

![Architecture Flow](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?logo=githubactions)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)
![AWS EC2](https://img.shields.io/badge/Cloud-AWS%20EC2-FF9900?logo=amazonec2)
![Python](https://img.shields.io/badge/Application-Flask-000000?logo=flask)

---

## 🏗️ Architecture Overview

```mermaid
flowchart LR
    A[Developer Git Push to main] --> B[GitHub Actions CI/CD]
    subgraph GitHub Actions Runner
        B --> C[Build Docker Image]
        C --> D[Push Image with Tags to Docker Hub]
    end
    D --> E[Docker Hub Registry]
    B --> F[SSH to AWS EC2 via Secrets]
    subgraph AWS EC2 Ubuntu Instance
        F --> G[Pull Latest Image from Docker Hub]
        G --> H[Gracefully Stop/Remove Existing Container]
        H --> I[Run New Container on Port 5000]
        I --> J[Prune Dangling Images]
    end
    K[End User / Browser] -->|HTTP :5000| I
```

---

## 📁 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # Automated CI/CD Pipeline (Build, Push & SSH Deploy)
├── .dockerignore               # Optimizes build context & prevents credential leaks
├── .gitignore                  # Prevents committing sensitive files & virtualenvs
├── Dockerfile                  # Multi-stage/security-hardened slim container image
├── app.py                      # Flask Application with / and /health endpoints
├── requirements.txt            # Python dependencies (Flask, Gunicorn)
└── README.md                   # Complete architectural and setup guide
```

---

## 🔒 Security Best Practices Implemented

1. **Non-Root Container User**: Runs under `appuser` (UID 10001) instead of `root`.
2. **Minimal Attack Surface**: Uses `python:3.11-slim` with `--no-cache-dir`.
3. **Docker Layer Caching**: Separates dependency installation from source code copying.
4. **Secrets Management**: Credentials (Docker Hub token, SSH private key) are managed strictly via GitHub Encrypted Secrets.
5. **Disk Hygiene**: Automated pruning of dangling images (`docker image prune -f`) on EC2 prevents disk full outages.
6. **Container Healthcheck**: Configured native `/health` check in Dockerfile.

---

## 🚀 Step-by-Step Deployment Guide

See the walkthrough guide for the complete checklist to configure AWS EC2, GitHub Secrets, and run the pipeline live today.
