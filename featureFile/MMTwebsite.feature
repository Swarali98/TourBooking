
Feature: The Booking of a vacation tour package

  @TestCase01 @Regression
  Scenario: To book a flight for given dates and destination.
    Given Navigate to MMT-Flights website
    When Search Flights for a round trip of Pune-Delhi-Pune and dates 30th Jan - 31th Jan
    When Add filters on the flight details page
    Then Store all the searched results in an excel file

  @TestCase02 @Regression
  Scenario: To book a hotel for given dates and location
    Given Navigate to MMT-Hotels website
    When Search Hotels for Delhi location and dates 30th Jan - 31th Jan
    When Add filters on the hotel details page
    Then Store all the searched hotel results in an excel file
