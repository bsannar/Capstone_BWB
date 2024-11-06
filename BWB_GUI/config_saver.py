# config_saver.py
def class_to_csv(bwb_configurations_list, file_name):
    import csv

    # Check if there is at least one configuration in the list to define the headers
    if not bwb_configurations_list:
        print("No configurations to save.")
        return

    # Get headers by combining attributes of independentVars and dependentVars
    sample_bwb = bwb_configurations_list[0]
    independent_headers = [f"independent_{key}" for key in vars(sample_bwb.independentVars)]
    dependent_headers = [f"dependent_{key}" for key in vars(sample_bwb.dependentVars)]
    headers = independent_headers + dependent_headers

    # Open or create the CSV file to save the configurations
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(headers)

        # Write each configuration's values
        for bwb in bwb_configurations_list:
            # Get values of independentVars and dependentVars
            independent_values = list(vars(bwb.independentVars).values())
            dependent_values = list(vars(bwb.dependentVars).values())
            values = independent_values + dependent_values
            writer.writerow(values)



# config_loader.py
def csv_to_class(file_name):
    import csv
    from bwb_class import Bwb, BwbJetIndependentVars, BwbDependentVars

    instances = []

    # Open the CSV file to read the configurations
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Read the header row to get attribute names
        headers = next(reader)

        # Identify attributes for independentVars and dependentVars based on headers
        independent_attrs = [header for header in headers if header.startswith("independent_")]
        dependent_attrs = [header for header in headers if header.startswith("dependent_")]

        # Read each row and create an instance of Bwb
        for row in reader:
            # Create instances of independentVars and dependentVars
            independent_instance = BwbJetIndependentVars.__new__(BwbJetIndependentVars)
            dependent_instance = BwbDependentVars.__new__(BwbDependentVars)

            # Set attributes for independentVars
            for attr, value in zip(independent_attrs, row):
                actual_attr = attr.replace("independent_", "")  # Remove prefix
                setattr(independent_instance, actual_attr, value)

            # Set attributes for dependentVars
            for attr, value in zip(dependent_attrs, row[len(independent_attrs):]):
                actual_attr = attr.replace("dependent_", "")  # Remove prefix
                setattr(dependent_instance, actual_attr, value)

            # Create the main Bwb instance and assign the nested instances
            instance = Bwb(independent_instance, dependent_instance)

            # Append the instance to the list
            instances.append(instance)

    return instances


