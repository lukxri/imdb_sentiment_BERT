pipeline {
  agent any
  stages {
    
    stage("build") {
      steps {
        echo "Building the application"
        script {
	  sh "docker build -t bert:api ."
	}
      }
    }
    
    stage("test") {
      steps {
        echo "Testing the application"
      }
    }
    stage("deploy") {
      steps {
        echo "Deploying the application"
      }
    }
  }
}
