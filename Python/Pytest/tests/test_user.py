import pytest
import logging

from pages.user1 import (
    checkItemInStock,
    userName,
    balance,
    itemsPrachased,
    itemsInStock,
    calcTotal,
    suffentbalance
)

# Configure logging
logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def test_check_username_length():
    logger.info("Checking username length")
    assert len(userName) < 30
    logger.info("Username length is valid")


def test_check_username_Invaild_Chr():
    logger.info("Checking username for invalid characters")
    assert not any(char in "!@#$%^&*?{}|" for char in userName)
    logger.info("Username contains no invalid characters")


@pytest.mark.parametrize("balance", [2000, 3000, 5000])
def test_balance(balance):
    logger.info(f"Checking balance: {balance}")
    assert balance > 0
    logger.info("Balance is valid")


def test_check_balance():
    logger.info("Checking balance data type")
    assert isinstance(balance, int)
    logger.info("Balance is an integer")


def test_item_prachased_type():
    logger.info("Checking purchased items data type")
    assert isinstance(itemsPrachased, tuple)
    logger.info("Purchased items are stored as a tuple")


def test_item_prachased_itemsType():
    logger.info("Checking purchased item types")
    assert all(isinstance(item, str) for item in itemsPrachased)
    logger.info("All purchased items are strings")


def test_item_in_stock():
    logger.info("Checking items in stock data type")
    assert isinstance(itemsInStock, dict)
    logger.info("Items in stock are stored as a dictionary")


def test_check_Item_In_Stock():
    logger.info("Checking item availability")
    checkItemInStock()
    logger.info("Item availability check completed")


def test_total_cal():
    logger.info("Calculating total price")
    assert calcTotal()
    logger.info("Total calculation completed successfully")


def test_suffesent_balance():
    logger.info("Checking sufficient balance")
    assert suffentbalance() is True
    logger.info("Sufficient balance check passed")
