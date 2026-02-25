from selenium import webdriver
from selenium.webdriver.common.by import By

# ---------------------------------------------------------
# ESTRUCTURA PAGE OBJECT MODEL (POM)
# ---------------------------------------------------------

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def encontrar(self, locator):
        return self.driver.find_element(*locator)

    def clic(self, locator):
        self.encontrar(locator).click()

    def escribir(self, locator, texto):
        elemento = self.encontrar(locator)
        elemento.clear()
        elemento.send_keys(texto)

class LoginPage(BasePage):
    LOCATOR_USER = (By.ID, "username")
    LOCATOR_PASS = (By.ID, "password")
    LOCATOR_BTN = (By.CSS_SELECTOR, "button.radius")
    LOCATOR_MSG = (By.ID, "flash")

    def cargar_pagina(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, usuario, password):
        self.escribir(self.LOCATOR_USER, usuario)
        self.escribir(self.LOCATOR_PASS, password)
        self.clic(self.LOCATOR_BTN)

    def obtener_mensaje(self):
        return self.encontrar(self.LOCATOR_MSG).text

# ---------------------------------------------------------
# EJECUCIÓN DE PRUEBA AVANZADA
# ---------------------------------------------------------

if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        pagina_login = LoginPage(driver)
        pagina_login.cargar_pagina()
        pagina_login.login("tomsmith", "SuperSecretPassword!")
        
        print("Resultado POM:", pagina_login.obtener_mensaje())
    finally:
        driver.quit()