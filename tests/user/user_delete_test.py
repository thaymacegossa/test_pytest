import uuid
import requests


def _generate_user_payload():
	suffix = uuid.uuid4().hex[:8]
	return {
		"nome": f"Teste DELETE {suffix}",
		"email": f"teste_delete_{suffix}@example.com",
		"password": "teste123"
	}


def _create_user(base_url):
	payload = _generate_user_payload()
	response = requests.post(f"{base_url}/usuarios", json=payload)
	response.raise_for_status()
	data = response.json()
	return data.get("_id") or data.get("id")


def test_delete_user_successfully(base_url):
	user_id = _create_user(base_url)
	assert user_id

	response = requests.delete(f"{base_url}/usuarios/{user_id}")

	assert response.status_code in (200, 204)

	if response.status_code == 200:
		response_data = response.json()
		assert "message" in response_data
		assert isinstance(response_data["message"], str)

	verify = requests.get(f"{base_url}/usuarios/{user_id}")
	assert verify.status_code == 404


def test_delete_user_with_invalid_id_returns_not_found(base_url):
	invalid_id = "00000000ABCDEFGH"
	response = requests.delete(f"{base_url}/usuarios/{invalid_id}")

	assert response.status_code == 404
	response_data = response.json()
	assert "message" in response_data
	assert isinstance(response_data["message"], str)


def test_delete_user_response_format(base_url):
	user_id = _create_user(base_url)
	assert user_id

	response = requests.delete(f"{base_url}/usuarios/{user_id}")
	assert response.status_code in (200, 204)

	if response.status_code == 200:
		assert response.headers.get("Content-Type", "").startswith("application/json")
		response_data = response.json()
		assert isinstance(response_data, dict)
		assert "message" in response_data
		assert response_data["message"]
