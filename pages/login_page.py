from selenium.webdriver.common.by import By

class LoginPage:
    URL = "http://127.0.0.1:5500/index.html"  # cambia esto por la ruta real

    INPUT_USUARIO = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "loginBtn")
    MENSAJE_ERROR = (By.ID, "errorMsg")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)

    def login(self, usuario, password):
        self.driver.find_element(*self.INPUT_USUARIO).clear()
        self.driver.find_element(*self.INPUT_USUARIO).send_keys(usuario)
        self.driver.find_element(*self.INPUT_PASSWORD).clear()
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*self.BTN_LOGIN).click()

    def obtener_error(self):
        return self.driver.find_element(*self.MENSAJE_ERROR).text