import csv
from datetime import datetime

def convert_from_camel_casing(string):
    output = ""
    for s in string:
        if s.isupper():
            output += " " + s
        else:
            output += s
    return str.upper(output[0]) + output[1:]

def convert_to_camel_casing(string):
    return str.lower(string[0]) + string[1:].replace(" ", "")

class Bwb():
    def __init__(self, independentVars, dependentVars):
        self.independentVars = independentVars
        self.dependentVars = dependentVars

    def list_dependent_vars(self):
        names = vars(self.dependentVars).keys()
        return [convert_from_camel_casing(name) for name in names]

    def list_independent_vars(self):
        names = vars(self.independentVars).keys()
        return [convert_from_camel_casing(name) for name in names]

    def list_all_vars(self):
        names = {**vars(self.dependentVars), **vars(self.independentVars)}.keys()
        return [convert_from_camel_casing(name) for name in names]

class BwbJetIndependentVars:
    def __init__(self,
    wingSquareFootage,
    verticalTailSquareFootage,
    wingAspectRatio,
    verticalTailAspectRatio,
    wingTaperRatio,
    verticalTailTaperRatio,
    wingSweepAngle,
    verticalTailSweepAngle,
    fuelCapacity,
    thrustSpecificFuelConsumption,
    payloadTransportDistance,
    fractionOfRemainingFuelInF35sWhenRefueled=0.1):
        self.wingSquareFootage = wingSquareFootage
        self.verticalTailSquareFootage = verticalTailSquareFootage
        self.wingAspectRatio = wingAspectRatio
        self.verticalTailAspectRatio = verticalTailAspectRatio
        self.wingTaperRatio = wingTaperRatio
        self.verticalTailTaperRatio = verticalTailTaperRatio
        self.wingSweepAngle = wingSweepAngle
        self.verticalTailSweepAngle = verticalTailSweepAngle
        self.fuelCapacity = fuelCapacity
        self.thrustSpecificFuelConsumption = thrustSpecificFuelConsumption
        self.fractionOfRemainingFuelInF35sWhenRefueled = fractionOfRemainingFuelInF35sWhenRefueled
        self.payloadTransportDistance = payloadTransportDistance
        self.update_csv()

    def update_csv(self):
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a list of the current values
        values = ["BWB"]
        values.extend(vars(self))

        # Data to be written to the CSV
        row = [current_time] + values

        # Write to CSV file
        with open('DST_md.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

class BwbOpenVspIndependentVars:
    def __init__(self):
        self.vars = 0

class BwbDependentVars:
    def __init__(self):
        self.dryWeight = None
        self.liftOverDrag = None
        self.f35sRefueled = None
        self.maxRange = None
