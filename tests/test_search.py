import pytest
from conftest import MySearchPage


def test_mercado_libre_search(MySearchPage):
    MySearchPage.load()

    # Assert that the page title contains "Mercado Libre"
    assert "Mercado Libre" in MySearchPage.page.title(), "The MercadoLibre website is not loaded successfully."
