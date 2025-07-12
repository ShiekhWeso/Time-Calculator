def add_time(start, duration, day=""):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        time_part_1, period_1 = start.strip().split()
        start_hour, start_minute = map(int, time_part_1.strip().split(":")) #this line converts the list of ["3","45"] for integers
        if start_minute >= 60:
            print("print the minutes must be less than 60!")
            return
    except Exception:
        print("The Time must contain the period 'AM or PM'.")
        return
    
    duration_hour, duration_minute = map(int, duration.strip().split(":"))
    if duration_minute >= 60:
        print("print the minutes must be less than 60!")
        return

    start_minutes = start_hour % 12 * 60 + start_minute
    if period_1.upper() == "PM":
        start_minutes += 12 * 60
    
    total_minutes = start_minutes + duration_hour * 60 + duration_minute
    days_later = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)

    new_period = "AM" if (remaining_minutes // 60) < 12 else "PM"
    display_hour = (remaining_minutes // 60) % 12
    display_hour = 12 if display_hour == 0 else display_hour
    display_minute = remaining_minutes % 60
    
    result = f"{display_hour}:{display_minute:02d} {new_period}"
    if day:
        start_day_index = days.index(day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = days[new_day_index]
        result += f", {new_day}"
    if days_later == 1:
        result += " (nextday)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
    print(result)
    
add_time("3:30 PM", "2:12")