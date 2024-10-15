#import numpy as np
#from bwb_class import BWB

#bwb = BWB(300000, 200000, .5, 20, .1, 530)

# # # Hypothetical BWB Parameters
# # empty_weight_BWB = 300000                                   # BWB empty weight
# # fuel_capacity_BWB = 200000
# # initial_weight_BWB = empty_weight_BWB + fuel_capacity_BWB   # Fully fueled BWB weight
# # SFC_BWB = 0.5                                               # Specific fuel consumption in 1/hour??
# # L_over_D_BWB = 20                                           # Lift-to-drag ratio
# # cruise_speed_BWB = 530                                      # BWB cruise speed in knots (NM/hour)??
# # reserve_fraction = 0.1                                      # Fraction of total fuel reserved for safety (10%)

# # # Mission parameters
# # range_nm = 4000             # Mission radius in nautical miles (one way)
# # f35_max_fuel = 18000        # Maximum fuel capacity of F-35 in pounds
# # f35_refuel_threshold = .2   # percentage of fuel left in F-35 tank when refueling begins
# # f35_refuel_rate = 360000    # this is a totally arbitrary number (just googled) in lbs of fuel per hour


# # Function to calculate the fuel consumed for a given range using the range equation
# def fuel_required_for_range(range_nm, SFC, V, L_over_D, W_i):

#     # Calculate the final weight after burning fuel for the given range
#     W_f = W_i * np.exp(-(range_nm * SFC) / (V * L_over_D))

#     # Return the fuel consumed (initial weight - final weight)
#     fuel_consumed = W_i - W_f

#     return fuel_consumed

# def fuel_used_during_refueling_calc(num_f35s, refuel_rate, lbs_of_fuel_per_f35, refuel_cruise_speed, SFC, L_over_D, Weight_when_refueling_begins):

#     #calculate time per f-35 refueled
#     time_per_f35 = lbs_of_fuel_per_f35 / refuel_rate

#     #calculate the time to refuel all f-35s
#     time_refueling = num_f35s * time_per_f35

#     #calculate the distance flown while refueling all f-35s
#     distance_flown_during_refueling = time_refueling * (refuel_cruise_speed) # converting to nautical miles

#     #calculate the weight difference (and therefore fuel used) in refueling
#     Weight_when_refueling_ends = Weight_when_refueling_begins * np.exp(-(distance_flown_during_refueling * SFC) / (refuel_cruise_speed * L_over_D))

#     #calculate total fuel used in refueling from the time in flight, and the fuel offloaded to the f-35s (not calculus lol)
#     total_fuel_used_in_refueling = Weight_when_refueling_begins - Weight_when_refueling_ends - num_f35s * lbs_of_fuel_per_f35

#     return total_fuel_used_in_refueling


# # Function to calculate the tanker's fuel requirement for a round trip
# def tanker_fuel_for_round_trip(range_nm, SFC, V, L_over_D, initial_weight, fuel_used_during_refueling):
#     W_i = initial_weight

#     # Calculate fuel for outbound leg (4000 NM)
#     fuel_outbound = fuel_required_for_range(range_nm, SFC, V, L_over_D, W_i)

#     # Calculate fuel for return leg and during refueling
#     fuel_return_and_refuel = fuel_required_for_range(range_nm, SFC, V, L_over_D, W_i - fuel_outbound - fuel_used_during_refueling)

#     # Total fuel needed for the round trip (outbound + return)
#     total_fuel_round_trip = fuel_outbound + fuel_return_and_refuel

#     return total_fuel_round_trip


# def get_number_f_35s(bwb):
#     initial_weight_BWB = bwb.dryWeight + bwb.fuelCap                  # Fully fueled BWB weight

#     range_nm = 4000                                                   # Mission radius in nautical miles (one way)
#     f35_max_fuel = 18000                                              # Maximum fuel capacity of F-35 in pounds
#     f35_refuel_threshold = .2                                         # percentage of fuel left in F-35 tank when refueling begins
#     f35_refuel_rate = 360000                                          # this is a totally arbitrary number (just googled) in lbs of fuel per hour
#     fuel_required_per_f35 = f35_max_fuel * (1 - f35_refuel_threshold) #Fuel required per F-35 for the mission (based on how empty each f-35 is)


#     # Simulate refueling to count number of f-35s
#     num_f35s_refueled = 0
#     max_f35s = 80000  # Max number of F-35s to attempt refueling
#     cruiseSpeed = bwb.machNumber * 666.739
#     for i in range(1, max_f35s + 1):
#         weight_after_leg_1 = initial_weight_BWB - fuel_required_for_range(range_nm, bwb.sFuelConsum, cruiseSpeed, bwb.liftDrag, initial_weight_BWB)

#         fuel_for_refueling_f_35s = fuel_used_during_refueling_calc(i, f35_refuel_rate, fuel_required_per_f35, cruiseSpeed, bwb.sFuelConsum, bwb.liftDrag, weight_after_leg_1)

#         # Calculate total fuel for the round trip (including refueling)
#         fuel_for_whole_trip = tanker_fuel_for_round_trip(range_nm, bwb.sFuelConsum, cruiseSpeed, bwb.liftDrag, initial_weight_BWB, fuel_for_refueling_f_35s)

#         # Reserve some fuel as a factor of safety, and calculate fuel left over
#         fuel_left_over = bwb.fuelCap - fuel_for_whole_trip - (bwb.resFraction * bwb.fuelCap)

#         # Count number of iterations to know how many f-35s can be refueled
#         if fuel_left_over >= 0:
#             num_f35s_refueled = i  # Update count of F-35s refueled
#         else:
#             number_refueled = i-1
#             leftover_fuel = fuel_left_over
#             break
#     bwb.numFighter = num_f35s_refueled

#get_number_f_35s(bwb)

def get_number_f_35s(bwb, mainSheet)       # compare_x40_to_018()
    f35_max_fuel = 18000                       # Maximum fuel capacity of F-35 in pounds
    f35_refuel_threshold = .2

    max_number_f35s = 80000  # Max number of F-35s to attempt refueling
    for i in range(1, max_number_f35s + 1):

        mainSheet["017"].value = f35_max_fuel*(1-f35_refuel_threshold)*i

        # Count number of iterations to know how many f-35s can be refueled
        if mainSheet["X40"] > mainSheet["O18"]:
            bwb.numFighter = i-1
            break







