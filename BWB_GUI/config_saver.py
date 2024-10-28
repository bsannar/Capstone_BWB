# config_saver.py
def class_to_csv(bwb_configurations_list,file_name):
    import csv

    # Check if there is at least one configuration in the list to define the headers
    if not bwb_configurations_list:
        print("No configurations to save.")
        return

    # Use vars() on the first item to get the attribute names dynamically
    headers = list(vars(bwb_configurations_list[0]).keys())

    # Open or create the CSV file to save the configurations

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(headers)


        # Write each configuration's values
        for bwb in bwb_configurations_list:
            # Get the values of all attributes dynamically using vars()
            values = list(vars(bwb).values())
            writer.writerow(values)


# config_loader.py
def csv_to_class(file_name):
    import csv
    from bwb_class import BWB  # Import the bwb class

    instances = []

    # Open the CSV file to read the configurations
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Read the header row to get attribute names
        headers = next(reader)

        # Read each row and create an instance of BWB
        for row in reader:
            # Create an instance of the BWB class without calling __init__
            instance = BWB.__new__(BWB)

            # Set the attributes dynamically based on headers and values
            for attr, value in zip(headers, row):
                setattr(instance, attr, value)

            # Append the instance to the list
            instances.append(instance)

    return instances
