pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = 'dockerhub-credentials-v2'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/vigneshgopal004/dev_project.git', branch: 'main'
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t vignesh407/ssc:v1 .'
            }
        }
        stage('Run Container') {
            steps {
                script {
                    def containerName = "ssc_cloud_${BUILD_NUMBER}"
                    sh "docker run -d -p 8081:5000 --name ${containerName} vignesh407/ssc:v1"
                }
            }
        }
        stage('Test App') {
            steps {
                sh 'sleep 5'
                sh 'curl http://localhost:8081'
            }
        }
    }
}

