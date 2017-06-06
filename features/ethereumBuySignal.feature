Feature: Determine Ethereum Buy Signal

  Scenario: Given historical data of Ehtereum and Bitcoin

    Given A historical data of ethereum, bitcoin and time
        When determineBuySignalForEthereum is called
        Then It will return a ExecutionSignal Signal
