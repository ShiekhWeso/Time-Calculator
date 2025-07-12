def add_time(start, duration, day=""):
    days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saterday", "Sunday"]
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

    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    total_hours = start_hour + duration_hour + extra_hours
    days_later = total_hours // 24
    
    period_flips = (total_hours - 1) // 12    #(12 - 1) // 12 = 11 // 12 = 0   #(13 - 1) // 12 = 12 // 12 = 1
    if period_flips % 2 == 1:
        period_1 = "PM" if period_1 == "AM" else "AM"
        
    display_hour = total_hours % 12
    if display_hour == 0:
        display_hour = 12
    
    result = f"{display_hour}:{remaining_minutes:02d} {period_1}"
    if day:
        start_day_index = days.index(day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = days[new_day_index]
        result += f", {new_day}"
    if days_later == 1:
        result += " (nextday)"
    elif days_later > 1:
    print(result)
    
add_time("3:00 PM", "3:10", "sunday")