# to-do-list

## README

**FAST-API Backend with MySQL Database using docker compose**

This repository contains a simple FAST-API backend application connected to a MySQL database, both orchestrated using Docker Compose. The backend provides endpoints to perform basic CRUD operations on a 'todo' table in the database.

**Prerequisites**

- Docker installed on your machine

**Installation**

1.  Clone this repository to your local machine:

        git clone https://github.com/kafe-it/distributed-systems.git

**Usage (Only start backend)**

1.  Navigate to the project directory:

        cd fastapi-rest

2.  Start the application by running Docker Compose:

        docker compose up

The backend server will start on http://localhost:8000.

**Usage (Start backend and frontend)**

1.  Navigate to the project directory:

        cd sample/otel-in-action

2.  Start the application by running Docker Compose:

        docker compose --file .\docker-compose-fastapi.yaml up -d

The backend server will start on http://localhost:8000.

_NOTE:_ Startup of backend depends on mysqldb. therefore, startup takes some time.

**Endpoints**

1. GET /todos

- Description: Fetches all todo items from the database.
- Method: GET
- Response:
  - Status Code: 200 (OK)
  - Body: An array of todo texts

2. POST /todos/:todo

- Description: Adds a new todo item to the database.
- Method: POST
- Parameters:
  - todo: todo item to be added
- Response:
  - Status Code: 201 (Created)
  - Body: Confirmation message

3. DELETE /todos/:todo

- Description: Deletes a todo item from the database.
- Method: DELETE
- Parameters:
  - todo: todo item to be deleted
- Response:
  - Status Code: 200 (OK)
  - Body: Confirmation message

**Configuration**

The Docker Compose file (`docker-compose-fastapi.yml`) contains the configuration for both the fast api backend and the MySQL database containers. Ensure that the environment variables in the database service match your MySQL configuration needs.

**Error Handling**

- If an error occurs during any operation, the server will respond with a 500 (Internal Server Error) status code along with an error message.

**Kubernetes**

Ensure kubectl and minikube/kind are installed.

Run:

        minikube start
        kubectl apply -f sample/otel-in-action/deployment.yaml

Now you can observe the deployments (mysql and fastapi should be running):

        kubectl get deployments
