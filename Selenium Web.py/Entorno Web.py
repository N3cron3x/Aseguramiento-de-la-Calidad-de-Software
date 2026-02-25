import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PruebasAutomatizadasEdge(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.base_url = "https://www.saucedemo.com"

    def test_flujo_completo_compra(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        driver.get(self.base_url)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        titulo_seccion = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        self.assertEqual(titulo_seccion.text, "Products")

        boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        boton_agregar.click()

        boton_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        boton_carrito.click()

        item_inventario = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        self.assertEqual(item_inventario.text, "Sauce Labs Backpack")

        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Usuario")
        driver.find_element(By.ID, "last-name").send_keys("Automated")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        driver.find_element(By.ID, "finish").click()

        mensaje_final = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        self.assertIn("Thank you", mensaje_final.text)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    archivo_reporte = "resultado_prueba.txt"
    
    with open(archivo_reporte, "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(PruebasAutomatizadasEdge)
        result = runner.run(suite)
        
    print(f"Ejecución finalizada. Se ha creado el archivo: {archivo_reporte}")