from tixi3 import tixi3wrapper
from tixi3.tixi3wrapper import Tixi3Exception

print("loading dictionary")
data_dict:dict = {'Alt': {'Loiter': 10000.0, 'Service1': 20000.0, 'Service3': 20000.0, 'Climb1': 35000.0, 'Cruise2': 35000.0, 'Patrol1': 20000.0, 'Accel': 500.0, 'Landing': 0.0, 'Service2': 20000.0, 'Cruise1': 35000.0, 'TO': 0.0, 'Climb2': 35000.0, 'Patrol3': 20000.0, 'Patrol2': 20000.0}, 'Payload': {'TO': None, 'Climb1': 0.0, 'Landing': 200000.0, 'Service1': 66666.66666666667, 'Service3': 66666.66666666667, 'Service2': 66666.66666666667, 'Patrol1': 0.0, 'Climb2': 0.0, 'Loiter': 0.0, 'Cruise2': 0.0, 'Cruise1': 0.0, 'Patrol2': 0.0, 'Accel': 0.0, 'Patrol3': 0.0}, 'Time': {'Climb2': 3.495389101740758, 'Patrol1': 30.0, 'Cruise2': 148.77635757646775, 'Accel': 0.9985329948445103, 'Landing': 501.42238211708377, 'Service2': 30.0, 'Patrol2': 30.0, 'Service1': 30.0, 'Loiter': 20.0, 'Patrol3': 30.0, 'Climb1': 5.592937952809215, 'Service3': 30.0, 'Cruise1': 141.95003487876042, 'TO': 0.609129612461129}, 'Dist': {'Service3': 0.0, 'Cruise2': 1000.0, 'Climb2': 0.0, 'Patrol3': 0.0, 'Service1': 0.0, 'Cruise1': 954.1168851764721, 'Climb1': 40.32357644366336, 'TO': 5858.116088533008, 'Patrol1': 0.0, 'Service2': 0.0, 'Loiter': 0.0, 'Patrol2': 0.0, 'Accel': 5.559538379864544, 'Landing': 'Totals'}, 'Mach': {'Loiter': 0.4, 'Patrol3': 0.5, 'Cruise2': 0.7, 'Service2': 0.5, 'Climb2': 0.7, 'Climb1': 0.7, 'Patrol2': 0.5, 'Accel': 0.7, 'Cruise1': 0.7, 'TO': 0.2857963234948967, 'Patrol1': 0.5, 'Service1': 0.5, 'Landing': 'Distance', 'Service3': 0.5}, 'ExpPayload': 200000.0, 'PermPayload': 0.015625}
print("dictionary loaded")
print(data_dict)

def pull_data(dictionary, cpacs):
    # Define handles and open the tixi document
    tixi_handle = tixi3wrapper.Tixi3()
    tixi_handle.open(cpacs)

    # Count the number of segment elements
    segment_count = tixi_handle.getNamedChildrenCount("/cpacs/vehicles/performanceCases/missionDefinitions/segments", "segment")
    print(segment_count)
    
    print("begin dictionary print")
    # Iterate through each segment and print its name
    for i in range(1, segment_count + 1):  # Tixi uses 1-based indexing
        segment_name = tixi_handle.getTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/name")
        segment_type = tixi_handle.getTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/segmentType")
        segment_fuel = tixi_handle.getTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/fuelMass")
        segment_payload_expended = tixi_handle.getTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/payloadExpended")
        segment_distance = tixi_handle.getTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/distance")
        segment_altitude = tixi_handle.getTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/altitude")
        segment_mach = tixi_handle.getTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/mach")
        
        for key, sub_dict in dictionary.items():
            if isinstance(sub_dict, dict):  # Ensure it's a dictionary before iterating
                for sub_key, value in sub_dict.items():
                    if key == "Alt" and sub_key == segment_type:
                        sub_dict[sub_key] = segment_altitude
                    if key == "Payload" and sub_key == segment_type:
                        sub_dict[sub_key] = segment_payload_expended
                    # if key == "Time" and sub_key == segment_type:
                    #     sub_dict[sub_key] = segment_altitude
                    if key == "Dist" and sub_key == segment_type:
                        sub_dict[sub_key] = segment_distance
                    if key == "Mach" and sub_key == segment_type:
                        sub_dict[sub_key] = segment_mach
                    if key == "Dist" and sub_key == segment_type:
                        sub_dict[sub_key] = segment_distance
            if key == "ExpPayload":
                data_dict["ExpPayload"] += segment_payload_expended

            # else:
            #     # print(f"{key}: {sub_dict}")  
    print(dictionary)
    return(dictionary)


def push_data(dictionary, cpacs):
    # Define handles and open the tixi document
    tixi_handle = tixi3wrapper.Tixi3()
    tixi_handle.open(cpacs)

    # Count the number of subkeys
    num_subkeys = len(data_dict["Alt"])

    print(num_subkeys)
    
    print("begin dictionary print")
    # Iterate through each segment and print its name
        
    for key, sub_dict in dictionary.items():
        if isinstance(sub_dict, dict):  # Ensure it's a dictionary before iterating
            for sub_key, value in sub_dict.items():
                for i in range(1, num_subkeys + 1):  # Tixi uses 1-based indexing      
                    if key == "Name":
                        tixi_handle.updateTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/name", sub_dict[sub_key])
                    if key == "Type":
                        tixi_handle.updateTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/segmentType", sub_dict[sub_key])
                    if key == "Fuel":
                        tixi_handle.updateTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/fuelMass", sub_dict[sub_key])
                    if key == "Payload":
                        tixi_handle.updateTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/payloadExpended", sub_dict[sub_key])
                    if key == "Dist":
                        tixi_handle.updateTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/distance", sub_dict[sub_key])
                    if key == "Alt":
                        tixi_handle.updateTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/altitude", sub_dict[sub_key])
                    if key == "Mach":
                        tixi_handle.updateTextElement(f"/cpacs/vehicles/performanceCases/missionDefinitions/segments/segment[{i}]/mach", sub_dict[sub_key])


            # else:
            #     # print(f"{key}: {sub_dict}")  
    print(dictionary)
    return(dictionary)


pull_data(data_dict, "theAircraft.xml")