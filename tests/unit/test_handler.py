from fastapi.testclient import TestClient
from hello_world.app import app as hello_world_app
from item.app import app as item_app
import json

hello_world_client = TestClient(hello_world_app)
item_client = TestClient(item_app)

def test_root():
    response = hello_world_client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello SAM World"}

def test_get_item():
    response = item_client.get("/item?id=ABC")
    assert response.status_code == 200
    assert response.json() == {"id": "ABC", "name": "read_item+ABC","description":"read_item+ABC","price":100.0}

def test_post_item():
    response = item_client.post(
        "/item",
        json={"name": "name-0009","description":"desc-0009","price":90.0}
    )
    del_id_res = response.json()
    del del_id_res["id"]
    assert response.status_code == 201
    assert del_id_res =={"name": "name-0009","description":"desc-0009","price":90.0}

def test_put_item():
    response = item_client.put(
        "/item/9"
    )
    assert response.status_code == 201
    assert response.json() =={"id": "9", "name": "update_item+9","description":"update_item+9","price":200.0}
