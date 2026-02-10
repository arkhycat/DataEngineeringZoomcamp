# List all containers
docker ps -a
# List all images
docker images
# List volumes
docker volume ls
# List networks
docker network ls


# Stop All Running Containers
docker-compose down
# Remove Containers
docker container prune
# Remove all unused images
docker image prune -a
# Remove specific volumes
docker volume rm ny_taxi_postgres_data
docker volume rm pgadmin_data
# Remove all unused volumes
docker volume prune
# Remove specific network
docker network rm pg-network
# Remove all unused networks
docker network prune


# List all containers
docker ps -a
# List all images
docker images
# List volumes
docker volume ls
# List networks
docker network ls
