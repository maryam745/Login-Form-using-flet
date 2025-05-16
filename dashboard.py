import flet as ft
#from helper import *
class dashboard_view(ft.View):
    def __init__(self, page):
        super().__init__(route="/dashboard")
        self.page = page  # Store reference to the main page
        self.text=ft.Text(value="Dashboard",size=45)
        self.controls = [self.text,
                         ft.AppBar(
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                on_click=lambda _: self.page.go("/")
            ),
            title=ft.Text("Dashboard"),
            center_title=True,
            bgcolor=ft.colors.BLUE_700
        )
        ]
        self.horizontal_alignment = "center"
        self.padding = 25
        self.vertical_alignment = "center" 