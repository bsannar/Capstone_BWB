def get_number_f_35s(bwb, mainSheet):       # compare_x40_to_018()
    f35_max_fuel = 18000                       # Maximum fuel capacity of F-35 in pounds
    f35_refuel_threshold = .2

    max_number_f35s = 80000  # Max number of F-35s to attempt refueling
    for i in range(1, max_number_f35s + 1):

        mainSheet["O17"].value = f35_max_fuel*(1-f35_refuel_threshold)*i

        # Count number of iterations to know how many f-35s can be refueled
        if mainSheet["X40"].value > mainSheet["O18"].value:
            bwb.dependentVars.f35sRefueled = i-1
            break
