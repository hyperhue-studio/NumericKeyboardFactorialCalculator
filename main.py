import tkinter as tk
from tkinter import messagebox

# Defines a function to calculate the factorial of a number
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Defines a function to count the zeros in a number
def count_zeros(number):
    num_str = str(number)
    count = num_str.count('0')
    return count

# Defines the NumericKeyboard class, creating a graphical interface that limits input to numbers between 0 and 1558
class NumericKeyboard(tk.Tk):
    # Constructor of the class
    def __init__(self):
        super().__init__()
        self.title("Numeric Keyboard")
        self.geometry("300x200")

        self.number = tk.StringVar()

        self.entry = tk.Entry(self, state="readonly", textvariable=self.number, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', 'DEL', '=',
        ]

        for i, button in enumerate(buttons):
            row = i // 3 + 1
            col = i % 3
            tk.Button(self, text=button, width=5, height=2, command=lambda btn=button: self.add_number(btn)).grid(row=row, column=col)

    # Defines the add_number method, which adds a number to the text field
    def add_number(self, value):
        if value == '=':
            try:
                num = int(self.number.get())
                if num >= 0 and num <= 1558:
                    factorial = calculate_factorial(num)
                    zeros = count_zeros(factorial)
                    messagebox.showinfo("Result", f"The factorial of {num} is {factorial} and contains {zeros} zeros.")
                else:
                    messagebox.showerror("Error", "Enter a number between 0 and 1558.")
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number.")
        elif value == 'DEL':
            current_text = self.number.get()
            if current_text:
                self.number.set(current_text[:-1])
        else:
            self.number.set(self.number.get() + value)

# Runs the application
if __name__ == "__main__":
    app = NumericKeyboard()
    app.mainloop()
