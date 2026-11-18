from dataclasses import dataclass

@dataclass
class Expense:
    description: str
    amount_cents: int
    paid_by: str
    split_between: list[str]
    category: str = "Other"

    def __post_init__(self):
        if len(self.split_between) == 0:
            raise ValueError("No User found to split the amount.")
        if self.amount_cents <= 0:
            raise ValueError("Amount must be positive.")
        if len(self.split_between) != len(set(self.split_between)):
            self.split_between = list(dict.fromkeys(self.split_between))

    def shares(self)->dict [str, int]:
        """It returns how much each person owes for this expense."""
        per_person_share, remainder_share = divmod(self.amount_cents, len(self.split_between))
        res = {name: per_person_share for name in self.split_between}
        res[self.split_between[0]] += remainder_share
        return res
