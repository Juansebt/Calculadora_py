import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text=None, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand

class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        CalcButton.__init__(self, text, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text=None, expand=1):
        CalcButton.__init__(self, text, expand)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

def main(page: ft.Page):
    page.title = "Calculadora_py"
    
    page.window.width = 370
    page.window.height = 337
    # page.bgcolor = "#1D2B53"
    
    result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

    page.add(
        ft.Container(
            width=350,
            bgcolor="#1D2B53",
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="Delete", expand=2),
                            ExtraActionButton(text="%"),
                            ActionButton(text="/"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="7"),
                            DigitButton(text="8"),
                            DigitButton(text="9"),
                            ActionButton(text="*"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="4"),
                            DigitButton(text="5"),
                            DigitButton(text="6"),
                            ActionButton(text="-"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="1"),
                            DigitButton(text="2"),
                            DigitButton(text="3"),
                            ActionButton(text="+"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="C"),
                            DigitButton(text="0"),
                            DigitButton(text="."),
                            ActionButton(text="="),
                        ]
                    ),
                ]
            )
        ),
    )

ft.app(target=main)
