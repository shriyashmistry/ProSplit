from pathlib import Path
import flet as ft
from core.storage import load_group, save_group

DATA_PATH = Path("groups.json")


def main(page: ft.Page):
    page.title = "ProSplit"
    groups = load_group(DATA_PATH)

    group_list = ft.Column()

    def refresh():
        group_list.controls.clear()
        for g in groups:
            group_list.controls.append(ft.Text(f"{g.name} - {len(g.members)} Members"))
        page.update()

    page.add(
        ft.Text("ProSplit 💸", size=28, weight=ft.FontWeight.BOLD),
        group_list,
    )
    refresh()


ft.run(main)