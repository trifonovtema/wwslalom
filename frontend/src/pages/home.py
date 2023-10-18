from flet import (
    Container, Page, alignment, Column, Text, TextField, InputBorder, TextStyle, padding, border
)


class Home(Container):
    def __init__(self, page: Page, auth2_manager):
        super().__init__()
        self.bgcolor = '#4e73df'
        self.expand = True
        self.auth2_manager=auth2_manager
        self.alignment = alignment.center
        self.content = Container(
            alignment=alignment.center,
            on_click=lambda _: page.go('/signup'),
            height=50, width=150,
            bgcolor='white',
            content=Text(
                value='Понеслась',
                size=20,
                color='black'
            )
        )
