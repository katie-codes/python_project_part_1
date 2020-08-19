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
    return round((temp_in_farenheit - 32) * 5/9, 1)




def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = float(total)/ num_items
    mean = round(mean,1)
    return mean




def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
#     pass
# if __name__ == "__main__":
#     print(process_weather("data/forecast_5days_a.json"))


    with open(forecast_file) as json_file:
        json_data = json.load(json_file)

    # #open the file
    # with open("data/forecast_5days_a.json") as json_file:
    #     # with open("data/forecast_5days_b.json") as json_file:
    #     #     with open("data/forecast_8days.json") as json_file:
    #             json_data = json.load(json_file)


    # variables for while loops
    min_temp_w = 0
    max_temp_w = 0
    min_temp_a = 0
    max_temp_a = 0
    number_days = 0

    # final output list
    flist_daily = []
    flist_summary = []

    # for loop
    for item in json_data["DailyForecasts"]:

        # date   
        date_day = item["Date"]

        # temperature 
        min_temp_d = (item["Temperature"]["Minimum"]["Value"])
        max_temp_d = (item["Temperature"]["Maximum"]["Value"])
        # convert temperature to C
        c_min_temp_d = format_temperature(convert_f_to_c(min_temp_d))
        c_max_temp_d = format_temperature(convert_f_to_c(max_temp_d))   
        # for day 
        long_chance_d = (item["Day"]["LongPhrase"])
        long_chance_n = (item["Night"]["LongPhrase"])
        rain_chance_d = (item["Day"]["RainProbability"])
        rain_chance_n = (item["Night"]["RainProbability"])


        # final print list
        line6 = f"-------- {convert_date(date_day)} --------"
        flist_daily.append(line6)
        line7 = f"Minimum Temperature: {c_min_temp_d}"
        flist_daily.append(line7)
        line8 = f"Maximum Temperature: {c_max_temp_d}"
        flist_daily.append(line8)
        line9 = f"Daytime: {long_chance_d}"
        flist_daily.append(line9)
        line10 = f"    Chance of rain:  {rain_chance_d}%"
        flist_daily.append(line10)
        line11 = f"Nighttime: {long_chance_n}"
        flist_daily.append(line11)
        line12 = f"    Chance of rain:  {rain_chance_n}%\n"
        flist_daily.append(line12)


        # sum totals 
        max_temp_a += max_temp_d
        min_temp_a += min_temp_d
        number_days += 1

    # for 8 day forecast
        if min_temp_w == 0:
            min_temp_w = min_temp_d
            min_date_w = item["Date"]
        else:
            if min_temp_d < min_temp_w:
                min_temp_w = min_temp_d
                min_date_w = item["Date"]


        if max_temp_w == 0:
            max_temp_w = max_temp_d
            max_date_w = item["Date"]
        else:
            if max_temp_d > max_temp_w:
                max_temp_w = max_temp_d
                max_date_w = item["Date"]


    # convert temperature to C
    c_min_temp_w = format_temperature(convert_f_to_c(min_temp_w))
    c_max_temp_w = format_temperature(convert_f_to_c(max_temp_w))    

    
    # final print list
    line1 = f"{number_days} Day Overview"
    flist_summary.append(line1)
    line2 = f"    The lowest temperature will be {c_min_temp_w}, and will occur on {convert_date(min_date_w)}."
    flist_summary.append(line2)
    line3 = f"    The highest temperature will be {c_max_temp_w}, and will occur on {convert_date(max_date_w)}."
    flist_summary.append(line3)
    line4 = f"    The average low this week is {format_temperature(convert_f_to_c(calculate_mean(min_temp_a, number_days)))}."
    flist_summary.append(line4)
    line5 = f"    The average high this week is {format_temperature(convert_f_to_c(calculate_mean(max_temp_a, number_days)))}.\n\n"
    flist_summary.append(line5)
    
    # # format final print list
    flist_summary = "\n".join(flist_summary)
    flist_daily = "\n".join(flist_daily)

    # add together final print list
    final_output = f"{flist_summary}{flist_daily}"
    final_output = final_output + "\n"
    return final_output

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_8days.json"))

