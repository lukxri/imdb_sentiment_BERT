pipeline {
    agent none
    stages {
        stage('Back-end1') {
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
        stage('Front-end2') {
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
