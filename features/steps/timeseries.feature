Feature: Analysis Bitcoin with Ethereum Data by using time series

  Scenario: Should execute trade due to time series analysis

    Given A collection of Ethereum and Bitcoin Data
        When analysis by time series function is called
        Then it will return an "Execute" trade indicator

  Scenario: Should not execute trade due to time series analysis

      Given A collection of Ethereum and Bitcoin Data
        When analysis by time series function is called
        Then it will return a "Do Not Execute" trade indicator