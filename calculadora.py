import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text=None, expand=1, on_click=None):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = on_click

class DigitButton(CalcButton):
    def __init__(self, text, expand=1, on_click=None):
        CalcButton.__init__(self, text, expand, on_click)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text, on_click=None):
        CalcButton.__init__(self, text, on_click=on_click)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text=None, expand=1, on_click=None):
        CalcButton.__init__(self, text, expand, on_click=on_click)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

def main(page: ft.Page):
    page.title = "Calculadora_py"
    
    page.window.width = 370
    page.window.height = 367
    
    current_value = "0"  # Almacena el valor que se está mostrando
    operation = None  # Almacena la operación actual
    operand1 = None  # Almacena el primer número ingresado
    operation_text = ""  # Almacena la operación mostrada

    def update_display(value):
        nonlocal current_value
        result.value = value
        current_value = value
        page.update()

    def update_operation_display(op_text):
        operation_display.value = op_text
        page.update()

    def on_digit_click(e):
        nonlocal current_value, operation_text
        if current_value == "0" or current_value == "Error":
            current_value = e.control.text
        else:
            current_value += e.control.text
        operation_text += e.control.text
        update_display(current_value)
        update_operation_display(operation_text)

    def on_action_click(e):
        nonlocal current_value, operand1, operation, operation_text
        if e.control.text in ["+", "-", "*", "/"]:
            if operand1 is None and current_value != "0":
                operand1 = float(current_value)
            elif operand1 is not None and current_value != "0":
                operand1 = evaluate()
            operation = e.control.text
            current_value = "0"
            operation_text += f" {operation} "
        elif e.control.text == "=":
            if operand1 is None or current_value == "0":
                update_display("Error")
                operation_text = ""
                operand1 = None
                operation = None
            else:
                result_value = evaluate()
                update_display(format_result(result_value))
                operation_text = ""  # Resetea la operación después del cálculo
                operand1 = None
                operation = None
        update_operation_display(operation_text)
        page.update()

    def evaluate():
        nonlocal operand1, current_value, operation
        try:
            operand2 = float(current_value)
            if operation == "+":
                return operand1 + operand2
            elif operation == "-":
                return operand1 - operand2
            elif operation == "*":
                return operand1 * operand2
            elif operation == "/":
                if operand2 != 0:
                    return operand1 / operand2
                else:
                    return "Error: Division by 0"
        except ValueError:
            return "Error: Invalid Input"

    def format_result(result):
        # Si el resultado es un número entero, lo mostramos como entero
        if isinstance(result, (int, float)):
            if result.is_integer():
                return str(int(result))  # Convierte a entero si no tiene decimales
            else:
                return str(result)  # De lo contrario, lo mostramos con decimales
        return result

    def on_clear_click(e):
        nonlocal current_value, operand1, operation, operation_text
        current_value = "0"
        operand1 = None
        operation = None
        operation_text = ""
        update_display(current_value)
        update_operation_display(operation_text)

    def on_delete_click(e):
        nonlocal current_value, operation_text
        if len(current_value) > 1:
            current_value = current_value[:-1]
        else:
            current_value = "0"
        if len(operation_text) > 1:
            operation_text = operation_text[:-1]
        else:
            operation_text = ""
        update_display(current_value)
        update_operation_display(operation_text)

    # Pantalla donde se mostrará la operación
    operation_display = ft.Text(value="", color=ft.colors.WHITE38, size=15)
    result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

    page.add(
        ft.Container(
            width=350,
            bgcolor="#1D2B53",
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[operation_display], alignment="end"),  # Mostrar operación
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="Delete", expand=2, on_click=on_delete_click),
                            ExtraActionButton(text="%", on_click=None),  # Este se puede implementar
                            ActionButton(text="/", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="7", on_click=on_digit_click),
                            DigitButton(text="8", on_click=on_digit_click),
                            DigitButton(text="9", on_click=on_digit_click),
                            ActionButton(text="*", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="4", on_click=on_digit_click),
                            DigitButton(text="5", on_click=on_digit_click),
                            DigitButton(text="6", on_click=on_digit_click),
                            ActionButton(text="-", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="1", on_click=on_digit_click),
                            DigitButton(text="2", on_click=on_digit_click),
                            DigitButton(text="3", on_click=on_digit_click),
                            ActionButton(text="+", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="C", on_click=on_clear_click),
                            DigitButton(text="0", on_click=on_digit_click),
                            DigitButton(text=".", on_click=on_digit_click),
                            ActionButton(text="=", on_click=on_action_click),
                        ]
                    ),
                ]
            )
        ),
    )

ft.app(target=main)
