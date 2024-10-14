from flask import Blueprint, request, jsonify
from models import Task
from database import SessionLocal

task_routes = Blueprint("tasks", __name__)

db = SessionLocal()

@task_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"], is_completed=data.get("is_completed", False))
    db.add(new_task)
    db.commit()
    return jsonify({"id": new_task.id}), 201

@task_routes.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = db.query(Task).all()
    return jsonify({"tasks": [{"id": task.id, "title": task.title, "is_completed": task.is_completed} for task in tasks]}), 200

@task_routes.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = db.query(Task).filter(Task.id == id).first()
    if task:
        return jsonify({"id": task.id, "title": task.title, "is_completed": task.is_completed}), 200
    return jsonify({"error": "There is no task at that id"}), 404


@task_routes.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    task = db.query(Task).filter(Task.id == id).first()
    if task:
        if "title" in data:
            task.title = data["title"]
        if "is_completed" in data:
            task.is_completed = data["is_completed"]
        db.commit()
        return '', 204
    return jsonify({"error": "There is no task at that id"}), 404


@task_routes.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = db.query(Task).filter(Task.id == id).first()
    if task:
        db.delete(task)
        db.commit()
    return '', 204

# Bulk Add Tasks (Extra Credit)
@task_routes.route("/tasks", methods=["POST"])
def bulk_add_tasks():
    data = request.get_json()
    tasks = [Task(title=task_data["title"], is_completed=task_data.get("is_completed", False)) for task_data in data["tasks"]]
    db.add_all(tasks)
    db.commit()
    return jsonify({"tasks": [{"id": task.id} for task in tasks]}), 201

# Bulk Delete Tasks (Extra Credit)
@task_routes.route("/tasks", methods=["DELETE"])
def bulk_delete_tasks():
    data = request.get_json()
    task_ids = data["tasks"]
    db.query(Task).filter(Task.id.in_([task["id"] for task in task_ids])).delete(synchronize_session=False)
    db.commit()
    return '', 204
