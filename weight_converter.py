import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_weight():
    try:
        weight = float(weight_entry.get())
        if weight <= 0:
            raise ValueError("Invalid weight entered. Weight must be positive.")
        
        from_unit = from_unit_combo.get()
        to_unit = to_unit_combo.get()
        
        conversion_factors = {
            "Tonne": {"Tonne": 1, "Kilogram": 1000, "Gram": 1e+6, "Milligram": 1e+9, "Microgram": 1e+12, "Imperial ton": 0.984207, "US ton": 1.10231, "Pound": 2204.62, "Ounce": 35274},
            "Kilogram": {"Tonne": 0.001, "Kilogram": 1, "Gram": 1000, "Milligram": 1e+6, "Microgram": 1e+9, "Imperial ton": 0.000984207, "US ton": 0.00110231, "Pound": 2.20462, "Ounce": 35.274},
            "Gram": {"Tonne": 1e-6, "Kilogram": 0.001, "Gram": 1, "Milligram": 1000, "Microgram": 1e+6, "Imperial ton": 9.8421e-7, "US ton": 1.1023e-6, "Pound": 0.00220462, "Ounce": 0.035274},
            "Milligram": {"Tonne": 1e-9, "Kilogram": 1e-6, "Gram": 0.001, "Milligram": 1, "Microgram": 1000, "Imperial ton": 9.8421e-10, "US ton": 1.1023e-9, "Pound": 2.2046e-6, "Ounce": 3.5274e-5},
            "Microgram": {"Tonne": 1e-12, "Kilogram": 1e-9, "Gram": 1e-6, "Milligram": 0.001, "Microgram": 1, "Imperial ton": 9.8421e-13, "US ton": 1.1023e-12, "Pound": 2.2046e-9, "Ounce": 3.5274e-8},
            "Imperial ton": {"Tonne": 1.01605, "Kilogram": 1016.05, "Gram": 1.016e+6, "Milligram": 1.016e+9, "Microgram": 1.016e+12, "Imperial ton": 1, "US ton": 1.12, "Pound": 2240, "Ounce": 35840},
            "US ton": {"Tonne": 0.907185, "Kilogram": 907.185, "Gram": 907185, "Milligram": 9.072e+8, "Microgram": 9.072e+11, "Imperial ton": 0.892857, "US ton": 1, "Pound": 2000, "Ounce": 32000},
            "Pound": {"Tonne": 0.000453592, "Kilogram": 0.453592, "Gram": 453.592, "Milligram": 453592, "Microgram": 4.536e+8, "Imperial ton": 0.000446429, "US ton": 0.0005, "Pound": 1, "Ounce": 16},
            "Ounce": {"Tonne": 2.835e-5, "Kilogram": 0.0283495, "Gram": 28.3495, "Milligram": 28350, "Microgram": 2.835e+7, "Imperial ton": 2.7902e-5, "US ton": 3.125e-5, "Pound": 0.0625, "Ounce": 1}
        }
        
        result = weight * conversion_factors[from_unit][to_unit]
        result_label.config(text=f"{weight} {from_unit} = {result:.6f} {to_unit}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create main window
root = tk.Tk()
root.title("Weight Converter")

# Input for weight
tk.Label(root, text="Enter the Weight:").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for selecting units
units = ["Tonne", "Kilogram", "Gram", "Milligram", "Microgram", "Imperial ton", "US ton", "Pound", "Ounce"]

tk.Label(root, text="From:").grid(row=1, column=0, padx=10, pady=10)
from_unit_combo = ttk.Combobox(root, values=units)
from_unit_combo.grid(row=1, column=1, padx=10, pady=10)
from_unit_combo.current(0)

tk.Label(root, text="To:").grid(row=2, column=0, padx=10, pady=10)
to_unit_combo = ttk.Combobox(root, values=units)
to_unit_combo.grid(row=2, column=1, padx=10, pady=10)
to_unit_combo.current(1)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_weight)
convert_button.grid(row=3, columnspan=2, pady=20)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()
