# Project-Management-System-API
This project is a Django-based REST API for managing clients and projects within an organization. It allows the registration of clients, addition of projects, and assignment of users to these projects. Here is how to set up and run the project, along with details about the endpoints and how to use them. 


# API Endpoints

# Users
Register a User (via Django Admin)
URL: /admin/
Method: GET
Description: Create a new user in the Django admin panel.

# Clients
## List All Clients

URL: /api/clients/
Method: GET
Description: Retrieve a list of all clients.

# Create a New Client

URL: /api/create/
Method: POST
Body:
json
Copy code
{
  "client_name": "Company A"
}
Description: Register a new client.

# Retrieve Client Information

URL: /api/clients/:id/
Method: GET
Description: Fetch information of a client, including projects assigned to its users.

# Update Client Information

URL: /api/clients/:id/
Method: PUT or PATCH
Body:
json
Copy code
{
  "client_name": "New Company Name"
}
Description: Update information of a client.


# Delete a Client

URL: /api/delete/:id/
Method: DELETE
Description: Delete a client's record.

# Projects
## Create a New Project for a Client
URL: /api/projects/:id/
Method: POST
Body:
json
Copy code
{
  "project_name": "Project A",
  "users": [{"id": 1}]
}
Description: Add a new project and assign users to it.

# List Projects Assigned to Logged-In User

URL: /api/projects/
Method: GET
Description: Retrieve all projects assigned to the logged-in user.
