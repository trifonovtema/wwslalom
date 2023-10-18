import pickle
import flet as ft
from pages.home import Home
from pages.forgotpassword import ForgotPassword
# from pages.dashboard import Dashboard
from pages.login import Login
from pages.signup import Signup
from pages.me import Me
from service.auth2 import Auth2Manager
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BACKEND_URL = "http://backend:8000"

AUTH2_URL = BACKEND_URL
CLIENT_STORAGE_PREFIX = "wwslalom."

DEFAULT_FLET_PATH = ""  # or 'ui/path'
DEFAULT_FLET_PORT = 8080


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        page.padding = 0
        self.page = page
        self.auth2_manager = Auth2Manager(auth2_url=AUTH2_URL,
                                          client_storage_prefix=CLIENT_STORAGE_PREFIX,
                                          page=page)
        self.init()

    def init(self):
        self.page.on_route_change = self.on_route_change
        self.page.go("/")

        #
        # if "error" in res:
        #     print(res["error"])
        #     self.page.go("/login")
        # else:
        #     self.page.go("/me")

    def on_route_change(self, route):
        routes = {
            "/": Home,
            "/login": Login,
            "/signup": Signup,
            "/me": Me,
            "/forgotpassword": ForgotPassword,
            "/logout": Login
        }

        if self.page.route == "/logout":
            self.auth2_manager.logout()
            self.page.route = "/login"

        if self.auth2_manager.is_authenticated():
            if self.page.route in ["/login", "/signup"]:
                self.page.route = "/me"
        else:
            if self.page.route == "/me":
                self.page.route = "/login"

        new_page = routes[self.page.route](page=self.page, auth2_manager=self.auth2_manager)

        self.page.views.clear()
        self.page.views.append(
            ft.View(route, [new_page])
        )

        self.page.go(self.page.route)


flet_path = DEFAULT_FLET_PATH  # os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
flet_port = DEFAULT_FLET_PORT  # int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
ft.app(name=flet_path, target=Main, view=ft.AppView.WEB_BROWSER, port=flet_port)
