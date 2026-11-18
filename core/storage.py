import json
from dataclasses import asdict
from pathlib import Path

from core.models import Expense

def save_expenses(expenses: list[Expense], path: Path) -> None:
    with open(path, 'w') as f:
        for e in expenses:
            json.dump(asdict(e), f, indent=2)

def load_expenses(path: Path) -> list[Expense]:
    if path.exists():
        with open(path, 'r') as f:
            expenses = json.load(f)
            return list(Expense(**expenses))
    return []