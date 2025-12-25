# 🌆 Urban Heat Island Predictor (End-to-End MLOps)

[![MLOps CI Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/mlops-ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)
![MLflow](https://img.shields.io/badge/mlflow-tracked-orange.svg)

## 📌 Project Overview
This project predicts micro-temperature increases in urban environments. It is a complete MLOps implementation focusing on **experiment reproducibility**, **data versioning**, and **automated delivery**.

## 🏗️ System Architecture
```mermaid
graph TD
    subgraph "Data & Versioning"
        A[urban_heat_data.csv] -->|Tracked by| B(DVC)
    end

    subgraph "Training Pipeline"
        C[train.py] -->|Reads| A
        C -->|Logs Metrics/Params| D{MLflow}
        C -->|Produces| E[urban_heat_model.pkl]
    end

    subgraph "CI/CD (GitHub Actions)"
        F[Push Code] --> G[Run Pytest]
        G --> H[Build Docker Image]
    end

    subgraph "Deployment"
        E -->|Loaded by| I[app.py - Flask API]
        H -->|Containerizes| I
        I --> J[Predict: JSON Output]
    end