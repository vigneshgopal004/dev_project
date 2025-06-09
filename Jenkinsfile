
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'vignesh407/ssc:v1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: 'dockerhub-ssc-v3', url: 'https://github.com/vigneshgopal004/dev_project.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker rm -f ssc-cloud-7 || true'
                    sh 'docker run -d -p 8081:5000 --name ssc-cloud-7 $DOCKER_IMAGE'
                }
            }
        }

        stage('Test App') {
            steps {
                sh 'sleep 5'
                sh 'curl -f http://localhost:8081 || exit 1'
            }
        }
    }
}
