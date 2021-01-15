# LAb 19 - Rain Data

import requests
import re
import math
from datetime import datetime

# Saught Variables
total_rain =0
mean = 0
variance = 0
stand_div = 0
variance_numerator = 0
date_format = '%d-%b-%Y'

# Get Data
url = 'https://or.water.usgs.gov/non-usgs/bes/arleta.rain'
response = requests.get(url)
data = response.text

all_dates = re.findall(r'\d{2}-[A-Z]+-\d{4}', data)
rain_amt = re.findall(r'\d{4}\s+(\d*-?)\s+', data)

# Combine to Dictionary
formatted_data = []
for idx in range(len(all_dates)):
    # Turn rain data to int
    if rain_amt[idx] == '-':
        pass                # If there is no data, skip
    else:
        rain_amt[idx] = int(rain_amt[idx])
        # Get total rain for calculations

        cur_data = {
            'date': datetime.strptime(all_dates[idx], date_format),
            'rainfall': rain_amt[idx],
        }
        formatted_data.append(cur_data)
        total_rain += rain_amt[idx]
        variance_numerator += (rain_amt[idx] - mean) ** 2

# Calculate Mean
mean = total_rain / (len(formatted_data))

# Calculate the variance
variance = variance_numerator / (len(formatted_data))

# Standard Deviation
standard_div = math.sqrt(variance)

# Most rain date
high = 0
high_date = ''
for item in formatted_data:
    if item['rainfall']> high:
        high = item['rainfall']
        high_date = item['date']

# Display for user
print(f"""Most rainfall happened on {high_date.strftime(date_format)} with {high} inches.
From {formatted_data[-1]['date'].strftime(date_format)} to {formatted_data[0]['date'].strftime(date_format)}
Variance = {variance}
Standard Diviation = {standard_div}
""")