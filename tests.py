import requests

BASE_URL = "http://localhost:5000/v1"

def test_create_task():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": "Test Task 1"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_list_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert isinstance(response.json()["tasks"], list)

def test_get_task():
    response = requests.get(f"{BASE_URL}/tasks/1")
    assert response.status_code == 200
    assert "id" in response.json()

def test_update_task():
    response = requests.put(f"{BASE_URL}/tasks/1", json={"title": "Updated Task", "is_completed": True})
    assert response.status_code == 204

def test_delete_task():
    response = requests.delete(f"{BASE_URL}/tasks/1")
    assert response.status_code == 204

def test_bulk_add_tasks():
    response = requests.post(f"{BASE_URL}/tasks", json={
        "tasks": [
            {"title": "Bulk Task 1", "is_completed": False},
            {"title": "Bulk Task 2", "is_completed": True}
        ]
    })
    assert response.status_code == 201
    assert "tasks" in response.json()

def test_bulk_delete_tasks():
    response = requests.delete(f"{BASE_URL}/tasks", json={
        "tasks": [
            {"id": 1},
            {"id": 2}
        ]
    })
    assert response.status_code == 204
