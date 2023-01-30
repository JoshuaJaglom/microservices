import requests
import pytest
import json
from menu_service import schemas


@pytest.fixture
def service_url():
    port = '8001'
    api_version = 'v1'
    final_url = f'http://localhost:{port}/{api_version}'
    return final_url


@pytest.fixture
def api_gateway_url():
    port = '8080'
    api_version = 'v1'
    final_url = f'http://localhost:{port}/{api_version}'
    return final_url


@pytest.mark.parametrize('endpoint, schemas, body', [
    ('menu/add', schemas.PostProduct, schemas.PostProduct(
        product='Mega name for film',
        price=1000)),
])
def test_post_product(endpoint, schemas, body, service_url):
    response = requests.post(
        f'{service_url}/{endpoint}',
        json=body.dict()
    )
    assert response.status_code == 201
    data = json.loads(response.content.decode())
    assert schemas.validate(data)
