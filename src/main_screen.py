import flet as ft
from generator import choice_quote
from quote_screen import QuoteScreen

class MainScreen:
    def __init__(self, pg: ft.Page):
        self.pg = pg
        self.settings_app()
        self.main_menu()

    def settings_app(self):
        self.pg.bgcolor = "#FFFFFF"

        self.pg.theme_mode = ft.ThemeMode.LIGHT
        self.pg.title = 'Gusto'
        self.pg.vertical_alignment = ft.VerticalAlignment.CENTER
        self.pg.horizontal_alignment = ft.CrossAxisAlignment.START
        self.pg.padding = 15

    def _work(self, e):
        quote, author = choice_quote(cat='work')

        self.pg.clean()
        QuoteScreen(self.pg, quote, author)
        self.pg.update()

    def _sport(self, e):
        quote, author = choice_quote(cat='sport')

        self.pg.clean()
        QuoteScreen(self.pg, quote, author)
        self.pg.update()

    def _mentality(self, e):
        quote, author = choice_quote(cat='mental')

        self.pg.clean()
        QuoteScreen(self.pg, quote, author)
        self.pg.update()

    def main_menu(self):
        self.title = ft.Text(value='Gusto', text_align=ft.TextAlign.LEFT, color='#7F9133', size=48, italic=True)
        self.info_text = ft.Text(value='Привет, давай найдем нужный настрой!', color='#000000', size=24)

        self.btn_work = ft.Button(content='Работа', icon=ft.icons.Icons.WORK, width=300, bgcolor='#FFFFFF', style=ft.ButtonStyle(side=ft.BorderSide(0.5, color='#000000')), color='#000000', icon_color='#000000', on_click=lambda e: self._work(e))
        self.btn_sport = ft.Button(content='Спорт', icon=ft.icons.Icons.DIRECTIONS_RUN, width=300, bgcolor='#FFFFFF', style=ft.ButtonStyle(side=ft.BorderSide(0.5, color='#000000')), color='#000000', icon_color='#000000', on_click=lambda e: self._sport(e))
        self.btn_mentality = ft.Button(content='Менталка', icon=ft.icons.Icons.PSYCHOLOGY, width=300, bgcolor='#FFFFFF', style=ft.ButtonStyle(side=ft.BorderSide(0.5, color='#000000')), color='#000000', icon_color='#000000', on_click=lambda e: self._mentality(e))

        self.btn_container = ft.Container(
            content=ft.Column(
                controls=[self.btn_work, self.btn_sport, self.btn_mentality]
            ),
            padding=ft.Padding.only(top=50)
        )

        self.pg.add(self.title, self.info_text, self.btn_container)

def main(page: ft.Page):
    MainScreen(page)

if __name__ == '__main__':
    ft.run(main)