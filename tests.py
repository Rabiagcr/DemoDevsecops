import json
from app import createapp_
def test_get_tasks():
    app=createapp_
    client=app.test_client()

    response=client.get('/tasks')
    assert response.status_code==200

def test_task():
    app=createapp_
    client=app.test_client() 
    response = client.post('/tasks', json={"title": "Test Görevi"})
    assert response.status_code == 201
    
