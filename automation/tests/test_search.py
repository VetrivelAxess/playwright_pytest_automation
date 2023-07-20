
def test_mercado_libre_search(MyHomePage):
    MyHomePage.load()

    # Assert that the page title contains "e"
    assert "Home - Alphacode" in MyHomePage.page.title(), "The alphacode website is loaded successfully."

def test_navigate_to_contact(MyHomePage):
    MyHomePage.load()
    MyHomePage.navigate_to_contact()
