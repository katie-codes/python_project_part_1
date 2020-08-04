import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    #Attempt 1
    # if temp_cel = float(temp_in_farenheit - 32) * 5/9)
    # return temp_cel

    return round(float(temp_in_farenheit - 32) * 5 / 9,1)



def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    return (total) / (num_items)









def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass



if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))




#open the file
with open("data/forecast_5days_a.json") as json_file:
    json_data = json.load(json_file)


# Variables for loop
min_temp_a = 0
date_day = 0


#print unformatted data
# print(json_data)




#for loop
for item in json_data["DailyForecasts"]:

#for date   
    date_day = (item["Date"])






#for loop
for item in json_data["DailyForecasts"]:

#for date   
    date_day = (item["Date"])
    print(f"--------{convert_date(date_day)}--------")

#for temperature 
    min_temp_d = (item["Temperature"]["Minimum"]["Value"])
    max_temp_d = (item["Temperature"]["Maximum"]["Value"])

# convert temperature to C
    c_min_temp_d = format_temperature(convert_f_to_c(min_temp_d))
    c_max_temp_d = format_temperature(convert_f_to_c(max_temp_d))   
    print( f"Minimum: {c_min_temp_d}, Maximum: {c_max_temp_d}")

# for day 
    long_chance_d = (item["Day"]["LongPhrase"])
    long_chance_n = (item["Night"]["LongPhrase"])

    rain_chance_d = (item["Day"]["PrecipitationProbability"])
    rain_chance_n = (item["Night"]["PrecipitationProbability"])

#### Print statement
    print(f"Daytime: {long_chance_d}")
    print(f"Chance of rain: {rain_chance_n}")

    print(f"Nighttime: {long_chance_n}")
    print(f"Chance of rain: {rain_chance_n}")

# calculate the lowest, highest 
min_temp_w = 0
max_temp_w = 0

#for loops min temp and day 8 day forecast
for item in json_data["DailyForecasts"]:
    min_temp_d = (item["Temperature"]["Minimum"]["Value"])
    if min_temp_w == 0:
        min_temp_w = min_temp_d
        min_date_w = item["Date"]
    else:
        if min_temp_d < min_temp_w:
            min_temp_w = min_temp_d
            min_date_w = item["Date"]


# convert temperature to C
c_min_temp_w = format_temperature(convert_f_to_c(min_temp_w))

#### Print statement
print()
print (f"The lowest temperature will be {c_min_temp_w}, and will occur on {convert_date(min_date_w)}")
    



#for loops max temp and day 8 day forecast
for item in json_data["DailyForecasts"]:
    max_temp_d = (item["Temperature"]["Maximum"]["Value"])
    if max_temp_w == 0:
        max_temp_w = max_temp_d
        max_date_w = item["Date"]
    else:
        if max_temp_d > max_temp_w:
            max_temp_w = max_temp_d
            max_date_w = item["Date"]

# convert temperature to C
c_max_temp_w = format_temperature(convert_f_to_c(max_temp_w)) 


#### Print statement




print()

# calculate the mean
# low 11.7
# high 20.1

#for loop
for item in json_data["DailyForecasts"]:

#for date   
    date_day = (item["Date"])

#for temperature 
    min_temp_d = (item["Temperature"]["Minimum"]["Value"])
    max_temp_d = (item["Temperature"]["Maximum"]["Value"])


    min_temp_a += min_temp_d
date_day = 0
date_day += 1



# convert temperature to C
# min_temp_a = format_temperature(convert_f_to_c(min_temp_a)) 

print(f"The average low this week is {format_temperature(convert_f_to_c(calculate_mean(min_temp_a, date_day)))}.")

min_temp_a = format_temperature(convert_f_to_c(min_temp_a)) 









############## working file

# # List to hold numbers entered by user
# numbers = []


# # While loop to add all items into a total
# count = 0
# while count < 4:
#     number = int(input("Please enter a number "))
#     numbers.append(number)
#     count += 1

# #get the total sum
# total_sum = sum(numbers)
# print(total_sum)

# #get number of items in list
# num_items = len(numbers)
# print(num_items)

# print (total_sum / num_items)


# # Function to calculate the mean - did not figure this out
# def calculate_mean(total_sum, num_items):
#     mean = (total_sum) / (num_items)
#     print(mean)
#     return (f"the mean of the numbers is {mean})")







































## an approach
# for dates in DailyForecasts:
# #print item off a list
#     print (DailyForecasts["Date"])

# for date in DailyForecasts(len(dates)):
#         line1 = f"-------- {dates[date]} --------"
#         output.append(line1)
#         line2 = f"Minimum Temperature: {format_temperature(min_temp[date])}"
#         output.append(line2)
#         line3 = f"Maximum Temperature: {format_temperature(max_temp[date])}"
#         output.append(line3)
#         line4 = f"Daytime: {long_chance_d[date]}"
#         output.append(line4)
#         line5 = f"    Chance of rain:  {rain_chance_d[date]}%"
#         output.append(line5)
#         line6 = f"Nighttime: {long_chance_n[date]}"
#         output.append(line6)
#         line7 = f"    Chance of rain:  {rain_chance_n[date]}%"
#         output.append(line7)

#         final_output = "\n".join(output)
#         print(final_output)










# #output the file
# with open("quiz_output.json", "w") as json_file:
#     for option in options:
#         json_file.write(option)





