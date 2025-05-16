import flet as ft
import httpx  # Using httpx instead of requests

class register_view(ft.View):
    
    def __init__(self, page):
        super().__init__(route="/register")
        self.page = page  
        self.url = "http://127.0.0.1:8000/register/"  

        # Page Background Color
        self.bgcolor = ft.colors.BLUE_GREY_50  

        # App Bar
        self.app_bar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                on_click=lambda _: self.page.go("/")
            ),
            title=ft.Text("Register Yourself"),
            center_title=True,
            bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE
        )

        # UI Elements
        self.heading = ft.Text(
            value="Create an Account",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE_GREY_800
        )

        self.id = ft.TextField(
            width=300, 
            label="ID", 
            helper_text="Enter your ID",
            prefix_icon=ft.icons.PERSON,
            border_radius=10,
            bgcolor=ft.colors.WHITE
        )

        self.name = ft.TextField(
            width=300, 
            label="Name", 
            helper_text="Enter your Name",
            prefix_icon=ft.icons.BADGE,
            border_radius=10,
            bgcolor=ft.colors.WHITE
        )

        self.password = ft.TextField(
            can_reveal_password=True,
            width=300, 
            label="Password", 
            helper_text="Enter a password",
            prefix_icon=ft.icons.LOCK,
            border_radius=10,
            bgcolor=ft.colors.WHITE
        )

        self.r_btn = ft.FilledButton(
            text="Register", 
            icon=ft.icons.CHECK_CIRCLE, 
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor=ft.colors.BLUE_500,
                color=ft.colors.WHITE
            ),
            on_click=self.on_register
        )

        # Card Layout (Consistent with Login UI)
        self.card = ft.Card(
            elevation=6,
            content=ft.Container(
                content=ft.Column(
                    [
                        self.heading,
                        self.id,
                        self.name,
                        self.password,
                        self.r_btn,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                padding=30,
                width=380,
                bgcolor=ft.colors.WHITE,
                border_radius=15,
                shadow=ft.BoxShadow(blur_radius=8, color=ft.colors.GREY_400)
            )
        )

        # Layout with centered content
        self.controls = [
            self.app_bar,
            ft.Container(
                content=ft.Column(
                    [self.card],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]

    def on_register(self, e):
        """Handles user registration when the button is clicked."""
        print("Register function called")  

        user_data = {
            "id": int(self.id.value) if self.id.value.isdigit() else 0,  
            "name": self.name.value,
            "password": self.password.value
        }

        try:
            with httpx.Client() as client:  
                response = client.post(self.url, json=user_data)  
                data = response.json()
                print(data)

            if response.status_code == 200:
                print("Success")
                self.page.go("/login")  # Redirect to login after successful registration
            else:
                print("Error:", data["detail"])

        except httpx.RequestError as err:
            print("Network error:", err)

        self.page.update()  
