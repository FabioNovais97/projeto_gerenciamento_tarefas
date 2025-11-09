from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/?title=Tarefa Teste&description=Descrição Teste")
    assert response.status_code == 200
    assert response.json()["title"] == "Tarefa Teste"

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
