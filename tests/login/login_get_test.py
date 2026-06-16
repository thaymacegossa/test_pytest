import uuid
import requests


def _create_user(base_url):
    suffix = uuid.uuid4().hex[:8]
    payload = {
        "nome": f"Login Test {suffix}",
        "email": f"login_test_{suffix}@example.com",
        "password": "teste123"
    }
    resp = requests.post(f"{base_url}/usuarios", json=payload)
    resp.raise_for_status()
    return payload["email"], payload["password"]


# test scenario 1: login with correct user and password
def test_login_with_correct_user_and_password(base_url):
    email, pwd = _create_user(base_url)

    response = requests.post(f"{base_url}/login", json={"email": email, "password": pwd})

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "message" in data
    assert data["message"]
    assert "authorization" in data or "token" in data or "senha" not in data


# test scenario 2: login with incorrect user and correct password
def test_login_with_incorrect_user_and_correct_password(base_url):
    wrong_email = f"no_such_user_{uuid.uuid4().hex[:8]}@example.com"
    pwd = "teste123"

    response = requests.post(f"{base_url}/login", json={"email": wrong_email, "password": pwd})

    assert response.status_code in (400, 401, 404)
    data = response.json()
    assert "message" in data


# test scenario 3: login with correct user and incorrect password
def test_login_with_correct_user_and_incorrect_password(base_url):
    email, pwd = _create_user(base_url)
    wrong_pwd = "senha_incorreta"

    response = requests.post(f"{base_url}/login", json={"email": email, "password": wrong_pwd})

    assert response.status_code in (400, 401)
    data = response.json()
    assert "message" in data


# test scenario 4: login with incorrect user and incorrect password
def test_login_with_incorrect_user_and_incorrect_password(base_url):
    wrong_email = f"no_such_user_{uuid.uuid4().hex[:8]}@example.com"
    wrong_pwd = "senha_incorreta"

    response = requests.post(f"{base_url}/login", json={"email": wrong_email, "password": wrong_pwd})

    assert response.status_code in (400, 401, 404)
    data = response.json()
    assert "message" in data


# test scenario 5: login with blank user and password
def test_login_with_blank_user_and_password(base_url):
    response = requests.post(f"{base_url}/login", json={"email": "", "password": ""})

    assert response.status_code in (400, 422)
    data = response.json()
    assert "message" in data