from core.models import Expense
from core.balances import compute_balances
for e in [
    Expense("Pizza", 1000, "Yash", ["Yash", "Nishant", "Trupesh", "Yash"]),   # 10.00 €
    Expense("Taxi", 1000, "Yash", ["Nishant", "Trupesh"]),             # payer not in split
    Expense("Coffee", 1250, "Nishant", ["Yash", "Nishant", "Trupesh", "Anna"]),  # 12.50 € split 4 ways
]:
    s = e.shares()
    #print(s)
expenses = [
    Expense("Pizza", 3000, "Yash", ["Yash", "Nishant", "Trupesh"]),
    Expense("Taxi", 1200, "Nishant", ["Nishant", "Trupesh"]),
]
b = compute_balances(expenses)
print(b)