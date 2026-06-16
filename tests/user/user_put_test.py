import uuid
import requests


def _generate_user_payload():
	suffix = uuid.uuid4().hex[:8]
	return {
		"nome": f"Teste PUT {suffix}",
		"email": f"teste_put_{suffix}@example.com",
		"password": "teste123"
	}


def _create_user(base_url):
	payload = _generate_user_payload()
	response = requests.post(f"{base_url}/usuarios", json=payload)
	response.raise_for_status()
	data = response.json()
	return data.get("_id") or data.get("id")


def test_update_user_successfully(base_url):
	user_id = _create_user(base_url)
	assert user_id

	update_payload = {
		"nome": "Usuário Atualizado AI",
		"email": f"updated_{uuid.uuid4().hex[:8]}@example.com",
		"password": "novaSenha123"
	}

	response = requests.put(f"{base_url}/usuarios/{user_id}", json=update_payload)

	assert response.status_code in (200, 201, 204)

	if response.status_code != 204:
		response_data = response.json()
		assert "message" in response_data
		assert isinstance(response_data["message"], str)
		assert response_data["message"]

	verify = requests.get(f"{base_url}/usuarios/{user_id}")
	assert verify.status_code == 200
	verify_data = verify.json()
	assert verify_data["nome"] == update_payload["nome"]
	assert verify_data["email"] == update_payload["email"]


def test_update_user_with_invalid_id_returns_not_found(base_url):
	invalid_id = "00000000ABCDEFGH"
	response = requests.put(
		f"{base_url}/usuarios/{invalid_id}",
		json={"nome": "Nome Inválido", "email": "inv@example.com", "password": "teste123"}
	)

	assert response.status_code == 404
	response_data = response.json()
	assert "message" in response_data
	assert isinstance(response_data["message"], str)


def test_update_user_response_format(base_url):
	user_id = _create_user(base_url)
	assert user_id

	update_payload = {
		"nome": "Formato de Resposta",
		"email": f"format_{uuid.uuid4().hex[:8]}@example.com",
		"password": "senha123"
	}

	response = requests.put(f"{base_url}/usuarios/{user_id}", json=update_payload)
	assert response.status_code in (200, 201, 204)

	if response.status_code != 204:
		assert response.headers.get("Content-Type", "").startswith("application/json")
		response_data = response.json()
		assert isinstance(response_data, dict)
		assert "message" in response_data
		assert response_data["message"]
