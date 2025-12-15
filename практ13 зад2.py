def create_calendar(month_name, year, days_count):

    print(f'calendar: {month_name} {year}')
    print()  

   
    day = 1  
    while day <= days_count:
        week = []  

     
        for _ in range(7):
            if day <= days_count:
                week.append(str(day))  
                day += 1  
            else:
                break  

  
        print(' '.join(week))
create_calendar('Randomner', 2045, 23)
