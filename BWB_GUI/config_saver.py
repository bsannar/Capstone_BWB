import csv
import os

class MyClass:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def class_to_csv(obj, filename):
    # Get the attributes of the class as a dictionary
    class_attributes = vars(obj)
    
    # Check if the file already exists
    file_exists = os.path.isfile(filename)
    
    # Determine the next config number
    next_config = 1
    if file_exists:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:  # There are existing rows besides the header
                next_config = len(rows)

    # Append to the CSV file
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header (including "Config") if the file does not exist
        if not file_exists:
            writer.writerow(['Config'] + list(class_attributes.keys()))
        
        # Write the config number and the values of the dictionary
        writer.writerow([next_config] + list(class_attributes.values()))

# Example usage
my_obj1 = MyClass("Alice", 30, "New York")
class_to_csv(my_obj1, "output.csv")

my_obj2 = MyClass("Ben", 26, "Gridley")
class_to_csv(my_obj2, "output.csv")