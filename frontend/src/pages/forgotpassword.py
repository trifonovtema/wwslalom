import re
from flet import Page,alignment,border,Container,InputBorder,TextField,TextStyle,Column,Text,TapEvent,ProgressBar,SnackBar,padding
# from service.auth2 import store_session, reset_password
from utils.validation import Validator


class ForgotPassword(Container):
    def __init__(self, page: Page, auth2_manager):
        super().__init__()
        page.padding = 0
        self.auth2_manager=auth2_manager
        self.validator = Validator()
        self.expand = True
        self.bgcolor = '#4e73df'
        self.alignment = alignment.center
        self.error_border = border.all(width=1, color='red')
        self.email_box = Container(
            content=TextField(
                value=page.data,
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Enter email address...',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),

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
                        alignment='center',
                        horizontal_alignment='center',
                        controls=[

                            Text(
                                value="Забыли пароль?",
                                size=20,
                                color='black',
                                text_align='center'
                            ),
                            Text(
                                value="Введите ваш email и мы отправим на него ссылку со сбросом пароля:",
                                size=16,
                                color='#858796',
                                text_align='center'
                            ),
                            Container(height=0),

                            self.email_box,
                            Container(height=0),

                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Reset Password'
                                ),
                                on_click=self.reset_password
                            ),
                            Container(height=30),
                            Container(
                                content=Text(
                                    value='Регистрация',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/signup')
                            ),
                            Container(
                                content=Text(
                                    value='Уже есть аккаунт? Войти',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/signup')
                            )
                        ]
                    )
                )

            ]
        )

    def reset_password(self, e: TapEvent):
        pass
        # if not self.validator.is_valid_email(self.email_box.content.value):
        #     self.email_box.border = self.error_border
        #     self.email_box.update()
        if 1==2:
            pass
        else:
            email = self.email_box.content.value
            self.page.splash = ProgressBar()
            self.page.update()

            user = self.auth2_manager.forgot_password(email)
            self.page.splash = None
            self.page.update()
            if user:
                self.page.snack_bar = SnackBar(
                    Text(
                        'Инструкции для сброса пароля отправлены на указанный email.')
                )
                self.page.snack_bar.open = True
                self.page.update()
                self.page.go('/login')
            else:
                self.page.snack_bar = SnackBar(
                    Text(
                        'Неверный email. Попробуйте еще раз через несколько минут')
                )
                self.page.snack_bar.open = True
                self.page.update()
