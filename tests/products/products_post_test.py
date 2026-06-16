import uuid
import requests


def _generate_product_payload():
    suffix = uuid.uuid4().hex[:8]
    return {
        "nome": f"Produto Teste {suffix}",
        "preco": 199,
        "descricao": "Descrição de teste",
        "quantidade": 10,
    }


# test scenario 1: create product successfully
def test_create_product_successfully(base_url, auth_headers):
    payload = _generate_product_payload()
    response = requests.post(f"{base_url}/produtos", json=payload, headers=auth_headers)

    assert response.status_code in (200, 201)

    response_data = response.json()
    assert "message" in response_data
    assert isinstance(response_data["message"], str)
    assert "_id" in response_data or "id" in response_data


# test scenario 2: create product missing required fields returns error
def test_create_product_missing_required_fields_returns_error(base_url, auth_headers):
    response = requests.post(f"{base_url}/produtos", json={"nome": "Produto Incompleto"}, headers=auth_headers)

    assert response.status_code == 400

    response_data = response.json()
    assert "descricao é obrigatório" in response_data.get("descricao")
    assert "preco é obrigatório" in response_data.get("preco")
    assert "quantidade é obrigatório" in response_data.get("quantidade")