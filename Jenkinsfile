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
                echo 'Source code retrieved from GitHub.'
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

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t healthapp:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f healthapp || true
                    docker run -d \
                        --name healthapp \
                        -p 5000:5000 \
                        --restart unless-stopped \
                        healthapp:${BUILD_NUMBER}
                '''
            }
        }
    }
}

