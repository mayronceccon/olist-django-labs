from django.urls import reverse
import pytest


@pytest.fixture
def response_aula9_view(client):
    return client.get(reverse("aula9"))
