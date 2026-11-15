
# End-to-End DevOps CI/CD Pipeline Project

## Project Overview
This project demonstrates an automated CI/CD pipeline for a Python Flask application using Jenkins, GitHub, Docker, and pytest.

Whenever code is pushed to GitHub, Jenkins retrieves the source code, installs dependencies, executes automated tests, builds a Docker image, and deploys the application inside a Docker container.

## Technologies Used
- Linux (Ubuntu WSL)
- Python
- Flask
- Git and GitHub
- Jenkins
- Docker
- Pytest
- CI/CD Pipeline

## Project Architecture

Developer → GitHub → Jenkins → Install Dependencies → Run Tests → Build Docker Image → Deploy Container → Flask Application

## Project Structure

```text
devproject/
├── healthapp.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
├── .gitignore
└── tests/
    └── test_app.py
```

## CI/CD Pipeline Stages

1. **Checkout:** Jenkins retrieves source code from GitHub.
2. **Install Dependencies:** Installs Python packages using requirements.txt.
3. **Run Tests:** Executes automated tests using pytest.
4. **Build Docker Image:** Creates a Docker image of the Flask application.
5. **Deploy Application:** Runs the application inside a Docker container.

## Application URLs

Main application:
http://localhost:5000

Health check:
http://localhost:5000/health

## Useful Docker Commands

```bash
docker ps
docker images
docker logs healthapp
docker stop healthapp
docker start healthapp
```

## Project Outcome

Successfully implemented an end-to-end CI/CD pipeline that automates source code checkout, dependency installation, testing, Docker image creation, and application deployment using Jenkins.
