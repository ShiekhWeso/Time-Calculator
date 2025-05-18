def add_time(start, duration, day=""):
    # days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saterday", "Sunday"]
    try:
        time_part_1, period_1 = start.strip().split()
        start_hour, start_minute = map(int, time_part_1.strip().split(":")) #this line converts the list of ["3","45"] for integers
        if start_minute >= 60:
            print("print the minutes must be less than 60!")
            return
    except Exception:
        print("The must contain the period.")
        return
    
    duration_hour, duration_minute = map(int, duration.strip().split(":"))
    if duration_minute >= 60:
        print("print the minutes must be less than 60!")
        return

    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    
add_time("3:00 ", "2:30")