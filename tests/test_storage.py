from core.models import Expense, Group
from core.storage import save_expenses, load_expenses
from core.storage import save_group, load_group


def test_roundtrip(tmp_path):
    path = tmp_path / "data.json"
    expenses = [Expense("Pizza", 3000, "Yash", ["Yash", "Nishant"])]
    save_expenses(expenses, path)
    assert load_expenses(path) == expenses

def test_missing_file(tmp_path):
    assert load_expenses(tmp_path / "nope.json") == []


def test_groups_roundtrip(tmp_path):
    path = tmp_path / "groups.json"
    g1 = Group("Trip", ["Yash", "Nishant"])
    g1.add_expense(Expense("Pizza", 3000, "Yash", ["Yash", "Nishant"], "Food"))
    g2 = Group("Flat", ["Yash", "Trupesh"])
    save_group([g1, g2], path)
    assert load_group(path) == [g1, g2]


def test_empty_file(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text("")
    assert load_group(path) == []
    assert load_expenses(path) == []