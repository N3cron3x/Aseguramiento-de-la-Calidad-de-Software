import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.PointerInput;
import org.openqa.selenium.interactions.Sequence;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;
import java.util.Arrays;
import java.util.Set;

public class AutomatizacionAppiumTest {

    private AndroidDriver driver;

    // Integración con Marcos de Pruebas Móviles
    @BeforeClass
    public void configurarEntorno() throws MalformedURLException {
        UiAutomator2Options opciones = new UiAutomator2Options();
        opciones.setDeviceName("emulator-5554");
        opciones.setApp("/ruta/absoluta/a/la/aplicacion.apk");
        
        driver = new AndroidDriver(new URL("http://127.0.0.1:4723"), opciones);
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
    }

    // Primeros Pasos con Appium
    @Test(priority = 1)
    public void iniciarSesionEInteractuar() {
        WebElement botonAceptar = driver.findElement(AppiumBy.id("com.proyecto.app:id/btn_aceptar"));
        botonAceptar.click();
    }

    // Identificación de Elementos en Aplicaciones Móviles
    @Test(priority = 2)
    public void identificarElementosUi() {
        WebElement campoTexto = driver.findElement(AppiumBy.id("com.proyecto.app:id/input_usuario"));
        campoTexto.sendKeys("UsuarioPrueba");

        WebElement elementoXpath = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text='Ingresar']"));
        elementoXpath.click();

        WebElement elementoAccesibilidad = driver.findElement(AppiumBy.accessibilityId("Icono de configuracion"));
        elementoAccesibilidad.click();
    }

    // Manejo de Gestos y Eventos Táctiles
    @Test(priority = 3)
    public void ejecutarGestosTactiles() {
        PointerInput dedo = new PointerInput(PointerInput.Kind.TOUCH, "dedo1");
        Sequence deslizamiento = new Sequence(dedo, 1);

        deslizamiento.addAction(dedo.createPointerMove(Duration.ofMillis(0), PointerInput.Origin.viewport(), 500, 1500));
        deslizamiento.addAction(dedo.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        deslizamiento.addAction(dedo.createPointerMove(Duration.ofMillis(1000), PointerInput.Origin.viewport(), 500, 500));
        deslizamiento.addAction(dedo.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));

        driver.perform(Arrays.asList(deslizamiento));
    }

    // Automatización de Aplicaciones Nativas y Híbridas
    @Test(priority = 4)
    public void operarElementosNativos() {
        WebElement selectorNativo = driver.findElement(AppiumBy.className("android.widget.Switch"));
        selectorNativo.click();
    }

    // Manejo de Contextos y Ventanas Múltiples
    @Test(priority = 5)
    public void alternarContextosHibridos() {
        Set<String> contextosDisponibles = driver.getContextHandles();
        
        for (String contexto : contextosDisponibles) {
            if (contexto.contains("WEBVIEW")) {
                driver.context(contexto);
                break;
            }
        }

        WebElement botonWeb = driver.findElement(AppiumBy.cssSelector(".btn-login-web"));
        botonWeb.click();

        driver.context("NATIVE_APP");
    }

    @AfterClass
    public void finalizarSesion() {
        if (driver != null) {
            driver.quit();
        }
    }
}