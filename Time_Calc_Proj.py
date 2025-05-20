def add_time(start, duration, day=""):
    # days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saterday", "Sunday"]
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

    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    
    if new_minute >= 60:
        extra_hours = new_minute // 60
        remaining_minutes = new_minute % 60
        new_hour += extra_hours
    
    if period_1 == "AM" and new_hour % 12 >= 0:
        period_1 == "PM"
        new_hour = new_hour % 12
    elif period_1 == "PM" and new_hour % 12 >= 0:
        period_1 == "AM"
        new_hour = new_hour % 12
    else:
        print("Invalid period! must be AM or PM") 
        return
    
    print(f"'{new_hour}:{remaining_minutes:02d} {period_1}'")
    
add_time("3:00 PM", "12:30")