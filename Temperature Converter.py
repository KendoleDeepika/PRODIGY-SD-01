def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

while True:
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '4':
        break
    
    temperature = float(input("Enter the temperature value: "))
    
    if choice == '1':
        converted_fahrenheit = celsius_to_fahrenheit(temperature)
        converted_kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} degrees Celsius is equal to {converted_fahrenheit} degrees Fahrenheit and {converted_kelvin} Kelvin.")
    elif choice == '2':
        converted_celsius = fahrenheit_to_celsius(temperature)
        converted_kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} degrees Fahrenheit is equal to {converted_celsius} degrees Celsius and {converted_kelvin} Kelvin.")
    elif choice == '3':
        converted_celsius = kelvin_to_celsius(temperature)
        converted_fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} Kelvin is equal to {converted_celsius} degrees Celsius and {converted_fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")

