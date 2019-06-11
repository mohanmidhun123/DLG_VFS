Feature: Acceptance Test for Volkswagen financial services

    Scenario: Positive Scenario - Check that the web page tittle is visible
        Given I navigate to the Home page
        Then I verify page tittle as "Volkswagen Financial Services"

    Scenario: Positive Scenario - Verify that "ENTER REG" field is present
        Given I navigate to the Home page
        Then I verify that "ENTER REG" field is present

    Scenario: Positive Scenario - Verify that "Find vehicle" button is present
        Given I navigate to the Home page
        Then I verify that "Find vehicle" field is present

    Scenario: Positive Scenario - Verify that "Please enter the vehicle registration" field is present
        Given I navigate to the Home page
        Then I verify that "Please enter the vehicle registration" field is present

    Scenario: Negative Scenario -Check Error responses if no registration number is entered.
        Given I navigate to the Home page
        When I click on "Find vehicle"
        Then I should get an error message as "Please enter a valid car registration"

    Scenario: Positive Scenario - Check if expected search result(Cover Start and End date) is obtained
        Given I navigate to the Home page
        When I search for registration no as "OV12UYY"
        And I click on "Find vehicle"
        Then I see a my registration number in search result
        Then I see a cover start date as "09FEB2022:16:26"
        Then I see a cover end date as "18FEB2022:23:59"