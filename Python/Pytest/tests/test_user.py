import pytest 
from pages.user1 import checkItemInStock,userName,balance,itemsPrachased,itemsInStock,calcTotal,suffentbalance

def test_check_username_length():
     assert len(userName)<30

def test_check_username_Invaild_Chr():
    assert not any(char in "!@#$%^&*?{}|" for char in userName)

# @pytest.fixture
# def balance():
#     return 3000


@pytest.mark.parametrize("balance", [2000, 3000, 5000])
def test_balance(balance):
    assert balance > 0

 
def test_check_balance():
    assert isinstance(balance, int) 

def test_item_prachased_type():
    assert isinstance(itemsPrachased,tuple) 

def test_item_prachased_itemsType():
    assert all(isinstance(item, str) for item in itemsPrachased)

def test_item_in_stock():
    assert isinstance(itemsInStock,dict)

def test_check_Item_In_Stock():
    checkItemInStock()

def test_total_cal():
    assert calcTotal()

def test_suffesent_balance():
    assert suffentbalance() == True

