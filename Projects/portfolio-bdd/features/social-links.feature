
Feature: Social Media Links

  As a portfolio visitor
  I want to visit social media profiles
  So that I can connect with the portfolio owner

  Scenario: Open social profile
    Given the visitor is on the portfolio
    When the visitor clicks a social media link
    Then the correct social profile should open
