import flet as ft
from generator import choice_quote

class QuoteScreen:
    def __init__(self, pg: ft.Page, quote: str, author: str):
        self.pg = pg
        self.settings_app()
        self.quote_screen(quote, author)

    def settings_app(self):
        self.pg.bgcolor = "#FFFFFF"

        self.pg.theme_mode = ft.ThemeMode.LIGHT
        self.pg.title = 'Gusto'
        self.pg.vertical_alignment = ft.VerticalAlignment.CENTER
        self.pg.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.pg.padding = 15

    def back(self, e):
        self.pg.clean()
        from main_screen import MainScreen

        MainScreen(self.pg)
        self.pg.update()

    def quote_screen(self, quote, author):
        self.quote = ft.Text(value=f'<<{quote}>>', italic=True)
        self.author = ft.Text(value=author, weight=ft.FontWeight.BOLD)

        self.btn_back = ft.Button(content='Назад', icon=ft.icons.Icons.ARROW_BACK, width=300, bgcolor='#FFFFFF', style=ft.ButtonStyle(side=ft.BorderSide(0.5, color='#000000')), color='#000000', icon_color='#000000', on_click=lambda e: self.back(e))

        self.pg.add(ft.Column(controls=[
            ft.Container(
                content=ft.Column([self.quote, self.author], alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.Alignment.CENTER,
                expand=True,
            ),
            self.btn_back
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER))

def main(page: ft.Page):
    QuoteScreen(page)

if __name__ == '__main__':
    ft.run(main)