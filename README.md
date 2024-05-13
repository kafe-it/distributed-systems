# to-do-list

## README

**FAST-API Backend with MySQL Database using docker compose**

This repository contains a simple FAST-API backend application connected to a MySQL database, both orchestrated using Docker Compose. The backend provides endpoints to perform basic CRUD operations on a 'todo' table in the database.

**Prerequisites**

* Docker installed on your machine

**Installation**

1. Clone this repository to your local machine:

        git clone https://github.com/kafe-it/distributed-systems.git

2. Navigate to the project directory:

        cd fastapi-rest

**Usage**

1. Start the application by running Docker Compose:

        docker compose up

The backend server will start on http://localhost:8000.

*NOTE:* Startup of backend depends on mysqldb. therefore, startup takes some time.

**Endpoints**

1. GET /todos

  * Description: Fetches all todo items from the database.
  * Method: GET
  * Response:
    * Status Code: 200 (OK)
    * Body: An array of todo texts
       
2. POST /todos/:todo_name

  * Description: Adds a new todo item to the database.
  * Method: POST
  * Parameters:
    * todo_name: The text of the todo item
  * Response:
    * Status Code: 201 (Created)
    * Body: Confirmation message
   
3. DELETE /todos/:todo_name

  * Description: Deletes a todo item from the database.
  * Method: DELETE
  * Parameters:
    * todo_name: The text of the todo item to be deleted
  * Response:
    * Status Code: 200 (OK)
    * Body: Confirmation message



**Configuration**

The Docker Compose file (```docker-compose.yml```) contains the configuration for both the backend and the PostgreSQL database containers. Ensure that the environment variables in the database service match your PostgreSQL configuration needs.

**Error Handling**

* If an error occurs during any operation, the server will respond with a 500 (Internal Server Error) status code along with an error message.
