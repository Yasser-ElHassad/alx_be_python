import datetime

current_date  = datetime.datetime.now()

def display_current_datetime():  
    print(f'Current date and time: {str(current_date)[:-7]}')

def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = current_date + datetime.timedelta(days= number_of_days)
    print(f'Future date: {str(future_date)[:11]}')



