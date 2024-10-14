# Waterdip-AI-Backend-Assignment
Task Management Server

This project implements a backend server to manage tasks with CRUD operations and bulk processing capabilities.

Features
1. Create a New Task
  Endpoint: POST /tasks
  Description: Create a new task with a unique ID, title, and completion status.
2. List All Tasks
  Endpoint: GET /tasks
  Description: Retrieve a list of all tasks with their IDs, titles, and completion statuses.
3. Get a Specific Task
  Endpoint: GET /tasks/{id}
  Description: Retrieve the details of a specific task by its unique ID.
4. Delete a Specific Task
  Endpoint: DELETE /tasks/{id}
  Description: Delete a task by its unique ID.
5. Edit a Specific Task
  Endpoint: PUT /tasks/{id}
  Description: Edit the title and/or completion status of an existing task.
6. (Extra Credit) Bulk Add Multiple Tasks
  Endpoint: POST /tasks/bulk
  Description: Add multiple tasks in a single request.
7. (Extra Credit) Bulk Delete Multiple Tasks
  Endpoint: DELETE /tasks/bulk
  Description: Delete multiple tasks by providing an array of task IDs in one request.
