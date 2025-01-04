import helpers
import helpers
import pages
import data
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

    def test_01_set_route(self):
        # Test para establecer una ruta"""
        self.driver.get(data.urban_routes_url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'from')))
        wait.until(EC.presence_of_element_located((By.ID, 'to')))
        routes_page = pages.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.round')))
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_02_select_comfort_fee(self):
        # Test para seleccionar la tarifa de confort"""
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')))
        routes_page.select_comfort_fee()
        assert routes_page.get_comfort_title() == "Comfort"

    def test_03_fill_phone_number(self):
        # Test para ingresar el número de teléfono
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_button()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'phone')))
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        routes_page.click_next_phone_button()
        code = helpers.retrieve_phone_code(driver=self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirmation_button()

    def test_04_add_credit_card(self):
        # Test para agregar una tarjeta de crédito
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_payment_method_button()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pp-plus')))
        assert routes_page.return_payment_method_text() == 'Payment method'
        routes_page.click_add_plus_button()
        card_number = data.card_number
        code = data.card_code
        routes_page.set_card_number(card_number)
        routes_page.set_card_code(code)
        routes_page.click_no_interactable_space()
        routes_page.click_add_card_button()
        routes_page.click_close_add_card_button()

    def test_05_write_driver_a_message(self):
        # Test para escribir un mensaje al conductor
        routes_page = pages.UrbanRoutesPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'comment')))
        message_for_driver = data.message_for_driver
        routes_page.set_drivers_message(message_for_driver)
        assert routes_page.get_drivers_message() == message_for_driver

    def test_06_request_blanket_and_tissues(self):
        # Test para solicitar mantas y pañuelos
        routes_page = pages.UrbanRoutesPage(self.driver)
        wait = WebDriverWait(self.driver, 10)

        # Esperar a que el elemento sea clicable
        # sugerido para corrección
        blanket_and_tissues_slider = wait.until(EC.element_to_be_clickable(routes_page.blanket_and_tissues_slider))
        blanket_and_tissues_slider.click()

    def test_07_order_two_ice_creams(self):
        # Test para ordenar dos helados
        # sugerido para corrección
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.double_click_ice_cream()
        two_ice_creams_count = routes_page.get_ice_cream_count()
        assert '2' in two_ice_creams_count

    def test_08_call_taxi_modal_change(self):
        # Test para cambiar el modal de llamar al taxi
        routes_page = pages.UrbanRoutesPage(self.driver)
        # Esperar a que el botón sea clicable
        wait = WebDriverWait(self.driver, 10)
        find_taxi_button = wait.until(EC.element_to_be_clickable(routes_page.find_taxi_button))
        find_taxi_button.click()
        button_text_change = routes_page.get_button_text_change()
        assert 'Call a taxi' in button_text_change

    @classmethod
    def teardown_class(cls):
        time.sleep(3)
        # Cerrar la ventana del navegador
        cls.driver.quit()

