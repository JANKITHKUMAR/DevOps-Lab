#!/bin/bash
# 1. Create a bridge network
docker network create --driver bridge my-bridge-net

# 2. Build Flask API
docker build -t flask-api .

# 3. Run MySQL, Redis, and Flask on the custom network
docker run -d --name mysql --net=my-bridge-net -e MYSQL_ROOT_PASSWORD=secret mysql:latest
docker run -d --name redis --net=my-bridge-net redis:latest
docker run -d --name flask --net=my-bridge-net -p 5001:5001 flask-api

# 4. Test connectivity
docker exec -it flask ping -c 3 mysql
docker exec -it flask ping -c 3 redis

# 5. Clean up
docker stop mysql redis flask && docker rm mysql redis flask
docker network rm my-bridge-net
