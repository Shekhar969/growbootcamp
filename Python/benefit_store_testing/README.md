# Playwright Pytest Automation

 This project automates the **CoreEnroll QA application** using **Playwright, Pytest, and Allure**.

 ## Setup

 Create and activate a virtual environment:

```
python3 -m venv .env
source .env/bin/activate
```

 Install dependencies:

```
pip install -r requirements.txt
playwright install
```

 ## Verify Installation

```
python --version
pytest --version
playwright --version
allure --version
```

 ## Run Tests

```
pytest --headed -s --alluredir=allure-results ./tests
```

 ## View Allure Report

```
allure serve allure-results
```

 ## Test Coverage

 - User registration
- Login
- Form validation
- User workflows
- Application navigation

 ## Application

 https://qa-enroll.corenroll.com/