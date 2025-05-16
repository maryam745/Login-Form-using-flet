import flet as ft

def route_change(route_event, page):
    route = route_event.route
    print("Route change:", route)
    page.views.clear()  # Clear previous views to avoid memory leaks
    if route == "/":
        # Lazy import for Home view
        from login import Login_View
        page.views.append(Login_View(page))  # Add the Home view to page views
    elif route == "/register":
        from Register import register_view
        page.views.append(register_view(page))
    elif route == "/dashboard":
        from dashboard import dashboard_view
        page.views.append(dashboard_view(page))
    else:
        # Fallback for undefined routes
        page.views.append(
            ft.View(
                route="/404",
                controls=[
                    ft.Text("404", size=80, weight="bold", text_align="center"),
                    ft.Text("Page Not Found", size=26, text_align="center"),
                    ft.FilledButton(
                        "Return Home",
                        style=ft.ButtonStyle(
                            bgcolor='black',
                            color='white',
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        on_click=lambda _: page.go("/"),
                    ),
                ],
                horizontal_alignment="center",
                vertical_alignment="center",
            ),
        )
    page.update()  # Update the page to reflect changes
def view_pop(view, page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)

def main(page: ft.Page):
    page.title = "Routes Example"
    page.on_route_change = lambda route: route_change(route, page)
    page.on_view_pop = lambda view: view_pop(view, page)
    page.go(page.route)
    page.theme_mode = 'light'
    page.window.width = 370
    page.window.always_on_top = True
    page.update()  # Ensure the page is updated when the app starts

# Run the app
ft.app(target=main)
