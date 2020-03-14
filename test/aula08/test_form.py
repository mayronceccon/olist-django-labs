from aula08.forms import PetForm
from datetime import date
from unittest import mock
import pytest


@mock.patch("aula08.forms.external_valid_names")
def test_pet_form(mock_external_valid_names):
    mock_external_valid_names.return_value = True
    data = {
        "nome": "rex",
        "data_nascimento": date(2019, 1, 1)
    }

    form = PetForm(data=data)

    assert form.is_valid()


@mock.patch("aula08.forms.external_valid_names")
@pytest.mark.parametrize("name", ["Putinho", "PUTINHO", "putinho"])
def test_pet_invalid(mock_external_valid_names, name):
    mock_external_valid_names.return_value = True
    data = {
        "nome": name,
        "data_nascimento": date(2019, 1, 1)
    }

    form = PetForm(data=data)

    assert form.is_valid() is False
