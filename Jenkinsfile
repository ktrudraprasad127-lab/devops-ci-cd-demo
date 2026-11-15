
pipeline {
    agent any

    stages {
        stage('Welcome') {
            steps {
                echo 'Welcome to my DevOps CI/CD Pipeline!'
            }
        }

        stage('Checkout') {
            steps {
                echo 'Project source code is checked out from GitHub.'
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }
    }
}

