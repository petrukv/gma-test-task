# gma-test-task
Instructions for Running the Project
Here are the steps to run the project, including the instructions for setting up the environment and running the application.

1. Clone the Repository
First, clone the repository from GitHub:
git clone https://github.com/petrukv/gma-test-task.git

2. Create and Configure the .env File
Here's an example of what your .env file should look like:
DB_NAME=gma
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=db
DB_PORT=5432

3. Build and Run the Docker Containers
Use Docker Compose to build and run the containers:

docker-compose up --build

4. Access the Application
The application should now be running and accessible at http://localhost:8080


API Documentation
The API provides endpoints for managing locations, users, and devices. Here are the details of the available endpoints:

1. Location Endpoints
   
Create Location

Endpoint: POST /locations
Request Body:
{
  "name": "Location Name"
}
Response:
{
  "id": 1
}

Get Location

Endpoint: GET /locations/{location_id}
Response:
{
  "id": 1,
  "name": "Location Name"
}

2. User Endpoints
   
Create User

Endpoint: POST /users
Request Body:

{
  "name": "User Name",
  "email": "user@example.com",
  "password": "password"
}
Response:
{
  "id": 1
}

Get User

Endpoint: GET /users/{user_id}
Response:
{
  "id": 1,
  "name": "User Name",
  "email": "user@example.com"
}

3. Device Endpoints
   
Create Device

Endpoint: POST /devices
Request Body:
{
  "name": "Device Name",
  "type": "Device Type",
  "login": "login",
  "password": "password",
  "location_id": 1,
  "api_user_id": 1
}
Response:
{
  "id": 1
}

Get Device

Endpoint: GET /devices/{device_id}
Response:
{
  "id": 1,
  "name": "Device Name",
  "type": "Device Type",
  "login": "login",
  "password": "password",
  "location_id": 1,
  "api_user_id": 1
}

Update Device

Endpoint: PUT /devices/{device_id}
Request Body:
{
  "name": "Updated Device Name",
  "type": "Updated Device Type",
  "login": "updated_login",
  "password": "updated_password"
}
Response:
{
  "status": "success"
}

Delete Device

Endpoint: DELETE /devices/{device_id}
Response:
{
  "status": "success"
}
