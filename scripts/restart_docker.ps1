# Stop and remove the Alice container if it exists
if (docker ps -a --format '{{.Names}}' | Select-String -Pattern '^alice$') {
    docker stop alice
    docker rm alice
}

# Stop and remove the Bob container if it exists
if (docker ps -a --format '{{.Names}}' | Select-String -Pattern '^bob$') {
    docker stop bob
    docker rm bob
}

# Build and run the Alice container
docker build -t alice .\alice\
docker run -d --name alice -p 5000:5000 alice

# Build and run the Bob container
docker build -t bob .\bob\
docker run -d --name bob -p 5001:5001 -e PORT=5000 -e IP="192.168.1.4" bob
