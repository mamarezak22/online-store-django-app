from django.urls import reverse
from fixtures.fixtures import product
from rest_framework.test import APIClient

import pytest


@pytest.mark.django_db
def test_update_product_view_count(product):
    client = APIClient()
    resp = client.get(reverse("product-detail",kwargs = {"product_id" : product.id}))
    resp_data = resp.json()

    assert resp.status_code == 200
    product.refresh_from_db()

    assert product.view_count == 1
   
   
