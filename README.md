# pharma-finder
What is the Pharmacy Locator?

The Pharmacy Locator is a handy tool designed to help you quickly find the location of drugs within a pharmacy. No more wandering around trying to find what you need – simply input the drug name, dose, and type, and let the app do the rest!
How to Use

 Run the App: Start the Pharmacy Locator by running the provided Python script (pharmacy_locator.py).

Input Drug Information: Enter the name of the drug you're looking for in the designated field. You can also select the dose and type of the drug from the dropdown menus.

Click Search: Hit the "Search" button to find the drug within the pharmacy.

View Results: If the drug is found, you'll see its location within the pharmacy, along with the specified dose and type. If there's a typo in the drug name or a similar drug exists, the app suggests the closest matching drug name along with a similarity score.

Requirements

To use the Pharmacy Locator, you'll need:

 Python 3.x installed on your computer.
 The fuzzywuzzy library, which you can install by running pip install fuzzywuzzy.

Getting Started

Install Dependencies: Make sure you have Python 3.x installed, and install the fuzzywuzzy library using pip.

Download Files: Download the provided Python script (pharmacy_locator.py) and the drug data file (drug_locations.json) into the same directory.

Run the App: Start the app by running the Python script. The main window of the Pharmacy Locator will appear, ready for you to start searching!

Notes

Make sure your drug data file (drug_locations.json) is properly formatted. Each drug entry should include information such as name, location, dose, and type. The app uses fuzzy string matching to suggest similar drug names when a typo or a similar name is entered.
