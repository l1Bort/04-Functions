def time_string(hours, minutes, time_format):
    if time_format == '12':
        if hours >= 12:
            period = 'PM'
        else:
            period = 'AM'
        hours = hours % 12
        if hours == 0:
            hours = 12
        return print(f'{hours}:{minutes:02d} {period}')
    elif time_format == '24':
        return print(f'{hours}:{minutes:02d}')
    else:
        return 'Invalid time format'
    
time_string(15, 38, '24')
time_string(15, 38, '24') 
time_string(8, 3, '24') 
time_string(0, 5, '24') 
time_string(11, 15, '12') 
time_string(0, 7, '12') 
time_string(7, 30, '12') 
time_string(12, 46, '12') 
time_string(13, 10, '12') 
time_string(19, 2, '12')