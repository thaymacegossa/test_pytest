import requests

# test scenario 1: list all users
def test_list_all_users_successfully(base_url):
    response = requests.get(f"{base_url}/usuarios")
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert "quantidade" in response_data
    assert "usuarios" in response_data

# test scenario 2: get user by valid ID
def test_get_user_by_valid_id(base_url):
    list_response = requests.get(f"{base_url}/usuarios")
    user_list = list_response.json()["usuarios"]
    valid_id = user_list[0]["_id"]
    
    response = requests.get(f"{base_url}/usuarios/{valid_id}")
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data["_id"] == valid_id
    assert "nome" in response_data
    assert "email" in response_data

# test scenario 3: get user by invalid ID
# bug report: it should return a 404 not found, but it's returning a 400 bad request
def test_get_user_by_invalid_id(base_url):
    invalid_id = "00000000ABCDEFGH"
    
    response = requests.get(f"{base_url}/usuarios/{invalid_id}")
    
    assert response.status_code == 404
    assert response.json()["message"] == "Usuário não encontrado"
