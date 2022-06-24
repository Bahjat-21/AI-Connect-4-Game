Feature: Connect 4
Scenario: player X wins
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 2
    And Load old game: n
    And Board and game name appears
    And Player X enters column 1
    And Player O enters column 7
    And Player X enters column 1
    And Player O enters column 2
    And Player X enters column 1
    And Player O enters column 2
    And Player X enters column 1
    Then Player X wins

Scenario: player 0 wins
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 2
    And Load old game: n
    And Board and game name appears
    And Player X enters column 7
    And Player O enters column 1
    And Player X enters column 2
    And Player O enters column 1
    And Player X enters column 3
    And Player O enters column 1
    And Player X enters column 4
    And Player O enters column 1
    Then Player O wins

Scenario: Its a draw
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 2
    And Load old game: n
    And Board and game name appears
    And Player X enters column 1
    And player O enters column 1
    And Player X enters column 1
    And player O enters column 1
    And Player X enters column 1
    And player O enters column 1
    And Player X enters column 3
    And player O enters column 2
    And Player X enters column 2
    And player O enters column 2
    And Player X enters column 2
    And player O enters column 2
    And Player X enters column 2
    And player O enters column 3
    And Player X enters column 3
    And player O enters column 3
    And Player X enters column 3
    And player O enters column 3
    And Player X enters column 5
    And player O enters column 5
    And Player X enters column 4
    And player O enters column 4
    And Player X enters column 4
    And player O enters column 4
    And Player X enters column 4
    And player O enters column 4
    And Player X enters column 5
    And player O enters column 5
    And Player X enters column 5
    And player O enters column 5
    And Player X enters column 7
    And player O enters column 6
    And Player X enters column 6
    And player O enters column 6
    And Player X enters column 6
    And player O enters column 6
    And Player X enters column 6
    And player O enters column 7
    And Player X enters column 7
    And player O enters column 7
    And Player X enters column 7
    And player O enters column 7
    Then Its a draw

Scenario: Column full
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 2
    And Load old game: n
    And Board and game name appears
    And Player X enters column 1
    And player O enters column 1
    And Player X enters column 1
    And player O enters column 1
    And Player X enters column 1
    And player O enters column 1
    And Player X enters column 1
    Then Column full


Scenario: Entering a number that is too big
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 2
    And Load old game: n
    And Player X enters column 9
    Then input to large error

Scenario: loading saved game
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 2
    And Load old game: y
    Then old game loaded

Scenario: saving game
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 2
    And Load old game: n
    And Player X enters column 1
    And player O enters column 1
    And Player X enters column 1
    And Player O enters close
    Then game closed

Scenario: AI vs Player
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 1
    And Load old game: n
    And Player X enters column 1
    And Player X enters column 3
    And Player X enters column 7
    And Player X enters column 5
    And Player X enters column 2
    And Player X enters column 2
    Then AI wins

Scenario: AI vs AI
    Given I start the game
    When  The Instructions appear
    And I choose game mode: 3
    And Load old game: n
    Then AI 1 wins