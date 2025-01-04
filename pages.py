from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Localizadores

    # Campo de entrada para la dirección de origen
    from_field = (By.ID, 'from')

    # Campo de entrada para la dirección de destino
    to_field = (By.ID, 'to')

    # Botón para llamar un taxi
    call_taxi_button = (By.CSS_SELECTOR, 'button.round')

    # Elemento de tarifa de confort (icono de imagen)
    comfort_fee = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')

    # Título de la tarifa de confort
    comfort_title = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')

    # Botón para ingresar el número de teléfono
    phone_number_button = (By.CLASS_NAME, 'np-text')

    # Campo de entrada para el número de teléfono
    phone_number_field = (By.ID, 'phone')

    # Botón para continuar después de ingresar el número de teléfono
    phone_next_button = (By.XPATH, '//*/div[1]/form/div[2]/button')

    # Campo de entrada para el código de confirmación
    code_number_field = (By.XPATH, '//div[2]/form/div[1]/div[1]/input')

    # Botón de confirmación después de ingresar el código
    confirmation_button = (By.XPATH, '//div[2]/form/div[2]/button[1]')

    # Título del método de pago
    payment_method_title = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]')

    # Botón para seleccionar el método de pago
    payment_method_button = (By.CLASS_NAME, 'pp-text')

    # Botón para agregar una nueva tarjeta de crédito
    add_card_plus_button = (By.CLASS_NAME, 'pp-plus')

    # Campo de entrada para el número de la tarjeta de crédito
    card_number_field = (By.ID, 'number')

    # Campo de entrada para el código CVV de la tarjeta de crédito
    cvv_field = (By.XPATH, '//div[2]/div[2]/input')

    # Área no interactable para hacer clic
    no_interactable_space = (By.CLASS_NAME, 'card-wrapper')

    # Botón para agregar la tarjeta de crédito
    add_card_button = (By.XPATH, '//form/div[3]/button[1]')

    # Botón para cerrar la ventana de agregar tarjeta de crédito
    close_add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    # Campo de entrada para el mensaje al conductor
    drivers_message_field = (By.ID, 'comment')

    # Control deslizante para solicitar mantas y pañuelos
    # sugerido para corrección
    blanket_and_tissues_slider = (By.CLASS_NAME, 'switch')

    # Contador del producto
    # sugerido para corrección
    ice_plus_counter = (By.CLASS_NAME, 'counter-plus')

    # Contador del helado
    # sugerido para corrección
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')

    # Botón para buscar un taxi
    find_taxi_button = (By.CLASS_NAME, 'smart-button-main')

    def __init__(self, driver):
        self.driver = driver

    # Funciones Prueba 01
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    # Funciones Prueba 02
    def click_call_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_fee(self):
        self.driver.find_element(*self.comfort_fee).click()

    def get_comfort_title(self):
        return self.driver.find_element(*self.comfort_title).text

    # Funciones Prueba 03
    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_phone_button(self):
        self.driver.find_element(*self.phone_next_button).click()

    def set_phone_code(self, code):
        self.driver.find_element(*self.code_number_field).send_keys(code)

    def click_confirmation_button(self):
        self.driver.find_element(*self.confirmation_button).click()

    # Funciones Prueba 04
    def return_payment_method_text(self):
        return self.driver.find_element(*self.payment_method_title).text

    def click_payment_method_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_plus_button(self):
        self.driver.find_element(*self.add_card_plus_button).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, code):
        self.driver.find_element(*self.cvv_field).send_keys(code)

    def click_no_interactable_space(self):
        self.driver.find_element(*self.no_interactable_space).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def click_close_add_card_button(self):
        self.driver.find_element(*self.close_add_card_button).click()

    # Funciones Prueba 05
    def set_drivers_message(self, message_for_driver):
        self.driver.find_element(*self.drivers_message_field).send_keys(message_for_driver)

    def get_drivers_message(self):
        return self.driver.find_element(*self.drivers_message_field).get_attribute('value')

    # Funciones Prueba 06
    def click_blanket_and_tissues_slider(self):
        self.driver.find_element(*self.blanket_and_tissues_slider).click()

    # Funciones Prueba 07
    def double_click_ice_cream(self):
        self.driver.find_element(*self.ice_plus_counter).click()
        self.driver.find_element(*self.ice_plus_counter).click()
    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    # Funciones Prueba 08
    def get_button_text_change(self):
        return self.driver.find_element(*self.find_taxi_button).text