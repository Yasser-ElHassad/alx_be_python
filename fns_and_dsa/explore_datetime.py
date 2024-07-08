from datetime import datetime,timedelta

current_date  = datetime.now()

def display_current_datetime():  
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M;%S")
    print(f'Current date and time: {formatted_date}')

def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = current_date + timedelta(days= number_of_days)
    print(f'Future date: {future_date.strftime("%Y-%m-%d")}')

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()







