import tkinter as tk
from tkinter import messagebox

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

