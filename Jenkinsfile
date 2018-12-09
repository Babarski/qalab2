pipeline {
    agent {
        docker {
            image 'python:3.6-alpine'
        }
    }
    stages {
        stage('build') {

            steps {
                sh 'pip3 install --upgrade pip setuptools'
                sh 'apk add --update alpine-sdk make gcc && rm -rf /var/cache/apk/*'
                sh 'pip install -r configs/requirements.txt'
            }
        }
        stage('Test') {

            steps {
                sh 'python -m pytest --verbose --junit-xml test-reports/results.xml tests/lab2/utestsLab2.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}

