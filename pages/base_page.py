class BasePage:
    def __init__(self, page, context):
        self.page = page
        self.base_url = context.base_url
        self.locators = context.locators

    @staticmethod
    def get_base_url(self):
        return self.base_url
    
    def get_locator(self, page_name, locator_key):
        locator = self.locators.get(page_name, {}).get(locator_key)
        if locator:
            return locator
        else:
            raise ValueError(f"Locator '{locator_key}' not found for page '{page_name}'.")

    def click(self, page_name, locator_key):
        locator = self.get_locator(page_name, locator_key)
        self.page.locator(locator).click()
    
    def type(self, page_name, locator_key, text):
        locator = self.get_locator(page_name, locator_key)
        self.page.locator(locator).fill(text)

    def open(self, url):
        self.page.goto(url)

    def get_text(self, page_name, locator_key):
        locator = self.get_locator(page_name, locator_key)
        return self.page.locator(locator).text_content()