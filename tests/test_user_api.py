import pytest
from utils.api_client import * 
import  uuid

@pytest.fixture(scope="module")
def api_client():
    return ApIclient()

def test_get_task(api_client):
    # endpoint = 7599266  # replace with actual endpoint ID you want to test
    response = api_client.get_task("users")
    print(response)
    print(response.json())
    assert response.status_code == 200
    
def unique_emials():
     unique_id = uuid.uuid4().hex[:8]  # Shorten UUID to 8 characters for simplicity
     unique_emials= f"user_{unique_id}@example.com"
     return unique_emials
    
def test_post_task(api_client, load_user_data):
    
    user_data = load_user_data  # Fixture provides the dictionary from test_data.json
    user_payload = user_data["user_payload"]
    # user_payload = load_user_data[user_payload]
    user_payload["email"] = unique_emials() 
    response = api_client.create_task("users",user_payload)
    print(response)
    print(response.json())
    assert response.status_code == 201
    global data
    data = response.json()
    
def test_update_task (api_client, load_user_data):
    user_id = data["id"]
     #  Update task
    # updated_payload = { 
    #     'name': 'Ram', 
    #     'email': unique_emials(),
    #     "gender":"female"
    #     }
    user_data = load_user_data  # Fixture provides the dictionary from test_data.json
    updated_payload = user_data["updated_payload"]
    updated_payload["email"] = unique_emials() 
    response = api_client.update_task("users", user_id, updated_payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == updated_payload["name"]
    
def test_delete_task (api_client):
    user_id = data["id"]
    response = api_client.delete_task("users", user_id)
    print(response.status_code)
    assert response.status_code == 204
    
    
    