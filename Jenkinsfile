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
            // Publish test results
            junit testResults: 'results/*.xml', allowEmptyResults: true
            
            // Clean workspace
            cleanWs()
        }
        failure {
            emailext (
                subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                body: """
                    Pipeline failed!
                    
                    Job: ${env.JOB_NAME}
                    Build Number: ${env.BUILD_NUMBER}
                    Build URL: ${env.BUILD_URL}
                    Failed Stage: ${currentBuild.currentResult}
                    
                    Please check the Jenkins console output for more details.
                """,
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
}
