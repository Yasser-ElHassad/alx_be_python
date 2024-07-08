FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsisus(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = int(input("Enter the temperature to convert:"))

celisus_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
def main():
    if celisus_or_fahrenheit == 'F':
        print(f'{float(temperature)}°F is {convert_to_celsisus(temperature)}°C')
    elif celisus_or_fahrenheit == 'C':
        print(f'{float(temperature)}°F is {convert_to_fahrenheit(temperature)}°C')
    else:
        print('Invalid Input')

if __name__ == '__main__':
    main()
