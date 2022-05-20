Feature: I start the connect 4 game
Scenario: simple test
    Given I start the game
    When  The board and the game name appears
    And I choose X
    And I enter 1
    And I enter 2
    Then I am prompted to enter next move