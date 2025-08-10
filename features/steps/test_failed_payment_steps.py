from behave import given, when, then
from pages.sim_plans.seven_day_sim_page import SevenDaySimPlanPage
from pages.cart_page import CartPage
from pages.your_details_page import YourDetailsPage

@given('I am on the 7-day SIM plan page')
def step_given_seven_day_plan_page(context):
    context.seven_day_plan_page = SevenDaySimPlanPage(context.page, context)
    context.seven_day_plan_page.open()
    context.seven_day_plan_page.click_buy_now()

@when('I choose "{number_option}" and "{sim_type}"')
def step_when_choosing_plan(context, number_option, sim_type):
    context.cart_page = CartPage(context.page, context)
    if number_option.lower() == "pick a new number":
        context.cart_page.click_pick_a_new_number()
    elif number_option.lower() == "transfer your number":
        context.cart_page.click_transfer_your_number()
    else:
        raise ValueError(f"Invalid number_option: {number_option}")
    
    if sim_type.lower() == "physical sim":
        context.cart_page.choose_physical_sim()
    elif sim_type.lower() == "esim":
        context.cart_page.choose_esim()
    else:
        raise ValueError(f"Invalid sim_type: {sim_type}")
    
    context.cart_page.click_checkout_button()

@when('I fill in my customer details')
def step_when_fill_customer_details(context):
    context.your_details_page = YourDetailsPage(context.page, context)

    context.your_details_page.click_im_new_to_amaysim()

    about_you = context.test_data["about_you"]
    context.your_details_page.type_firstname(about_you['firstname'])
    context.your_details_page.type_lastname(about_you['lastname'])
    context.your_details_page.type_dob(about_you['dob'])
    context.your_details_page.type_email(about_you['email'])
    context.your_details_page.type_password(about_you['password'])
    context.your_details_page.type_number(about_you['phone_number'])
    
    delivery_address = context.test_data['delivery_address']
    context.your_details_page.type_address(delivery_address['default_address'])
    context.your_details_page.click_suggested_address(delivery_address['default_address'])

@when('I enter "{card_type}" credit card')
def step_when_enter_credit_card_details(context, card_type):
    context.your_details_page = YourDetailsPage(context.page, context)
    payments = context.test_data['payments']
    if card_type.lower() == "declined":
        declined_cc = payments['declined_cc']
        context.your_details_page.click_credit_card_button()
        context.your_details_page.type_cc_number(declined_cc['cc_number'])
        context.your_details_page.type_cc_expiry_date(declined_cc['cc_expiry_date'])
        context.your_details_page.type_cvc(declined_cc['cvc'])
        context.your_details_page.click_pay_now_button
    elif card_type.lower() == "valid":
        # code for valid card
        pass
    elif card_type.lower() == "expired":
        # code for expired card
        pass
    elif card_type.lower() == "blocked":
        # code for blocked card
        pass
    else:
        raise ValueError(f"Invalid card type: {card_type}")

@then('I should see a payment error message')
def step_then_validate_error_message(context):
    context.your_details_page = YourDetailsPage(context.page, context)

    assert context.your_details_page.get_cart_error_message().is_visible(), 'Cart error message is not visible'