pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                docker { 
                    image 'maven:3-alpine' 
                    label "docker"
                }
                
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                docker { 
                    image 'node:14-alpine' 
                    label "docker"
                }
            }
            steps {
                sh 'node --version'
            }
        }
    }
}
