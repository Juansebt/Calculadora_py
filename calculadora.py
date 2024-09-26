import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500")

        self.equation = tk.StringVar()
        self.equation.set("")

        self.entry = tk.Entry(self.root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == "=":
                btn = tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=self.calculate)
            else:
                btn = tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.button_click(b))

            btn.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        clear_button = tk.Button(self.root, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear)
        clear_button.grid(row=row_val, column=col_val, columnspan=4, sticky="we")

    def button_click(self, button):
        current_equation = self.equation.get()
        new_equation = current_equation + str(button)
        self.equation.set(new_equation)

    def clear(self):
        self.equation.set("")

    def calculate(self):
        try:
            result = eval(self.equation.get())
            self.equation.set(result)
        except Exception as e:
            self.equation.set("error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()

# Mejorar la calculadora --- diseño y funcionalidad