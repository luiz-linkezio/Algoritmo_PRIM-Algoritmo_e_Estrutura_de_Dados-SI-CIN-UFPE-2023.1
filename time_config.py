def time_config(total_minutes): #If the total minutes is greater than or equal to a day

    if total_minutes >= (60*24*365):
        years = total_minutes / (60*24*365)
        fractional_part = years - int(years)

        days = 365*fractional_part
        fractional_part = days - int(days)

        hours = 24*fractional_part
        fractional_part = hours - int(hours)

        minutes = 60*fractional_part
        fractional_part = minutes - int(minutes)

        seconds = 60*fractional_part

        return int(years), int(days), int(hours), int(minutes), round(seconds, 3)

    elif total_minutes >= (60*24):

        days = total_minutes / (60*24)
        fractional_part = days - int(days)

        hours = 24*fractional_part
        fractional_part = hours - int(hours)

        minutes = 60*fractional_part
        fractional_part = minutes - int(minutes)

        seconds = 60*fractional_part

        return 0, int(days), int(hours), int(minutes), round(seconds, 3)

    elif total_minutes >= 60: #If the total minutes time is greater than or equal to a hour
            
        hours = total_minutes / 60
        fractional_part = hours - int(hours)

        minutes = 60*fractional_part
        fractional_part = minutes - int(minutes)

        seconds = 60*fractional_part

        return 0, 0, int(hours), int(minutes), round(seconds, 3)

    elif total_minutes >= 1: #If the total minutes time is greater than or equal to a second

        minutes = total_minutes    
        fractional_part = minutes - int(minutes)

        seconds = 60*fractional_part

        return 0, 0, 0, int(minutes), round(seconds, 3)

    elif total_minutes < 1: #If the total minutes is lower than a second

        seconds = total_minutes*60    

        return 0, 0, 0, 0, round(seconds, 3)
    
def time_printer(years, days, hours, minutes, seconds):
    times_list = list()

    if years > 0 and years <= 1:
        times_list.append(f"{years} year")
    elif years > 0:    
        times_list.append(f"{years} years")

    if days > 0 and days <= 1:
        times_list.append(f"{days} day")
    elif days > 0:
        times_list.append(f"{days} days")    

    if hours > 0 and hours <= 1:
        times_list.append(f"{hours} hour")
    elif hours > 0:
        times_list.append(f"{hours} hours")  

    if minutes > 0 and minutes <= 1:
        times_list.append(f"{minutes} minute")
    elif minutes > 0:
        times_list.append(f"{minutes} minutes")

    if seconds > 0 and seconds <= 1:
        times_list.append(f"{int(seconds)} second")
    elif seconds > 0:
        times_list.append(f"{int(seconds)} seconds")


    if len(times_list) > 1:
        times_list.insert((len(times_list) - 1), "and")
        times_string = ", ".join(time for time in times_list[:-1]) + " " + times_list[-1]    
    else:
        times_string = ", ".join(times_list)
    print(f"The time spent to find the cure was: {times_string}.")