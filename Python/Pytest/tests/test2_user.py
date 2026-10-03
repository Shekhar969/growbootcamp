import pytest
import allure

from pages.user1 import (
    checkItemInStock,
    userName,
    balance,
    itemsPrachased,
    itemsInStock,
    calcTotal,
    suffentbalance
)


# ============================================================
# USER VALIDATION
# ============================================================

@allure.feature("User Validation")
@allure.story("Username")
@allure.title("Verify username length")
@allure.severity(allure.severity_level.NORMAL)
def test_username_length():

    with allure.step("Check username length"):
        assert len(userName) < 30


@allure.feature("User Validation")
@allure.story("Username")
@allure.title("Verify username does not contain invalid characters")
@allure.severity(allure.severity_level.NORMAL)
def test_username_invalid_characters():

    invalid_characters = "!@#$%^&*?{}|"

    with allure.step("Check username characters"):
        assert not any(
            char in invalid_characters
            for char in userName
        )


# ============================================================
# BALANCE
# ============================================================

@allure.feature("Balance")
@allure.story("Balance Validation")
@allure.title("Verify balance is greater than zero")
@allure.severity(allure.severity_level.NORMAL)
def test_balance_greater_than_zero():

    with allure.step("Check balance"):
        assert balance > 0


@allure.feature("Balance")
@allure.story("Balance Validation")
@allure.title("Verify balance is an integer")
@allure.severity(allure.severity_level.NORMAL)
def test_balance_is_integer():

    with allure.step("Check balance type"):
        assert isinstance(balance, int)


# ============================================================
# ITEMS
# ============================================================

@allure.feature("Items")
@allure.story("Purchased Items")
@allure.title("Verify purchased items are stored as tuple")
def test_purchased_items_type():

    with allure.step("Check purchased items type"):
        assert isinstance(itemsPrachased, tuple)


@allure.feature("Items")
@allure.story("Stock")
@allure.title("Verify items in stock are stored as dictionary")
def test_items_in_stock_type():

    with allure.step("Check stock type"):
        assert isinstance(itemsInStock, dict)


@allure.feature("Items")
@allure.story("Stock")
@allure.title("Verify purchased items are available in stock")
@allure.severity(allure.severity_level.CRITICAL)
def test_purchased_items_in_stock():

    available_items = checkItemInStock()

    with allure.step("Check available purchased items"):
        assert len(available_items) > 0


# ============================================================
# SHOPPING
# ============================================================

@allure.feature("Shopping")
@allure.story("Total Calculation")
@allure.title("Verify total price calculation")
@allure.severity(allure.severity_level.CRITICAL)
def test_total_calculation():

    total = calcTotal()

    with allure.step("Check total price"):
        assert total == 2500


@allure.feature("Shopping")
@allure.story("Balance Check")
@allure.title("Verify user has sufficient balance")
@allure.severity(allure.severity_level.CRITICAL)
def test_sufficient_balance():

    result = suffentbalance()

    with allure.step("Check sufficient balance"):
        assert result is True
