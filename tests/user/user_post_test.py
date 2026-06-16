import uuid
import requests


def _generate_user_payload():
	suffix = uuid.uuid4().hex[:8]
	return {
		"nome": f"Teste API {suffix}",
		"email": f"teste_api_{suffix}@example.com",
		"password": "teste123"
	}


def test_create_user_successfully(base_url):
	payload = _generate_user_payload()
	response = requests.post(f"{base_url}/usuarios", json=payload)

	assert response.status_code in (200, 201)

	response_data = response.json()
	assert "message" in response_data
	assert isinstance(response_data["message"], str)
	assert "_id" in response_data or "id" in response_data


def test_create_user_missing_fields_returns_error(base_url):
	response = requests.post(f"{base_url}/usuarios", json={"nome": "Sem email"})

	assert response.status_code == 400

	response_data = response.json()
	assert "message" in response_data
	assert isinstance(response_data["message"], str)


def test_create_user_response_format(base_url):
	payload = _generate_user_payload()
	response = requests.post(f"{base_url}/usuarios", json=payload)

	assert response.status_code in (200, 201)
	assert response.headers.get("Content-Type", "").startswith("application/json")

	response_data = response.json()
	assert isinstance(response_data, dict)
	assert "message" in response_data
	assert response_data["message"]
	assert "_id" in response_data or "id" in response_data
