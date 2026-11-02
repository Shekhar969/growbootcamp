
Feature: Contact Form

  As a portfolio visitor
  I want to send a message
  So that I can contact the portfolio owner

  Scenario: Submit a valid message
    Given the visitor opens the contact section
    When the visitor enters valid information
    And clicks Send Message
    Then the message should be submitted
    And a success message should appear
