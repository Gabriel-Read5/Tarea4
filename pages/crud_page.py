from selenium.webdriver.common.by import By

class CrudPage:
    INPUT_TAREA = (By.ID, "nombre-tarea")
    BTN_GUARDAR = (By.CSS_SELECTOR, "button[type='submit']")
    BUSCADOR = (By.ID, "buscador")
    LISTA_TAREAS = (By.ID, "lista-tareas")

    def __init__(self, driver):
        self.driver = driver

    def crear_tarea(self, nombre):
        self.driver.find_element(*self.INPUT_TAREA).clear()
        self.driver.find_element(*self.INPUT_TAREA).send_keys(nombre)
        self.driver.find_element(*self.BTN_GUARDAR).click()

    def buscar_tarea(self, texto):
        self.driver.find_element(*self.BUSCADOR).clear()
        self.driver.find_element(*self.BUSCADOR).send_keys(texto)

    def obtener_texto_lista(self):
        return self.driver.find_element(*self.LISTA_TAREAS).text