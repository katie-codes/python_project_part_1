# from datetime import datetime



import json

#open the file
with open("data/forecast_5days_a.json") as json_file:
    json_data = json.load(json_file)

#print unformatted data
# print(json_data)



## NEW BLOCK 5 day overview header
## for temp, min & max, and day occuring

## for avg, low & high over the week





## NEW BLOCK date line header
#for loop
for item in json_data["DailyForecasts"]:

#for temperature 
min_temp = (item["Temperature"]["Minimum"]["Value"])
max_temp = (item["Temperature"]["Maximum"]["Value"])
print( f"Minimum: {min_temp}, Maximum: {max_temp}")
    
######## Mentors - how to use {temp}{DEGREE_SYBMOL}
# min_temp = [convert_f_to_c(item) for item in min_temp]




# for day 
long_chance_d = (item["Day"]["LongPhrase"])
long_chance_n = (item["Night"]["LongPhrase"])

rain_chance_d = (item["Day"]["PrecipitationProbability"])
rain_chance_n = (item["Night"]["PrecipitationProbability"])

print(f"Daytime: {long_chance_d}")
print(f"Chance of rain: {rain_chance_n}")

print(f"Nighttime: {long_chance_n}")
print(f"Chance of rain: {rain_chance_n}")


## Split into days 

#create list to store data in
DailyForecasts = []

# Add data to list
DailyForecasts.append(json_data)
print(DailyForecasts)

#index items in data
item = "Date"
index = DailyForecasts.index(item)





## an approach
for dates in DailyForecasts:
    print (len(dates))

for date in DailyForecasts(len(dates)):
        line = f"-------- {dates[date]} --------"
        output.append(line)
        line2 = f"Minimum Temperature: {format_temperature(min_temp[date])}"
        output.append(line2)
        line3 = f"Maximum Temperature: {format_temperature(max_temp[date])}"
        output.append(line3)
        line4 = f"Daytime: {long_chance_d[date]}"
        output.append(line4)
        line5 = f"    Chance of rain:  {rain_chance_d[date]}%"
        output.append(line5)
        line6 = f"Nighttime: {long_chance_n[date]}"
        output.append(line6)
        line7 = f"    Chance of rain:  {rain_chance_n[date]}%"
        output.append(line7)

        final_output = "\n".join(output)
        print(final_output)










# #output the file
# with open("quiz_output.json", "w") as json_file:
#     for option in options:
#         json_file.write(option)

















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
    pass


############## working file
# temp_fah = input("What is your temp in fahrenheit? ")

# def convert_temp(temp_fah):
#     temp_cel = ((float(temp_fah) - 32) * 5/9)
#     return f"{temp_fah} = {temp_cel}"

# print(convert_temp(temp_fah))








def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    pass

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





