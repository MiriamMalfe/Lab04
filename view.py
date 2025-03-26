import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.__btn = None
        self.__text = None
        self.__dd1 = None
        self.__dd = None
        self.txtOut = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="pink")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        self.__dd = ft.Dropdown(label="Select language", options=[ft.dropdown.Option(key ="Italian", content = ft.Text(value = "Italian", color="pink")),
                                                                       ft.dropdown.Option(key="English", content=ft.Text(value="English", color="pink")),
                                                   ft.dropdown.Option(key="Spanish", content=ft.Text(value="Spanish", color="pink"))], width=750)

        self.page.controls.append(ft.Row(controls=[self.__dd], alignment=ft.MainAxisAlignment.CENTER))
        #self.page.add([])
        self.page.update()

        self.__dd1 = ft.Dropdown(label = "Search modality", options=[ft.dropdown.Option(key="Linear", content=ft.Text(value="Linear", color ="pink")),
                                                                     ft.dropdown.Option(key="Default", content=ft.Text(value="Default", color="pink")),
                                                                     ft.dropdown.Option(key="Dichotomic", content=ft.Text(value="Dichotomic", color="pink"))], width=170)
        self.__text= ft.TextField(label ="Add your sentence here", color = "pink", width=450)
        self.__btn = ft.ElevatedButton(text="Spell check", color = "pink", on_click=self.__controller.handleSentence)

        self.txtOut = ft.ListView(expand=True)  #expand=True -> gli dico che posso scorrere le varie opzioni della listView con la rotellina

        row1 = ft.Row([self.__dd1, self.__text, self.__btn])
        row2= ft.Row([self.txtOut])

        self.page.add(row1, row2)
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

    def getRicerca(self):
        return self.__dd1.value

    def getLanguage(self):
        return self.__dd.value