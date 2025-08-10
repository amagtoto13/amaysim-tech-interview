from pages.base_page import BasePage

class YourDetailsPage(BasePage):
    def __init__(self, page, context):
        super().__init__(page, context)
        self.page_name = 'your_details_page'

    def click_im_new_to_amaysim(self):
        self.click(self.page_name, 'radio_new_to_amaysim')

    def type_firstname(self, firstname):
        self.type(self.page_name, 'input_firstname', firstname)

    def type_lastname(self, lastname):
        self.type(self.page_name, 'input_lastname', lastname)

    def type_dob(self, dob):
        self.type(self.page_name, 'input_lastname', dob)

    def type_email(self, email):
        self.type(self.page_name, 'input_email', email)

    def type_password(self, password):
        self.type(self.page_name, 'input_password', password)

    def type_number(self, phone_number):
        self.type(self.page_name, 'input_number', phone_number)

    def type_address(self, address):
        self.type(self.page_name, 'input_address', address)

    def click_suggested_address(self, address):
        locator = self.get_locator(self.page_name, 'option_address')
        self.page.locator(locator).first.click()

    def click_credit_card_button(self):
        form_locator = self.page.locator(self.get_locator(self.page_name, 'form_payment_cc')).wait_for()
        iframe_locator = form_locator.locator(self.get_locator(self.page_name, 'iframe_cc')).wait_for()
        iframe_element = iframe_locator.frame()
        iframe_element.locator(self.get_locator(self.page_name, 'button_credit_card')).click()

    def type_cc_number(self, cc_number):
        self.type(self.page_name, 'input_card_number', cc_number)

    def type_cc_expiry_date(self, cc_expiry_date):
        self.type(self.page_name, 'input_expiry_date', cc_expiry_date)
    
    def type_cvc(self, cvc):
        self.type(self.page_name, 'input_security_code', cvc)

    def click_agree_tnc(self):
        self.click(self.page_name, 'checkbox_agree_tnc')

    def click_pay_now_button(self):
        self.click(self.page_name, 'button_pay_now')

    def get_cart_error_message(self):
        return self.page.locator(self.get_locator(self.page_name, 'shopping_cart_error'))