import uuid
import requests


def create_test_user(base_url):
    suffix = uuid.uuid4().hex[:8]
    payload = {
        "nome": f"Test User {suffix}",
        "email": f"test_user_{suffix}@example.com",
        "password": "teste123",
        "administrador": "true"
    }
    resp = requests.post(f"{base_url}/usuarios", json=payload)
    resp.raise_for_status()
    return payload["email"], payload["password"]


def get_auth_token(base_url, email=None, password=None):
    if email is None or password is None:
        email, password = create_test_user(base_url)
    
    response = requests.post(
        f"{base_url}/login",
        json={"email": email, "password": password}
    )
    response.raise_for_status()
    data = response.json()
    
    auth_header = data.get("authorization", "")
    if auth_header.startswith("Bearer "):
        return auth_header[7:] 
    return auth_header


def get_auth_headers(base_url, email=None, password=None):
    token = get_auth_token(base_url, email, password)
    return {"Authorization": f"Bearer {token}"}
