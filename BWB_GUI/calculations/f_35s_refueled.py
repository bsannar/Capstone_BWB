import numpy as np

# Hypothetical BWB Parameters
empty_weight_BWB = 300000                                   # BWB empty weight 
fuel_capacity_BWB = 245000
initial_weight_BWB = empty_weight_BWB + fuel_capacity_BWB   # Fully fueled BWB weight 
SFC_BWB = 0.5                                               # Specific fuel consumption in 1/hour??
L_over_D_BWB = 22                                           # Lift-to-drag ratio
cruise_speed_BWB = 530                                      # BWB cruise speed in knots (NM/hour)??
reserve_fraction = 0.1                                      # Fraction of total fuel reserved for safety (10%)

# Mission parameters
range_nm = 4000             # Mission radius in nautical miles (one way)
f35_max_fuel = 18000        # Maximum fuel capacity of F-35 in pounds
f35_refuel_threshold = .2   # percentage of fuel left in F-35 tank when refueling begins

# Function to calculate the fuel consumed for a given range using the range equation
def fuel_required_for_range(range_nm, SFC, V, L_over_D, W_i):

    # Calculate the final weight after burning fuel for the given range
    W_f = W_i * np.exp(-(range_nm * SFC) / (V * L_over_D))

    # Return the fuel consumed (initial weight - final weight)
    fuel_consumed = W_i - W_f

    return fuel_consumed

# Function to calculate the tanker's fuel requirement for a round trip
def tanker_fuel_for_round_trip(range_nm, SFC, V, L_over_D, initial_weight, empty_weight):
    W_i = initial_weight

    # Calculate fuel for outbound leg (4000 NM)
    fuel_outbound = fuel_required_for_range(range_nm, SFC, V, L_over_D, W_i)

    # Calculate fuel for return leg
    fuel_return = fuel_required_for_range(range_nm, SFC, V, L_over_D, W_i - fuel_outbound)
    
    # Total fuel needed for the round trip (outbound + return)
    total_fuel_round_trip = fuel_outbound + fuel_return

    return total_fuel_round_trip

# Calculate the available fuel for refueling after round trip
fuel_capacity_BWB = initial_weight_BWB - empty_weight_BWB
fuel_for_round_trip = tanker_fuel_for_round_trip(4000, SFC_BWB, cruise_speed_BWB, L_over_D_BWB, initial_weight_BWB, empty_weight_BWB)

# Reserve some fuel as a factor of safety
usable_fuel_for_refueling = fuel_capacity_BWB - fuel_for_round_trip - (reserve_fraction * fuel_capacity_BWB)

# Fuel required per F-35 for the mission (based on how empty each f-35 is)
fuel_required_per_f35 = f35_max_fuel * (1 - f35_refuel_threshold)

# Calculate how many F-35s can be refueled
num_f35s_refueled = usable_fuel_for_refueling // fuel_required_per_f35

# #Calculate how much fuel was used by the BWB in the refueling process (I haven't done this part yet...we might need to iterate)
# fuel_burned_during_single_refuel = 
# fuel_burned_during_refueling = num_f35s_refueled * fuel_burned_during_single_refuel

# Output results
print(f"\nFuel required for round trip: {fuel_for_round_trip:.2f} pounds")
print(f"\nFuel available for refueling after round trip and safety reserves: {usable_fuel_for_refueling:.2f} pounds")
print(f"\nFuel required per F-35: {fuel_required_per_f35:.2f} pounds")
print(f"\nNumber of F-35s that can be refueled: {int(num_f35s_refueled)} \n")