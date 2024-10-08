import sys
import os

# Add the path to the folder containing the other script
script_dir = os.path.abspath("BWB_GUI\calculations")
sys.path.insert(0, script_dir)

import f_35s_refueled as Henry


Henry_data = Henry.fuel_required_for_range(400, .5, 500, 20, 300000)
print(f"Test: {Henry_data}")

data_storage = {}

def save_data(name, values):
    data_storage[name] = values

def get_user_input():
    # Prompt the user to enter the dataset name (To be replaced by a GUI text box)
    name = input("Enter the name of the dataset: ")
    
    # Prompt the user to enter values separated by commas (To be replaced by GUI and/or excell data)
    values_str = input("Enter the values for the dataset (comma-separated): ")
    values = [float(value.strip()) for value in values_str.split(',')]
    
    # Save the dataset
    save_data(name, values)
    
    print(f"Dataset '{name}' saved successfully.")

def main():
    while True:
        get_user_input()
        
        # Ask the user if they want to add more datasets
        another = input("Do you want to add another dataset? (yes/no): ").lower()
        if another != 'yes':
            break

    # Show the final content of data_storage
    print("\nAll datasets:")
    print(data_storage)

# Run the program
main()
