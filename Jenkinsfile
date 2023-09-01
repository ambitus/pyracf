pipeline {
    agent {
        node {
            label 'zOS_pyRACF'
        }
    }

    parameters {
        booleanParam(
            name: "createRelease",
            defaultValue: false,
            description: "Toggle whether or not to create a release from this revision."
        )
        string(
            name: "releaseTag",
            defaultValue: "",
            description: "When creating a new release, this will be the git tag and version number of the release."
        )
        string(
            name: "gitHubMilestoneLink",
            defaultValue: "",
            description: "When creating a new release, this is the GitHub Milestore URL that coresponds to the release."
        )
        booleanParam(
            name: "preRelease",
            defaultValue: true,
            description: "Toggle whether or not this is a pre-release."
        )
    }

    options {
        ansiColor('css')
    }

    environment {
        OS = sh(
            returnStdout: true, 
            script: "uname"
        ).trim().replace("/", "")
        RELEASE = sh(
            returnStdout: true, 
            script: "uname -r"
        ).trim().replace(".", "_")
        PROCESSOR = sh(
            returnStdout: true, 
            script: "uname -m"
        ).trim()
        PYRACF_VERSION = sh(
            returnStdout: true, 
            script: "cat pyproject.toml | grep version | cut -d'=' -f2 | cut -d'\"' -f2"
        ).trim()

        PYHTON_310 = "python3.10"
        PYTHON_310_WHEEL = "pyRACF-${env.PYRACF_VERSION}-cp310-cp310-${env.OS}_${env.RELEASE}_${env.PROCESSOR}.whl"
        PYTHON_311 = "python3.11"
        PYTHON_311_WHEEL = "pyRACF-${env.PYRACF_VERSION}-cp311-cp311-${env.OS}_${env.RELEASE}_${env.PROCESSOR}.whl"
    }

    stages {
        stage('Parameter Validation') {
            steps {
                script {
                    if (params.createRelease) {
                        if (params.releaseTag == "") {
                            error("'releaseTag' is required when creating a release.")
                        }
                        if (params.gitHubMilestoneLink) {
                            error("'gitHubMilestoneLink' is required when creating a release.")
                        }
                    }
                }
            }
        }
        stage('Build Virtual Environment v3.11') {
            steps {
                build_virtual_environment(env.PYTHON_311)
            }
        }
        stage('Lint & Unit Test Python v3.11') {
            steps {
                lint_and_unit_test(env.PYTHON_311)
            }
        }
        stage('Function Test Python v3.11') {
            steps {
                function_test(env.PYTHON_311, env.PYTHON_311_WHEEL)
            }
        }
        stage('Publish') {
            when { 
                expression { params.createRelease == true }    
            }
            steps {
                publish(
                    env.PYTHON_310,
                    params.releaseTag, 
                    env.BRANCH_NAME, 
                    params.gitHubMilestoneLink,
                    params.preRelease,
                    env.PYTHON_311_WHEEL
                )
            }
        }
    }
}

def build_virtual_environment(python) {
    sh """
        ${python} --version
        rm -rf venv_${python}
        ${python} -m venv venv_${python}
        . venv_${python}/bin/activate
        ${python} -m pip install -r requirements.txt
        ${python} -m pip install -r requirements-development.txt
    """
}

def lint_and_unit_test(python) {
    sh """
        . venv_${python}/bin/activate
        ${python} -m flake8 . --exclude venv_*
        ${python} -m pylint --recursive=y --ignore-patterns venv_* .
        ${python} -m coverage run tests/test_runner.py
        ${python} -m coverage report -m
    """
}

def function_test(python, wheel) {
    sh """
        git clean -f -d -e venv_*
        . venv_${python}/bin/activate
        ${python} -m pip wheel .
        ${python} -m pip install ${wheel}
        cd tests/function_test
        ${python} function_test.py
    """
}

def publish(
        python, 
        release, 
        git_branch, 
        milestone, 
        pre_release, 
        wheel
) {
    if (pre_release == true) {
        pre_release = "true"
    }
    else {
        pre_release = "false"
    }
    withCredentials(
        [
            string(
                credentialsId: 'pyracf-github-access-token',
                variable: 'github_access_token'
            ),
            string(
                credentialsId: 'pyracf-pypi-username',
                variable: 'pypi_username'
            ),
            string(
                credentialsId: 'pyracf-pypi-password',
                variable: 'pypi_password'
            )
        ]
    ) {
        // Creating GitHub releases: https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#create-a-release
        // Uploading release assets: https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#upload-a-release-asset

        // Use single quotes for access token since it is the most secure
        // method for interpolating secrets according to the Jenkins docs:
        // https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#string-interpolation

        echo "Creating ${release} GitHub release..."

        def release_id = sh(
            returnStdout: true,
            script: (
                'curl -L \\'
                + '-X POST \\'
                + '-H "Accept: application/vnd.github+json" \\'
                + '-H "Authorization: Bearer ${github_access_token}" \\'
                + '-H "X-GitHub-Api-Version: 2022-11-28" \\'
                + 'https://api.github.com/repos/ambitus/pyracf/releases \\'
                + "-d '{"
                + "     \"tag_name\": \"${release}\","
                + "     \"target_commitish\": \"${git_branch}\","
                + "     \"name\": \"${release}\","
                + "     \"body\": \"Release Milestone: ${milestone}\","
                + "     \"draft\": false,"
                + "     \"prerelease\": ${pre_release},"
                + "     \"generate_release_notes\":false"
                + "}' | grep '\"id\": ' | head -n1 | cut -d':' -f2 | cut -d',' -f1"
            ).trim()
        )

        echo "Cleaning repo and building ${wheel}..."

        sh """
            git clean -f -d -e venv_*
            . venv_${python}/bin/activate
            ${python} -m pip wheel .
        """

        echo "Uploading ${wheel} as an asset to ${release} GitHub release..."

        sh(
            'curl -L \\'
            + '-X POST \\'
            + '-H "Accept: application/vnd.github+json" \\'
            + '-H "Authorization: Bearer ${github_access_token}" \\'
            + '-H "X-GitHub-Api-Version: 2022-11-28" \\'
            + '-H "Content-Type: application/octet-stream" \\'
            + "\"https://uploads.github.com/repos/ambitus/pyracf/releases/${release_id}/assets?name=${wheel}\" \\"
            + "--data-binary \"@${wheel}\""
        )

        sh(
            ". venv_${python}/bin/activate && "
            + "${python} -m twine upload --repository test ${wheel} " 
            + '-u ${pypi_username} -p ${pypi_password}'
        )
    }
}
