from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
import os, json

@fixture
def browser(context):
    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=False)
        context.page = context.browser.new_page()

        yield context.page

def before_all(context):
    context.base_url = os.getenv("AMAYSIM_BASE_URL", "https://www.amaysim.com.au/")
    context.locators = get_locators()
    context.test_data = get_test_data()

def before_scenario(context, scenario):
    use_fixture(browser, context)

def after_scenario(context, scenario):
    context.page.close()
    context.browser.close()

def get_locators():
    with open('locators.json', 'r') as file:
        return json.load(file)["locators"]
    
def get_test_data():
    with open('test_data.json', 'r') as file:
        return json.load(file)