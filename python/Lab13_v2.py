# Lab 13 - Unit Converter - Allow user to enter unit

# Ask user for numeric distance
num_distance = input("What is the distance? ")
num_distance = float(num_distance)

# Ask user for unit
acceptable_units = {
    "ft": .3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000
}
# user_unit = input("What are the units? (ft, mi, m, km) ")
user_unit = ""
while user_unit not in acceptable_units:
    user_unit = input("What are the units? (ft, mi, m, km) ")

# Convert to meters
num_meter = num_distance * acceptable_units[user_unit]

# Print result
print(f"{num_distance} {user_unit} is {num_meter} m")

