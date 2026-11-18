from core.models import Expense
from core.balances import compute_balances
expenses = [
        Expense("Pizza", 3000, "Yash", ["Yash", "Nishant", "Trupesh"]),
        Expense("Taxi", 1200, "Nishant", ["Nishant", "Trupesh"]),
        Expense("Outing", 50000, "Trupesh", ["Trupesh"]),
    ]

def test_example():
    assert compute_balances(expenses) == {"Yash": 2000, "Nishant": -400, "Trupesh": -1600}

def test_sum():
    assert sum(compute_balances(expenses).values()) == 0

def test_empty_list():
    assert compute_balances([]) == {}
