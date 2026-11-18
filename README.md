# ProSplit 💸

Split group expenses with friends and settle up with the fewest possible payments.

## Features
- Create groups and add members
- Add expenses with equal splits (cent-exact, no rounding errors)
- See who owes whom, simplified to the fewest payments
- Mark debts as paid

## How it works
- **Money is stored in cents (integers)**, because floats can't represent money exactly
  (`0.1 + 0.2 != 0.3`). Leftover cents from uneven splits go to the first person, so totals always match.
- **Debt simplification:** a greedy algorithm repeatedly matches the biggest debtor with the
  biggest creditor. It needs at most n − 1 payments. (Finding the absolute minimum is NP-hard.)
- **Settlements are modeled as expenses**: "A pays B 10 €" is an expense paid by A, split only to B.
  No extra logic needed.

## Tech stack
Python · Streamlit · pytest

## Run locally
    git clone https://github.com/shriyashmistry/ProSplit.git
    cd ProSplit
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    streamlit run app.py

## Tests
    python -m pytest

## Limitations & future work
- Data is stored in a local JSON file (not persistent on Streamlit Cloud) → move to a database
- Only equal splits → add exact amounts / percentages
- Personal budget per category
- Mobile app with Flet
