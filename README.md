# Python_WebAPI
Create a hello world web application API that listens on port 8080 and greets a user with Hello! and exposes a health status endpoint.


How would you automate the build/test/deploy process for this application? (a verbal answer is enough. installation of CICD is bonus, not required)

a) What branching strategy would you use for development? - MASTER BRANCH

b) What CICD tool/service would you use? -
Source Code Management - GIT, GITHUB, CI Server - JENKINS (Build-Python(Virtualenv builder), Docker(docker file), CD - Either Ansible/Jenkins)

c) What stages would you have in the CICD pipeline? 

 1) Add the repository URL that contains the Python project, to the Source code management section
 2) Add a Build step, select Virtualenv builder and enter the following
	commands: pip install behave, pip install selenium
 3) Add a build step, select Python builder and enter the command: behave -i test.feature –junit
 4) optional step to move artifacts to artifactory/Nexus
 5) Add a post build activities and declare a deployment commands in deployment stage

d) What would be the purpose of each stage in CICD pipeline

A CI/CD pipeline helps you automate steps in your software delivery process, such as initiating code builds, running automated tests, and deploying to a staging or production environment. Automated pipelines remove manual errors, provide standardized development feedback loops and enable fast product iterations.

SCM stage   - Allows to clone the source code
Build stage - Used to build the source code
Test stage  - Used to perform testing for automated builds
Artifacts   - Move artifacts to binary repositories
