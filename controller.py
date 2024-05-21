import flet as ft
from view import second_root
import json
from model import translate_from

with open('languages.json') as json_file:
    data = json.load(json_file)
    lang1 = data['Language1']
    lang2 = data['Language2']

def main(page: ft.Page):
    page.title = 'Helptranslate'
    page.scroll = "always"
    def translate1(n):
        text = tb5.value
        translate = translate_from(text)

        new = ft.Row(
            [
                ft.Container(
                    content=ft.Text(f'{translate}'),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREY_700,
                    width=150,
                    height=150,
                    border_radius=10,
                ),])

        page.add(new)
        page.update(new)

    text1 = ft.Text(f'Your language: {lang1}\nOther language: {lang2}')
    tb5 = ft.TextField(label="Text", icon=ft.icons.TRANSLATE)
    btn1 = ft.ElevatedButton(f"Submit", data=0, width=250, height=70, on_click=translate1)

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0:
            page.add(text1, tb5, btn1)
            page.update()

        elif index == 1:
            page.add(second_root(page))
            page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(label='Main', icon=ft.icons.HOUSE),
            ft.NavigationDestination(label='Settings', icon=ft.icons.SETTINGS),
        ], on_change=navigate
    )

    page.add(text1, tb5, btn1)

ft.app(main)
