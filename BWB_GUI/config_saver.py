# config_saver.py
def class_to_csv(bwb_configurations_list):
    import csv

    # Check if there is at least one configuration in the list to define the headers
    if not bwb_configurations_list:
        print("No configurations to save.")
        return

    # Use vars() on the first item to get the attribute names dynamically
    headers = list(vars(bwb_configurations_list[0]).keys())

    # Open or create the CSV file to save the configurations
    with open('bwb_configurations.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(headers)

        # Write each configuration's values
        for bwb in bwb_configurations_list:
            # Get the values of all attributes dynamically using vars()
            values = list(vars(bwb).values())
            writer.writerow(values)

