import tkinter as tk
from tkinter import messagebox
import math

class CalculatorLogic:
    def add(self, num1, num2): return num1 + num2

    def subtract(self, num1, num2): return num1 - num2

    def multiply(self, num1, num2): return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Undefined")
        return num1 / num2

    def power(self, num1, num2): return num1 ** num2

    def square_root(self, num1, num2): return math.sqrt(num1 + num2)

class KimmyCalculatorApp(CalculatorLogic):
    def __init__(self, root):
        self.root = root
        self.root.title("Kim's Simple App Calculator")
        self.root.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter First Number: ").pack(pady=5)
        self.prog_num1 = tk.Entry(self.root)
        self.prog_num1.pack()

        tk.Label(self.root, text="Enter Second Number: ").pack(pady=5)
        self.prog_num2 = tk.Entry(self.root)
        self.prog_num2.pack()

        tk.Label(self.root, text="Choose Operation: ", bg="yellow").pack(pady=5)
        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set("Select Operation")
        options = ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root"]
        self.dropdown = tk.OptionMenu(self.root, self.operation_var, *options)
        self.dropdown.pack()

        self.btn_calculate = tk.Button(self.root, text="Calculate", command=self.calculate, bg="light pink", fg="black",
                                       font=("Times New Roman", 12, "bold"))
        self.btn_calculate.pack(pady=10)
        self.label_result = tk.Label(self.root, text="Result: ", font=("Times New Roman", 15, "bold"))
        self.label_result.pack(pady=10)

        self.btn_reset = tk.Button(self.root, text="Try Again", command=self.reset_program, bg="white", fg="green",
                                   font=("Times New Roman", 12, "bold"))
        self.btn_reset.pack(pady=5)

        self.btn_exit = tk.Button(self.root, text="Exit", command=self.exit_program, bg="white", fg="red")
        self.btn_exit.pack(pady=5)

    def calculate(self):
        try:
            num1 = float(self.prog_num1.get())
            num2 = float(self.prog_num2.get())
            operation = self.operation_var.get()
            result = None

            if operation == "Addition":
                result = self.add(num1, num2)
            elif operation == "Subtraction":
                result = self.subtract(num1, num2)
            elif operation == "Multiplication":
                result = self.multiply(num1, num2)
            elif operation == "Division":
                result = self.divide(num1, num2)
            elif operation == "Power":
                result = self.power(num1, num2)
            elif operation == "Square Root":
                result = self.square_root(num1, num2)
            else:
                messagebox.showerror(title="Invalid Input", message="Input Value is not recognized.")
                return

            self.label_result.config(text=f"Result: {result}", fg="blue")

        except ValueError:
             messagebox.showerror(title="Input Error", message=" PLEASE enter valid numbers.")

        except ZeroDivisionError as error:
             messagebox.showerror("Math Error", str(error))


    def reset_program(self):
        self.prog_num1.delete(0, tk.END)
        self.prog_num2.delete(0, tk.END)
        self.label_result.config(text="Result: ", fg="green")


    def exit_program(self):
        messagebox.showinfo("Exit Program", f"Program Exited. Come back next time!")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = KimmyCalculatorApp(root)
    root.mainloop()
