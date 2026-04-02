from pages.crud_page import CrudPage

def test_crear_tarea_camino_feliz(driver):
    driver.get("http://127.0.0.1:5500/index.html")  # cambia por tu URL real
    crud = CrudPage(driver)
    crud.crear_tarea("Estudiar Selenium")
    assert "Estudiar Selenium" in crud.obtener_texto_lista()

def test_crear_tarea_negativa(driver):
    driver.get("http://127.0.0.1:5500/index.html")
    crud = CrudPage(driver)
    crud.crear_tarea("")
    assert "required" in driver.page_source.lower() or "obligatorio" in driver.page_source.lower()

def test_crear_tarea_limite(driver):
    driver.get("http://127.0.0.1:5500/index.html")
    crud = CrudPage(driver)
    texto_largo = "a" * 255
    crud.crear_tarea(texto_largo)
    assert texto_largo in crud.obtener_texto_lista() or "error" in driver.page_source.lower()