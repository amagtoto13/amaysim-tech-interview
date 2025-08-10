from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = self.get_base_url() + 'mobile/cart/7-day-10gb'
        self.page_name = 'cart_page'

    def open(self):
        return super().open(self.url)
    
    def click_pick_a_new_number(self):
        self.click(self.page_name, 'tab_new_number')

    def click_transfer_your_number(self):
        self.click(self.page_name, 'tab_transfer_your_number')

    def choose_physical_sim(self):
        self.click(self.page_name, 'radio_physical_sim')
    
    def choose_esim(self):
        self.click(self.page_name, 'radio_esim')

    def click_checkout_button(self):
        self.click(self.page_name, 'button_checkout')