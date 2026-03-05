import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class PruebaAutomatizacionAppium(unittest.TestCase):

    def setUp(self):
        opciones = UiAutomator2Options()
        opciones.platform_name = 'Android'
        opciones.device_name = 'emulator-5554'
        opciones.app = '/ruta/hacia/su/aplicacion_de_prueba.apk'
        opciones.automation_name = 'UiAutomator2'

        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=opciones)
        self.driver.implicitly_wait(10)

    def test_inicio_sesion(self):
        campo_usuario = self.driver.find_element(by=AppiumBy.ID, value='com.ejemplo.app:id/input_usuario')
        campo_usuario.send_keys('UsuarioPrueba')

        campo_clave = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Contraseña"]')
        campo_clave.send_keys('ClaveSegura123')

        boton_acceso = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Boton Acceder')
        boton_acceso.click()

        mensaje_bienvenida = self.driver.find_element(by=AppiumBy.ID, value='com.ejemplo.app:id/texto_bienvenida')
        self.assertTrue(mensaje_bienvenida.is_displayed())

    def test_desplazamiento_pantalla(self):
        acciones = ActionChains(self.driver)
        entrada_puntero = PointerInput(interaction.POINTER_TOUCH, "dedo_indice")
        acciones.w3c_actions = ActionBuilder(self.driver, mouse=entrada_puntero)
        
        acciones.w3c_actions.pointer_action.move_to_location(500, 1500)
        acciones.w3c_actions.pointer_action.pointer_down()
        acciones.w3c_actions.pointer_action.move_to_location(500, 500)
        acciones.w3c_actions.pointer_action.release()
        acciones.perform()

        elemento_lista = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Elemento Oculto"]')
        self.assertIsNotNone(elemento_lista)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()