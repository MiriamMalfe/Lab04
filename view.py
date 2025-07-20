import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.lingua = None
        self.row1 = None
        self.row2=None
        self.mod=None
        self.frase=None
        self.b1=None
        self.row3=None
        self.ris = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self.lingua = ft.Dropdown(label="select language",
                                  options=[ft.dropdown.Option("Italian"), ft.dropdown.Option("English"),
                                           ft.dropdown.Option("Spanish")], width=800)
        self.row1 = ft.Row([self.lingua], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(self.row1)
        self.mod = ft.Dropdown(label="Select mode", options=[ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic"), ft.dropdown.Option("Default")] )
        self.frase = ft.TextField(label= "Inserire una frase")
        self.b1 = ft.ElevatedButton(text="Spell check", on_click= self.__controller.handleSentence)
        self.row2 = ft.Row([self.mod, self.frase,self.b1], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(self.row2)
        self.ris = ft.ListView(expand=True)
        self.row3=ft.Row([self.ris])
        self.page.controls.append(self.row3)
        # Add your stuff here


        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )


        self.page.update()

