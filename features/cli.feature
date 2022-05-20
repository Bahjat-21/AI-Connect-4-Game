Feature: I start the connect 4 game
Scenario: simple test
    Given I start the game
    When  The board and the game name appears
    And I choose X as my player
    And I enter column 1
    And I enter column 8
    Then I check the row a 