import json
from dataclasses import asdict
from pathlib import Path

from core.models import Expense, Group


def save_expenses(expenses: list[Expense], path: Path) -> None:
    with open(path, 'w') as f:
        json.dump([asdict(e) for e in expenses], f, indent=2)

def load_expenses(path: Path) -> list[Expense]:
    if path.exists() and not path.stat().st_size == 0:
        with open(path, 'r') as f:
            expenses = json.load(f)
            return [Expense(**d) for d in expenses]
    return []

def save_group(group: list[Group], path: Path) -> None:
    with open(path, 'w') as f:
        json.dump([asdict(g) for g in group], f, indent=2)

def load_group(path: Path) -> list[Group]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with open(path, 'r') as f:
        d = json.load(f)
        return [Group(g["name"], g["members"], [Expense(**x) for x in g["expenses"]]) for g in d]
