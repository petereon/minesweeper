Feature: Sunk vessel

    Scenario Outline: Checking the sunk vessel status
        Given I have sunk a vessel <vessel_type> starting at <start_hole>
        And I have shot at <shot_hole>
        When the game checks the sunk vessel status
        Then I know that the vessel <vessel_type> has been sunk

        Examples:
            | vessel_type | start_hole | shot_hole |
            | carrier     | A4         | A6        |
            | battleship  | J2         | J5        |
            | cruiser     | D5         | D6        |
            | submarine   | F6         | F7        |


    Scenario: Game starts out with an empty sunk vessel indicator
        Given I have an empty target grid
        When game checks sunk vessel indicator
        Then it contains 5 empty holes