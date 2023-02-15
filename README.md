# TODO List Application
This is a backend application for a TODO list, implemented in Python using Flask and SQLite database.<br>

## Prerequisites
<ul>
  <li>Python 3.6 or higher</li>
  <li>Flask and Flask-SQLAlchemy</li>
</ul>

## Installation
<ul >
  <li type="1">Clone the repository: `https://github.com/prathameshpatil2002/Todo-List-Application-using-Flask`</li>
  <li type="1">Change into the project directory : cd Todo-List-Application-using-Flask</li>
  <li type="1">Install the dependencies : pip install -r requirements.txt</li>
</ul>

## Running the Application
To start the server, run the following command: <br>
```
python app.py
```
By default, the application will run on http://localhost:5000

# API Endpoints

The following API endpoints are available:

1. **GET /tasks** - Get a list of all tasks<br><br>
2. **POST /tasks** - Create a new task<br><br>
3. **PUT /tasks/:id** - Update a task<br><br>
4. **DELETE /tasks/:id** - Delete a task<br><br>
5. **PUT /tasks/:id/completed** - Mark a task as completed<br><br>
6. **PUT /tasks/:id/incomplete** - Mark a task as incomplete<br><br>

## Example Usage

To create a new task, make a **POST** request to **http://localhost:5000/tasks** with the following JSON payload:<br>
```
{
    "title": "Buy Groceries",
    "description": "Milk, Bread, Eggs"
}
```
To get a list of all tasks, make a **GET** request to **http://localhost:5000/tasks**.<br>

To update a task, make a **PUT** request to **http://localhost:5000/tasks/:id** with the following JSON payload:<br>
```
{
    "title": "Buy Groceries",
    "description": "Milk, Bread, Eggs, Cheese"
}
```
To delete a task, make a **DELETE** request to **http://localhost:5000/tasks/:id**.<br>

To mark a task as completed, make a **PUT** request to **http://localhost:5000/tasks/:id/completed**.<br>

To mark a task as incomplete, make a **PUT** request to **http://localhost:5000/tasks/:id/incomplete**.<br>

# Conclusion
This is a simple TODO list application, but it can be extended in various ways, such as adding user authentication, due dates, and more. Feel free to modify and improve this application to fit your needs!
