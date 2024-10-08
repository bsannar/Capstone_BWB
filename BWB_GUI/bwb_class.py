# This Python file uses the following encoding: utf-8


class BWB:
    def __init__(self, dryWeight=None, fuelCap=None, sFuelConsum=None, liftDrag=None, resFraction=None, cruiseSpeed=None):
        self.dryWeight = dryWeight
        self.fuelCap = fuelCap #lbs
        self.sFuelConsum = sFuelConsum
        self.liftDrag = liftDrag
        self.resFraction = 0.1
        self.cruiseSpeed = cruiseSpeed
        self.numFighter = None
