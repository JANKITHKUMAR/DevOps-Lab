#!/bin/bash
echo "Starting Jenkins container..."
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

echo "Waiting for Jenkins to generate admin password..."
sleep 15

echo "Jenkins initial admin password:"
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

echo "Access Jenkins at http://localhost:8080"
