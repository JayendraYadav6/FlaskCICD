    pipeline {
        agent any
        environment {
            IMAGE_NAME = "flask-app"
            CONTAINER_NAME = "flask-container"
        }
        stages {
            stage('Clone Repository') {
                steps {
                    git 'https://github.com/JayendraYadav6/FlaskCICD.git'
                }
            }
            stage('Build Docker Image') {
                steps {
                    script {
                        sh "docker build -t $IMAGE_NAME ."
                    }
                }
            }
            stage('Stop & Remove Old Container') {
                steps {
                    script {
                        sh """
                            docker stop $CONTAINER_NAME || true
                            docker rm $CONTAINER_NAME || true
                        """
                    }
                }
            }
            stage('Run New Container') {
                steps {
                    script {
                        sh "docker run -d -p 5002:5002 --name $CONTAINER_NAME $IMAGE_NAME"
                    }
                }
            }
        }
    }
