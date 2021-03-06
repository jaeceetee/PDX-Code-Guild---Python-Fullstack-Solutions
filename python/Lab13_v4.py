# Lab 13 - Unit Converter - Allow user to enter unit - Support for yard and inches - User dictates unit output

# Ask user for numeric distance
num_distance = input("What is the distance? ")
num_distance = int(num_distance)

# Ask user for unit
acceptable_units = {
    "ft": .3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": .9144,
    "in": .0254
}
user_unit = input("What are the input units? (ft, mi, m, km, yd, in) ")
while user_unit not in acceptable_units:
    user_unit = input("What are the input units? (ft, mi, m, km, yd, in) ")

# Ask for user unit output
user_output_unit = input("What are the output units? (ft, mi, m, km, yd, in) ")
while user_output_unit not in acceptable_units:
    user_output_unit = input("What are the output units? (ft, mi, m, km, yd, in) ")

# Convert to meters
num_meter = num_distance * acceptable_units[user_unit]

# Convert to user output
result = num_meter / acceptable_units[user_output_unit]

# Print result
print(f"{num_distance} {user_unit} is {result} {user_output_unit}")

