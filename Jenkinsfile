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
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${REGISTRY_CREDENTIALS}", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push ${DOCKER_IMAGE}
                    '''
                }
            }
        }

        stage('Run Flask Container') {
            steps {
                sh 'docker rm -f flaskapp || true'
                sh "docker run -d --name flaskapp -p 8080:5000 ${DOCKER_IMAGE}"
            }
        }
    }
}

