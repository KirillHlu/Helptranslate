import flet as ft
import json


def second_root(page: ft.Page):
    def safe(e):
        languages = {}
        languages['Language1'] = language1.value
        languages['Language2'] = language2.value
        with open('languages.json', 'w') as file:
            json.dump(languages, file)
    page.title = "Containers - clickable and not"
    language1 = ft.TextField(label="My language", icon=ft.icons.TRANSLATE)
    language2 = ft.TextField(label="Other language", icon=ft.icons.TRANSLATE)
    btn1 = ft.ElevatedButton(f"Submit", data=0, width=250, height=70, on_click=safe)
    page.add(language1, language2, btn1)
    return page
