pipeline {
  agent {
    docker { image "node:14-alpine" }
  }
  stages {
    
    stage("build") {
      steps {
        echo "Building the application!"
      }
    }
    
    stage("test") {
      steps {
        echo "Testing the application"
        sh "node --version"
      }
    }
    stage("deploy") {
      steps {
        echo "Deploying the application"
      }
    }
  }
}
