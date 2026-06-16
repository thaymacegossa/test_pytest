import uuid
import requests


def _generate_product_payload():
    suffix = uuid.uuid4().hex[:8]
    return {
        "nome": f"Produto DELETE {suffix}",
        "preco": 199,
        "descricao": "Produto para DELETE",
        "quantidade": 3,
        "categoria": "Teste"
    }


def _create_product(base_url):
    payload = _generate_product_payload()
    response = requests.post(f"{base_url}/produtos", json=payload)
    response.raise_for_status()
    data = response.json()
    return data.get("_id") or data.get("id")


# test scenario 1: delete product successfully
def test_delete_product_successfully(base_url):
    product_id = _create_product(base_url)
    assert product_id

    response = requests.delete(f"{base_url}/produtos/{product_id}")

    assert response.status_code in (200, 204)

    if response.status_code == 200:
        response_data = response.json()
        assert "message" in response_data
        assert isinstance(response_data["message"], str)

    verify = requests.get(f"{base_url}/produtos/{product_id}")
    assert verify.status_code == 404


# test scenario 2: delete product with invalid id returns not found
def test_delete_product_with_invalid_id_returns_not_found(base_url):
    invalid_id = "00000000ABCDEFGH"
    response = requests.delete(f"{base_url}/produtos/{invalid_id}")

    assert response.status_code == 404
    response_data = response.json()
    assert "message" in response_data