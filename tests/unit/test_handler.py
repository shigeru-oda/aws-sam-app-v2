from fastapi.testclient import TestClient
from hello_world.app import app as hello_world_app
from item.app import app as item_app

hello_world_client = TestClient(hello_world_app)
item_client = TestClient(item_app)

def test_root():
    response = hello_world_client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello SAM World"}

def test_read_item():
    response = item_client.get("/item?item_id=1")
    assert response.status_code == 200
    assert response.json() == {"1": {"name": "name-0001","description":"desc-0001","price":10.0}}
    
def test_read_item_error():
    response = item_client.get("/item?item_id=6")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
    
def test_create_item():
    response = item_client.post(
        "/item/9",
        json={"name": "name-0009","description":"desc-0009","price":90.0}
    )
    assert response.status_code == 201
    assert response.json() =={"9": {"name": "name-0009","description":"desc-0009","price":90.0}}