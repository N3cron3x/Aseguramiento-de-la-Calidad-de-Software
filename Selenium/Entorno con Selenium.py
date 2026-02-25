import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------------------------------
# CONFIGURACIÓN DEL ENTORNO Y GENERACIÓN DE INFORMES (LOGS)
# ---------------------------------------------------------

logging.basicConfig(
    filename='reporte_automatizacion.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8' 
)

def obtener_driver(navegador="chrome"):
    if navegador.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

# ---------------------------------------------------------
# EJECUCIÓN: IDENTIFICACIÓN, ESPERAS Y ELEMENTOS DINÁMICOS
# ---------------------------------------------------------

def ejecutar_pruebas_basicas():
    driver = obtener_driver("chrome")
    wait = WebDriverWait(driver, 10)

    try:
        logging.info("Iniciando prueba de navegación y elementos.")
        driver.get("https://the-internet.herokuapp.com/login")

        usuario = driver.find_element(By.ID, "username")
        password = driver.find_element(By.NAME, "password")
        boton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        texto_login = driver.find_element(By.XPATH, "//h2[contains(text(),'Login')]")

        usuario.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        boton.click()

        mensaje_alerta = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        
        if "You logged into a secure area!" in mensaje_alerta.text:
            logging.info("Login exitoso: Elemento dinámico verificado.")
        else:
            logging.error("Fallo en la validación del login.")

        # ---------------------------------------------------------
        # MANEJO DE VENTANAS, FRAMES Y JAVASCRIPT
        # ---------------------------------------------------------

        driver.execute_script("window.open('https://the-internet.herokuapp.com/iframe', '_blank');")
        
        ventanas = driver.window_handles
        driver.switch_to.window(ventanas[1])
        
        driver.switch_to.frame("mce_0_ifr")
        
        editor = driver.find_element(By.ID, "tinymce")
        
        editor.send_keys(Keys.CONTROL + "a")
        editor.send_keys(Keys.DELETE)
        
        editor.send_keys("Texto automatizado con Selenium en Python.")
        
        driver.switch_to.default_content()
        
        logging.info("Interacción con IFrame y Ventanas completada correctamente.")
        
        driver.close() 
        driver.switch_to.window(ventanas[0]) 
        cookies = driver.get_cookies()
        logging.info(f"Total de cookies obtenidas: {len(cookies)}")

    except Exception as e:
        logging.error(f"Error durante la ejecución: {e}")
        print(f"Error en consola: {e}")
    finally:
        driver.quit()
        logging.info("Driver cerrado correctamente.")

if __name__ == "__main__":
    ejecutar_pruebas_basicas()