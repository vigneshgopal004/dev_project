pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vignesh407/ssc:v1"
        REGISTRY = "docker.io"
        REGISTRY_CREDENTIALS = "dockerhub-credentials"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vigneshgopal004/dev_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("https://${REGISTRY}", REGISTRY_CREDENTIALS) {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('Run Flask Container') {
            steps {
                script {
                    sh 'docker rm -f flaskapp || true'
                    sh 'docker run -d --name flaskapp -p 8080:5000 ${DOCKER_IMAGE}'
                }
            }
        }
    }
}

