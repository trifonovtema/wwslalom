import re
from flet import (Page, alignment, border, Container, Column, TextField, InputBorder, TextStyle, padding, Text,
                  ProgressBar, SnackBar)
from service.auth2 import Auth2Manager
from utils.validation import Validator


class Signup(Container):
    def __init__(self, page: Page, auth2_manager: Auth2Manager):
        super().__init__()
        page.padding = 0
        self.validator = Validator()
        self.expand = True
        self.auth2_manager = auth2_manager
        self.bgcolor = '#4e73df'
        self.alignment = alignment.center
        self.error_border = border.all(width=1, color='red')

        self.name_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Full name',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),

            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        self.email_box = Container(
            content=TextField(
                # on_focus=self.input_on_focus,
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Введите email...',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),

            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),
                hint_text='Пароль',
                cursor_color='#858796',
                password=True,

            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    border_radius=12,
                    padding=40,
                    bgcolor='white',
                    content=Column(
                        horizontal_alignment='center',
                        controls=[

                            Text(
                                value="Регистрация",
                                size=20,
                                color='black',
                                text_align='center'
                            ),
                            Container(height=0),

                            # self.name_box,
                            # Container(height=0),
                            self.email_box,

                            self.password_box,

                            Container(height=10),

                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Регистрация'
                                ),
                                on_click=self.signup
                            ),
                            Container(
                                content=Text(
                                    value='Забыли пароль?',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go(
                                    '/forgotpassword')
                            ),
                            Container(
                                content=Text(
                                    value='Уже есть аккаунт? Войти',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/login')
                            )
                        ]
                    )
                )

            ]
        )

    def signup(self, e):
        if 1 == 2:
            pass
        # if not self.validator.validate_name(self.name_box.content.value):
        #     self.name_box.border = self.error_border
        #     self.name_box.update()
        #
        # if not self.validator.is_valid_email(self.email_box.content.value):
        #     self.email_box.border = self.error_border
        #     self.email_box.update()
        #
        # if not self.validator.is_valid_password(self.password_box.content.value):
        #     self.password_box.border = self.error_border
        #     self.password_box.update()

        else:
            # name = self.name_box.content.value
            email = self.email_box.content.value
            password = self.password_box.content.value

            self.page.splash = ProgressBar()
            self.page.update()

            res = self.auth2_manager.register_user_with_email_password(email, password)
            print(f"res={res}")
            self.page.splash = None
            if "error" in res:
                self.page.snack_bar = SnackBar(
                    Text('Не удалось залогиниться')
                )
                self.page.snack_bar.open = True
                self.page.update()
            elif "detail" in res and res["detail"] == "REGISTER_USER_ALREADY_EXISTS":
                self.page.snack_bar = SnackBar(
                    Text('Пользователь с таким email уже существует')
                )
                self.page.snack_bar.open = True
                self.page.update()
            elif "detail" in res:
                self.page.snack_bar = SnackBar(
                    Text(f"""{res["detail"]}""")
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                self.page.go('/me')

    def input_on_focus(self, e):
        e.control.border = border.all(width=1, color='#bdcbf4')
        e.control.update()
