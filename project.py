from dataclasses import dataclass
from datetime import datetime
from typing import List
import tkinter as tk
from tkinter import messagebox

# Define the Customer class
@dataclass
class Customer:
    name: str
    phone: str
    cc_number: str
    cc_exp_month: int
    cc_exp_year: int
    cc_valid: bool = False

# Function to extract digits from the credit card number
def digits_of(number: str) -> List[int]:
    return [int(d) for d in number if d.isdigit()]

# Function to validate the credit card
def validate_card(customer: Customer) -> bool:
    digits = digits_of(customer.cc_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    checksum += sum(sum(digits_of(str(digit * 2))) for digit in even_digits)
    valid_date = datetime(customer.cc_exp_year, customer.cc_exp_month, 1) > datetime.now()
    customer.cc_valid = checksum % 10 == 0 and valid_date
    return customer.cc_valid

# Main application class for the GUI
class CardValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Credit Card Validator")

        # Create UI elements
        self.name_label = tk.Label(root, text="Name")
        self.name_entry = tk.Entry(root)
        self.phone_label = tk.Label(root, text="Phone")
        self.phone_entry = tk.Entry(root)
        self.cc_number_label = tk.Label(root, text="CC Number")
        self.cc_number_entry = tk.Entry(root)
        self.cc_exp_month_label = tk.Label(root, text="Expiration Month (MM)")
        self.cc_exp_month_entry = tk.Entry(root)
        self.cc_exp_year_label = tk.Label(root, text="Expiration Year (YYYY)")
        self.cc_exp_year_entry = tk.Entry(root)
        self.validate_button = tk.Button(root, text="Validate", command=self.validate_card)

        # Layout UI elements
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.cc_number_label.grid(row=2, column=0, padx=10, pady=5)
        self.cc_number_entry.grid(row=2, column=1, padx=10, pady=5)
        self.cc_exp_month_label.grid(row=3, column=0, padx=10, pady=5)
        self.cc_exp_month_entry.grid(row=3, column=1, padx=10, pady=5)
        self.cc_exp_year_label.grid(row=4, column=0, padx=10, pady=5)
        self.cc_exp_year_entry.grid(row=4, column=1, padx=10, pady=5)
        self.validate_button.grid(row=5, columnspan=2, pady=10)

    def validate_card(self):
        # Collect input data
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        cc_number = self.cc_number_entry.get()
        cc_exp_month = int(self.cc_exp_month_entry.get())
        cc_exp_year = int(self.cc_exp_year_entry.get())

        # Create Customer object
        customer = Customer(name, phone, cc_number, cc_exp_month, cc_exp_year)

        # Validate card
        if validate_card(customer):
            messagebox.showinfo("Result", "Credit card is valid.")
        else:
            messagebox.showerror("Result", "Credit card is invalid.")

# Entry point of the program
if __name__ == "__main__":
    root = tk.Tk()
    app = CardValidatorApp(root)
    root.mainloop()
