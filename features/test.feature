# Created by eduardoreynoso at 4/4/19
Feature: Test

  Scenario: Test open browser
    Given I open the browser
    And I access the given URL
    And I verify that the text "Google" is present