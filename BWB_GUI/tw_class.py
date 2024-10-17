import csv
from datetime import datetime

class TW:
    def __init__(self,
                 sqFtWing,
                 sqFtVertTail,
                 aspectWing,
                 aspectVertTail,
                 taperRatioWing,
                 taperRatioVertTail,
                 sweepWing,
                 sweepVertTail,
                 dryWeight,
                 fuelCap,
                 sFuelConsum,
                 liftDrag,
                 machNumber,
                 resFraction=0.1):
        self.sqFtWing = sqFtWing
        self.sqFtVertTail = sqFtVertTail
        self.aspectWing = aspectWing
        self.aspectVertTail = aspectVertTail
        self.taperRatioWing = taperRatioWing
        self.taperRatioVertTail = taperRatioVertTail
        self.sweepWing = sweepWing
        self.sweepVertTail = sweepVertTail
        self.dryWeight = dryWeight
        self.fuelCap = fuelCap
        self.sFuelConsum = sFuelConsum
        self.liftDrag = liftDrag
        self.resFraction = resFraction
        self.machNumber = machNumber
        self.numFighter = None
        
        # Update CSV with the current instance's data
        self.update_csv()

    def update_csv(self):
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create a list of the current values
        values = ["T&W",self.sqFtWing, self.sqFtVertTail, self.aspectWing, self.aspectVertTail,
                  self.taperRatioWing, self.taperRatioVertTail, self.sweepWing, self.sweepVertTail,
                  self.dryWeight, self.fuelCap, self.sFuelConsum, self.liftDrag, self.resFraction,
                  self.machNumber]
              
        # Data to be written to the CSV
        row = [current_time] + values
        
        # Write to CSV file
        with open('DST_md.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
