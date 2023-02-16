from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite Configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Task model

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Task({self.id}, "{self.title}", {self.completed})'


# API for Retriving all tasks

@app.route('/')
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    result = []
    for task in tasks:
        result.append({'id': task.id, 'title': task.title,
                      'description': task.description, 'completed': task.completed})
    return jsonify(result)


# API for creating Task


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully!', 'task': {'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'completed': new_task.completed}})


# API for updating Task

@app.route('/tasks/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully!', 'task': {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}})


# API for deleting Task

@app.route('/tasks/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully!', 'task': {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}})


# API for marking Task Complete

@app.route('/tasks/complete/<int:task_id>')
def mark_task_completed(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    task.completed = True
    db.session.commit()
    return jsonify({'message': 'Task marked as completed!', 'task': {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}})


# API for marking Task incomplete

@app.route('/tasks/incomplete/<int:task_id>')
def mark_task_incomplete(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    task.completed = False
    db.session.commit()
    return jsonify({'message': 'Task marked'})


# Running App

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
