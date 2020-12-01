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
        checkout scm
      }
    }
   
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build(registry, "-f Dockerfile .")
        }
      }
    }
    
    stage("Testing") {
      steps {
        echo "Currently no tests available."
      }
    }
    
    stage('Deploy main Image') {
      when {
        anyOf {
          branch 'main'
        }
      }
      steps{    script {
        docker.withRegistry( '', registryCredential ) {
          dockerImage.push("$BUILD_NUMBER")
          dockerImage.push("latest")
          }
        }
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
    
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:latest"
      }
    }
    
  }
}
