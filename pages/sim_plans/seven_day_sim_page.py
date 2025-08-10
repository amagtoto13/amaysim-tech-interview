from pages.base_page import BasePage

class SevenDaySimPlanPage(BasePage):
    def __init__(self, page, context):
        super().__init__(page, context)
        self.url = self.get_base_url() + 'sim-plans/7-day-sim-plans'
        self.page_name = '7_day_sim_plan'
    
    def open(self):
        return super().open(self.url)
    
    def click_buy_now(self):
        self.click(self.page_name, 'button_buy_now')