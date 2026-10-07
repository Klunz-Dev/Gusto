import flet as ft
import re
from main_screen import MainScreen

class LoginScreen:
    def __init__(self, pg: ft.Page):
        self.pg = pg
        self.settings_app()
        self.login_forms()

    def settings_app(self):
        self.pg.bgcolor = "#FFFFFF"

        self.pg.theme_mode = ft.ThemeMode.LIGHT
        self.pg.title = 'Gusto'
        self.pg.vertical_alignment = ft.VerticalAlignment.CENTER
        self.pg.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.pg.padding = ft.Padding.only(top=50)

    def handle_login(self, e):
        name = self.input_name.value.strip()
        email = self.input_mail.value.strip()
        password = self.input_password.value

        if not (3 <= len(name) <= 10):
            return

        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, email):
            return

        if not (8 <= len(password) <= 32):
            return

        self.pg.clean()
        MainScreen(self.pg)
        self.pg.update()

    def login_forms(self):
        self.title_text = ft.Text(value='Gusto', italic=True, color='#7F9133', size=48, weight=ft.FontWeight.W_400)
        self.info_text = ft.Text(value='Gusto. Слова, которые меняют день.', color='#000000', size=16)

        self.input_name = ft.TextField(hint_text='Ваше имя', bgcolor='#FFFFFF', border_radius=100, border_color='#000000', border_width=0.5, width=300, height=40, autofocus=True, cursor_color='#000000', cursor_height=20, cursor_width=1)
        self.input_mail = ft.TextField(hint_text='Ваша почта', bgcolor='#FFFFFF', border_radius=100, border_color='#000000', border_width=0.5, width=300, height=40, autofocus=True, cursor_color='#000000', cursor_height=20, cursor_width=1)
        self.input_password = ft.TextField(hint_text='Пароль', bgcolor='#FFFFFF', border_radius=100, border_color='#000000', border_width=0.5, width=300, height=40, autofocus=True, cursor_color='#000000', cursor_height=20, cursor_width=1, password=True)

        self.btn_login = ft.Button('Войти', icon=ft.icons.Icons.LOGIN_OUTLINED, width=300, bgcolor='#7F9133', color='#000000', icon_color='#000000', height=40, on_click=self.handle_login)

        self.login_container = ft.Container(
            content=ft.Column(
                controls=[self.input_name, self.input_mail, self.input_password],
                spacing=15
            ),
            padding=ft.Padding.only(top=50, bottom=50)
        )

        self.pg.add(self.title_text, self.info_text, self.login_container, self.btn_login)

def main(page: ft.Page):
    LoginScreen(page)

if __name__ == '__main__':
    ft.run(main)
