pipeline {  
  agent any
  
  environment {
    registry = "lukxri/sentiment"
    registryCredential = 'docker-hub'
    dockerImage = ''
  } 
  stages {
    
    stage('Cloning Git') {
      steps {
        git 'https://github.com/lukxri/imdb_sentiment_BERT.git'
      }
    }
    
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    
    stage('Deploy Image') {
      steps{    script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
    
  }
}
