import flet as ft
import httpx  

class Login_View(ft.View):
    
    def __init__(self, page):
        super().__init__(route="/")
        self.page = page  

        # Set a background color (can be customized)
        self.bgcolor = ft.colors.BLUE_GREY_50  

        # FastAPI login endpoint
        self.url = "http://127.0.0.1:8000/login/"

        # UI Elements
        self.heading = ft.Text(
            value="Login",
            size=28,
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

        self.password = ft.TextField(
            password=True,
            can_reveal_password=True, 
            width=300, 
            label="Password", 
            helper_text="Enter your password",
            prefix_icon=ft.icons.LOCK,
            border_radius=10,
            bgcolor=ft.colors.WHITE
        )

        self.l_btn = ft.FilledButton(
            text="Login", 
            icon=ft.icons.LOGIN, 
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor=ft.colors.BLUE_500,
                color=ft.colors.WHITE
            ),
            on_click=self.on_login
        )

        self.register = ft.Container(
            content=ft.Text(
                disabled=False,
                spans=[
                    ft.TextSpan("Don't have an account? "),
                    ft.TextSpan(
                        "Create one",
                        style=ft.TextStyle(
                            decoration=ft.TextDecoration.UNDERLINE,
                            color=ft.colors.BLUE_700,  
                            weight=ft.FontWeight.BOLD  
                        ),
                        on_click=lambda _: self.page.go("/register"),
                    ),
                ],
            ),
            alignment=ft.alignment.center,
            padding=10
        )

        # Card-based design for a professional look
        self.card = ft.Card(
            elevation=6,
            content=ft.Container(
                content=ft.Column(
                    [
                        self.heading,
                        self.id,
                        self.password,
                        self.l_btn,
                        self.register,
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
            ft.Container(
                content=ft.Column(
                    [
                        self.card,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]

        self.horizontal_alignment = "center"
        self.padding = 25
        self.vertical_alignment = "center"

    def on_login(self, e):
        """Handles user login when the button is clicked."""
        print("Login function called")  
        if self.id.value=="" and self.password.value=="":
            print("empty fields") 
            return 
          
        user_data = {
                "id": int(self.id.value) if self.id.value.isdigit() else 0,  
                "password": self.password.value
            }
        
        try:
            with httpx.Client() as client:  
                    response = client.post(self.url, json=user_data)  
                    data = response.json()

            if response.status_code == 200:
               print("Success")
               self.page.go("/dashboard")
            else:
               print("Error:", data["detail"])

        except httpx.RequestError as err:
           print("Network error:", err)

        self.page.update()  