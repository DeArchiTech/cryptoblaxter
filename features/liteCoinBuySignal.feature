Feature: Determine LiteCoin Buy Signal

  Scenario: Computing Execution Signal For LiteCoin

    Given A time in space
        When ComputeLiteCoinBuySignal is called
        Then An ExecutionSignal will be returned