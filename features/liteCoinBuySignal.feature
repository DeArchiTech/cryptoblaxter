Feature: Determine LiteCoin Buy Signal

  Scenario: Given historical data of Litecoin and Bitcoin

    Given A historical data of litecoin, bitcoin and time
        When determineBuySignalForLitecoin is called
        Then It will return a ExecutionSignal