pipeline {
    agent {
        label 'docker'
    }

    stages {
        stage('Source') {
            steps {
                git branch: 'main', url: 'https://github.com/alvarorg14/unir-cicd.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building stage!'

                sh 'make build'
            }
        }

        stage('Unit tests') {
            steps {
                sh 'make test-unit'

                archiveArtifacts artifacts: 'results/unit_result.xml', allowEmptyArchive: true
            }
        }

        stage('API tests') {
            steps {
                sh 'make test-api'

                archiveArtifacts artifacts: 'results/api_result.xml', allowEmptyArchive: true
            }
        }

        stage('E2E tests') {
            steps {
                sh 'make test-e2e'

                archiveArtifacts artifacts: 'results/cypress_result.xml', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            junit 'results/**/*.xml'

            cleanWs()
        }
    }
}
