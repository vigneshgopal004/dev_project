pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t vignesh407/ssc:v1 .'
            }
        }
        stage('Run Container') {
            steps {
                script {
                    def containerName = "ssc-cloud-${BUILD_NUMBER}"
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

