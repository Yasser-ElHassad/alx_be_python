*datetime

def display_current_datetime():
    current_date  = datetime.now()
    print(f'Current date and time: {str(current_date)[:-7]}')
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    print(f'Future date: {str(current_date + timedelta(days= number_of_days))[:11]}')



display_current_datetime()
