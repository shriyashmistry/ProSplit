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

def simplify_balances(balances: dict[str, int])->list[tuple[str,str,int]]:
    """Return payment as (from_person, to_person, amount_cents)"""
    group = {p: b for p, b in balances.items() if b != 0}
    res = []
    while len(group)>0:
        biggest_creditor = max(group, key= lambda x: group[x])
        biggest_debitor = min(group, key= lambda x: group[x])

        transaction_amount = min((group[biggest_debitor]*-1), group[biggest_creditor])

        res.append((biggest_debitor, biggest_creditor, transaction_amount))

        group[biggest_creditor] -= transaction_amount
        group[biggest_debitor] += transaction_amount

        if group[biggest_debitor]==0: group.pop(biggest_debitor)
        if group[biggest_creditor]==0: group.pop(biggest_creditor)
    return res

