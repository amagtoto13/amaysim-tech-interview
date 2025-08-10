Feature: Payment failure handling

    Scenario: User tries to purchase a 7-day mobile plan with a declined card
        Given I am on the 7-day SIM plan page
        When I choose "pick a new number" and "physical sim"
        And I fill in my customer details
        And I enter "declined" credit card
        Then I should see a payment error message