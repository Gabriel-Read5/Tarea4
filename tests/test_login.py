from pages.login_page import LoginPage

def test_login_camino_feliz(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("admin", "1234")
    assert "dashboard" in driver.current_url.lower() or "bienvenido" in driver.page_source.lower()

def test_login_negativo(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("admin", "incorrecta")
    assert "error" in driver.page_source.lower() or "incorrect" in driver.page_source.lower()

def test_login_limite(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("", "")
    assert "required" in driver.page_source.lower() or "obligatorio" in driver.page_source.lower() or "error" in driver.page_source.lower()