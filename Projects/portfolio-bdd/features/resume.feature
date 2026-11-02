Feature: Resume Download

  As a portfolio visitor
  I want to view or download the resume
  So that I can review professional qualifications

  Scenario: Visitor opens resume PDF
    Given the visitor opens the portfolio
    When the visitor clicks the Resume link
    Then the resume PDF should open in a new tab
    And the PDF should load successfully