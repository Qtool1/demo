pipeline {
    agent any
    environment{
        IMAGE = "https://jfrog.asux.aptiv.com/artifactory/docker/test_image/confluencetest:1"
    }

    stages 
    {
        stage('run')
        {
            steps 
            {
                sh 'docker run $(IMAGE)'
            }
        }
         stage('build')
        {
            steps 
            {
                sh 'python C:/Users/mjqy67/Documents/Python Scripts/confluencetest/DockerDemo.py'
            }
        }
    }
}
