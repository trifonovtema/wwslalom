from flet import (
    Container, Page, alignment, Column, Text, TextField, InputBorder, TextStyle, padding, border, IconButton
)
import flet as ft


# from service.auth2 import get_name


class Me(Container):
    def __init__(self, page: Page, auth2_manager):
        super().__init__()
        self.bgcolor = '#4e73df'
        self.expand = True
        self.auth2_manager = auth2_manager
        self.alignment = alignment.center
        self.page = page

        self.expand = True
        self.bgcolor = '#4e73df'
        self.alignment = alignment.center
        self.error_border = border.all(width=1, color='red')
        self.msg = Container(
            content=Text(
                value=f"Ну вот ты и залогинился: {self.auth2_manager.get_name()}!",
                size=16,
                color='black',
                text_align='center'
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
                                value="Йохохо",
                                size=16,
                                color='black',
                                text_align='center'
                            ),

                            self.msg,

                            Container(height=0),

                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Выйти'
                                ),
                                on_click=self.logout
                            ),

                        ]
                    )
                )

            ]
        )

    def logout(self, e):
        self.page.go('/logout')
