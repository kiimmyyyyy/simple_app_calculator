import tkinter as tk
from tkinter import messagebox
from unittest import result


def kims_calculator():
    try:
        num1 = float(num1.get())
        num2 = float(num2.get())
        operation = operation_var.get()


        if operation == "Addition":
            result = num1 + num2
        elif operation =="Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation =="Division":
            result = num1 / num2
            if num2 == 0:
                raise ZeroDivisionError ("Undefined")
        else:
            messagebox.showerror(title="Input Error", message=" Math Operation is not recognized")
            return

        label_result.config(text=f"Result: {result}", fg="pink")

    except ValueError:
        messagebox.showerror(title="Input Error", message=" PLEASE enter valid numbers.")
    except ZeroDivisionError as error:
        messagebox.showerror("Math Error", str(error))

def reset_program()
    prog_num1.delete(0, tk.END)
    prog_num2.delete(0, tk.END)
    label_result.config(text=f"Result: {result}", fg="green")

def exit_program():
    messagebox.showinfo("Exit Program", f"Program Exited. Come back next time!")
    root.destroy()

root = tk.Tk()
root.title("Kim's Simple App Calculator")
root.geometry("400x400")

tk.Label(root, text= "Enter First Number: ").pack(pady=5)
prog_num1 = tk.Entry(root)
prog_num1.pack()

tk.Label(root, text= "Enter Second Number: ").pack(pady=5)
prog_num2 = tk.Entry(root)
prog_num2.pack()

