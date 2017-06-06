Feature: Determine Ethereum Buy Signal

  Scenario: Computing Execution Signal For Ehereum

    Given A time in space
        When ComputeEthereiumBuySignal is Called
        Then An ExecutionSignal will be returned
