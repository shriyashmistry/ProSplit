from core.models import Expense
from core.balances import compute_balances, simplify_balances
expenses = [
        Expense("Pizza", 3000, "Yash", ["Yash", "Nishant", "Trupesh"]),
        Expense("Taxi", 1200, "Nishant", ["Nishant", "Trupesh"]),
        Expense("Outing", 50000, "Trupesh", ["Trupesh"]),
]
sample_dict_1 = {'Yash': 2000, 'Nishant': -400, 'Trupesh': -1600}
sample_dict_2 = {'Anna' : 500, 'Banna': -500}
sample_dict_3 = {'Trupesh' : 0, 'Nishant' : 0}
sample_dict_4 = {'A': -100, 'B': -100, 'C': 50, 'D': 150}

def test_example_compute_balances():
    assert compute_balances(expenses) == {"Yash": 2000, "Nishant": -400, "Trupesh": -1600}

def test_sum():
    assert sum(compute_balances(expenses).values()) == 0

def test_empty_list():
    assert compute_balances([]) == {}

def test_example_simplification1():
    assert simplify_balances(sample_dict_1) == [('Trupesh', 'Yash', 1600),('Nishant', 'Yash', 400)]

def test_example_simplification2():
    assert simplify_balances(sample_dict_2) == [('Banna', 'Anna', 500)]

def test_example_simplification3():
    assert simplify_balances(sample_dict_3) == []


def test_empty_simplification():
    assert simplify_balances({}) == []

def test_sum_simplification():
    rest = dict(sample_dict_1)
    for(s,r,a) in simplify_balances(sample_dict_1):
        rest[s] += a
        rest[r] -= a
    assert all(v == 0 for v in rest.values())

def test_no_of_transactions():
    assert len(simplify_balances(sample_dict_1)) <= len(sample_dict_1)-1

def test_four_people():
    rest = dict(sample_dict_4)
    for s, r, a in simplify_balances(sample_dict_4):
        assert a > 0
        rest[s] += a
        rest[r] -= a
    assert all(v == 0 for v in rest.values())