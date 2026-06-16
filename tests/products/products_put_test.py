import uuid
import requests


def _generate_product_payload():
    suffix = uuid.uuid4().hex[:8]
    return {
        "nome": f"Produto PUT {suffix}",
        "preco": 299,
        "descricao": "Produto para PUT",
        "quantidade": 5,
        "categoria": "Teste"
    }


def _create_product(base_url):
    payload = _generate_product_payload()
    response = requests.post(f"{base_url}/produtos", json=payload)
    response.raise_for_status()
    data = response.json()
    return data.get("_id") or data.get("id")


# test scenario 1: update product successfully
def test_update_product_successfully(base_url):
    product_id = _create_product(base_url)
    assert product_id

    update_payload = {
        "nome": "Produto Atualizado AI",
        "preco": 349,
        "descricao": "Produto atualizado com sucesso",
        "quantidade": 8,
        "categoria": "Atualização"
    }

    response = requests.put(f"{base_url}/produtos/{product_id}", json=update_payload)

    assert response.status_code in (200, 201, 204)

    if response.status_code != 204:
        response_data = response.json()
        assert "message" in response_data
        assert isinstance(response_data["message"], str)

    verify = requests.get(f"{base_url}/produtos/{product_id}")
    assert verify.status_code == 200
    verify_data = verify.json()
    assert verify_data["nome"] == update_payload["nome"]
    assert verify_data["preco"] == update_payload["preco"]


# test scenario 2: update product with invalid id returns not found
def test_update_product_with_invalid_id_returns_not_found(base_url):
    invalid_id = "00000000ABCDEFGH"
    response = requests.put(
        f"{base_url}/produtos/{invalid_id}",
        json={"nome": "Produto Inválido", "preco": 100}
    )

    assert response.status_code == 404
    response_data = response.json()
    assert "message" in response_data