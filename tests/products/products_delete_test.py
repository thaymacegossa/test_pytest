import uuid
import requests


def _generate_product_payload():
    suffix = uuid.uuid4().hex[:8]
    return {
        "nome": f"Produto DELETE {suffix}",
        "preco": 199,
        "descricao": "Produto para DELETE",
        "quantidade": 3
    }


def _create_product(base_url, auth_headers):
    payload = _generate_product_payload()
    response = requests.post(f"{base_url}/produtos", json=payload, headers=auth_headers)
    response.raise_for_status()
    data = response.json()
    return data.get("_id") or data.get("id")


# test scenario 1: delete product successfully
def test_delete_product_successfully(base_url, auth_headers):
    product_id = _create_product(base_url, auth_headers)
    assert product_id

    response = requests.delete(f"{base_url}/produtos/{product_id}", headers=auth_headers)

    assert response.status_code in (200, 204)

    if response.status_code == 200:
        response_data = response.json()
        assert "message" in response_data
        assert isinstance(response_data["message"], str)

    verify = requests.get(f"{base_url}/produtos/{product_id}")
    
    # BUG REPORT: If status 200 is returned, product still exists after deletion
    if verify.status_code == 200:
        raise AssertionError(
            f"BUG: Product with ID {product_id} returned wrong code. "
            f"Expected status 404, but got 200. Product data: {verify.json()}"
        )
    
    assert verify.status_code == 400


# test scenario 2: delete product with invalid id returns not found
def test_delete_product_with_invalid_id_returns_not_found(base_url, auth_headers):
    invalid_id = "00000000ABCDEFGH"
    response = requests.delete(f"{base_url}/produtos/{invalid_id}", headers=auth_headers)

    if response.status_code != 404:
        raise AssertionError(
            f"BUG: Product deleted returned wrong code. "
            f"Expected status 404. but got {response.status_code}. Response data: {response.json()}"
        )

    assert response.status_code == 404