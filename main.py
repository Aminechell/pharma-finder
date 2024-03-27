import tkinter as tk
from tkinter import ttk
import json
from fuzzywuzzy import process

class Pharmacy:
    def __init__(self, layers, columns, drug_data):
        self.layers = layers
        self.columns = columns
        self.drug_data = drug_data

    def find_drug(self, drug_name, dose, drug_type):
        # Find closest match to the user input
        closest_match = process.extractOne(drug_name, self.drug_data.keys())
        matched_drug = closest_match[0]
        match_score = closest_match[1]

        if match_score >= 80:  # Minimum similarity score threshold
            drug_info = self.drug_data[matched_drug]
            if drug_info["dose"] == dose and drug_info["type"] == drug_type:
                location = drug_info["location"]
                return f"Drug: '{matched_drug}'\nLocation: Layer {location['layer']}, Column {location['column']}\nDose: {dose}\nType: {drug_type}"
            else:
                return f"The drug '{matched_drug}' with the specified dose '{dose}' and type '{drug_type}' is not available in the pharmacy."
        else:
            return matched_drug, match_score

def search():
    drug_name = entry_name.get()
    dose = dose_var.get()
    drug_type = type_var.get()

    result = pharmacy.find_drug(drug_name, dose, drug_type)
    if isinstance(result, tuple):
        suggested_drug, similarity_score = result
        result_label.config(text=f"The drug '{drug_name}' is not found in the pharmacy. Did you mean '{suggested_drug}'? Similarity score: {similarity_score}")
    else:
        result_label.config(text=result)

# Read drug data from JSON file
with open("drug_locations.json", "r") as file:
    drug_data = json.load(file)

# Create the main window
window = tk.Tk()
window.title("Pharmacy Locator")

# Create a Pharmacy instance
pharmacy = Pharmacy(layers=5, columns=4, drug_data=drug_data)  # Example: 5 layers, 4 columns

# Create GUI elements
label_name = tk.Label(window, text="Enter the name of the drug:")
label_name.grid(row=0, column=0, pady=5, padx=10, sticky="w")

entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, pady=5, padx=10)

label_dose = tk.Label(window, text="Select the dose:")
label_dose.grid(row=1, column=0, pady=5, padx=10, sticky="w")

doses = set()
for drug_info in drug_data.values():
    doses.add(drug_info["dose"])

dose_var = tk.StringVar()
dose_dropdown = ttk.Combobox(window, textvariable=dose_var, values=list(doses))
dose_dropdown.grid(row=1, column=1, pady=5, padx=10)

label_type = tk.Label(window, text="Select the type:")
label_type.grid(row=2, column=0, pady=5, padx=10, sticky="w")

types = set()
for drug_info in drug_data.values():
    types.add(drug_info["type"])

type_var = tk.StringVar()
type_dropdown = ttk.Combobox(window, textvariable=type_var, values=list(types))
type_dropdown.grid(row=2, column=1, pady=5, padx=10)

search_button = tk.Button(window, text="Search", command=search)
search_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="", wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

# Run the main event loop
window.mainloop()
