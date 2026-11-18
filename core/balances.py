from collections import defaultdict

from core.models import Expense


def compute_balances(expenses: list[Expense])->dict[str, int]:
    """"Net balance per person in cents"""
    res = defaultdict(int)
    for e in expenses:
        shares = e.shares()
        for person in e.split_between:
            res[person] -= shares[person]
        res[e.paid_by] += e.amount_cents
    return dict(res)