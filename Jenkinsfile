pipeline {
    agent {
        node {
            label 'zOS_pyRACF'
        }
    }

    options {
        ansiColor('css')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh """
                    python3 --version
                    python3 -m pip install -r requirements.txt
                    python3 -m pip install -r requirements-development.txt
                """
            }
        }
        stage('Unit Test') {
            steps {
                sh """
                    flake8 .
                    pylint --recursive=y .
                    coverage run tests/test_runner.py
                    coverage report -m
                """
            }
        }
        stage('Smoke Test') {
            steps {
                sh """
                    python3 -m pip uninstall pyracf
                    python3 setup.py install
                    cd tests/function_test
                    python3 smoke_test.py
                """
            }
        }
        stage('Publish') {
            when { tag "*" }
            steps {
                sh "python3 setup.py bdist_wheel upload -r pypi"
            }
        }
    }
}