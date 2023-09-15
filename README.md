simple exchange api based on FasstAPI framework.

Build application

Build the Docker image manually by cloning the Git repo.

$ git clone https://github.com/AntonPopov90/exchange_api.git

$ docker build -t exchange_api .

Run the container
$  docker run -d -p 8000:8000 exchange_api

Visit http://localhost:8000
