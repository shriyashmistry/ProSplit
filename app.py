from pathlib import Path

import streamlit as st

from core.balances import compute_balances, simplify_balances
from core.models import Expense, Group
from core.storage import load_group, save_group

DATA_PATH = Path("groups.json")
groups = load_group(DATA_PATH)

# --- Sidebar: create group ---
st.sidebar.header("Groups")
new_group = st.sidebar.text_input("New group name")
if st.sidebar.button("Create group"):
    name = new_group.strip()
    if not name:
        st.sidebar.error("Please enter a group name.")
    elif name in [g.name for g in groups]:
        st.sidebar.error("A group with this name already exists.")
    else:
        groups.append(Group(name, []))
        save_group(groups, DATA_PATH)
        st.rerun()

if not groups:
    st.info("Create a group in the sidebar to get started.")
    st.stop()          # stops the script here, so nothing below runs

# --- Sidebar: pick group ---
selected = st.sidebar.selectbox("Select group", [g.name for g in groups])
group = next(g for g in groups if g.name == selected)

# --- Sidebar: add member ---
new_member = st.sidebar.text_input("Add member")
if st.sidebar.button("Add member"):
    try:
        group.add_member(new_member)
        save_group(groups, DATA_PATH)
        st.rerun()
    except ValueError as err:
        st.sidebar.error(str(err))
st.sidebar.write("Members:", ", ".join(group.members) or "none yet")

if not group.members:
    st.info("Add members in the sidebar.")
    st.stop()

st.title(f"ProSplit 💸 – {group.name}")

#---Add Expense---
st.header("Add expense")
with st.form("add_expense", clear_on_submit=True):
    description = st.text_input("Description")
    amount = st.number_input("Amount (€)", min_value=0.0, step=0.5)
    paid_by = st.selectbox("Paid by", group.members)
    split_between = st.multiselect("Split between", group.members, default=group.members)
    category = st.selectbox("Category", ["Food", "Transport", "Rent", "Fun", "Other"])
    submitted = st.form_submit_button("Add")

if submitted:
    amount_cents = round(amount * 100)
    try:
        e = Expense(description, amount_cents, paid_by, split_between, category)
        group.add_expense(e)
    except ValueError as err:
        st.error(str(err))
    else:
        save_group(groups, DATA_PATH)
        st.success(f"Added {description}!")

# --- Expenses list ---
st.header("Expenses")
for e in group.expenses:
    st.write(f"{e.description} - {e.amount_cents / 100:.2f}€ paid by {e.paid_by}")

# --- Settle up ---
st.header("Who pays whom")
res = simplify_balances(compute_balances(group.expenses))
if len(res)==0:
    st.info("All settled up!")
else:
    for s,r,a in res:
        st.write(f"{s} pays {r} {a/100:.2f} €")