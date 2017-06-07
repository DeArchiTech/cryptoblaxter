Feature: Allows a user to use time series, a set of input as trainning data
  and output its timeseries prediction

  Scenario: Computing its timeseries forecast

    Given A time in space
        When timeSeriesForecast is called
        Then 138 will be returned
