Feature: Login on SauceDemo

  Scenario: Successful login with valid credentials
    Given I open the login page
    When I login with valid credentials
    Then I see the products page
