import requests


# test scenario 1: list all products
def test_list_all_products_successfully(base_url):
    response = requests.get(f"{base_url}/produtos")

    assert response.status_code == 200

    response_data = response.json()
    assert "quantidade" in response_data
    assert "produtos" in response_data


# test scenario 2: get product by valid ID
def test_get_product_by_valid_id(base_url):
    list_response = requests.get(f"{base_url}/produtos")
    product_list = list_response.json()["produtos"]
    valid_id = product_list[0]["_id"]

    response = requests.get(f"{base_url}/produtos/{valid_id}")

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["_id"] == valid_id
    assert "nome" in response_data
    assert "preco" in response_data


# test scenario 3: get product by invalid ID
# bug report: should return a 404 not found
def test_get_product_by_invalid_id(base_url):
    invalid_id = "00000000ABCDEFGH"

    response = requests.get(f"{base_url}/produtos/{invalid_id}")

    assert response.status_code == 404
    response_data = response.json()
    assert "message" in response_data
