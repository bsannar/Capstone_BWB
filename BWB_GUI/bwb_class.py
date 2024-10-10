class BWB:
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
        self.fuelCap = fuelCap #lbs
        self.sFuelConsum = sFuelConsum
        self.liftDrag = liftDrag
        self.resFraction = resFraction
        self.machNumber = machNumber
        self.numFighter = None
        self.maxRange = None
