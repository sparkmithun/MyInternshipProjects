def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")
    
    while True:
        try:
            value = float(input("Enter the temperature value: "))
            source_unit = input("Enter the source unit (C for Celsius, F for Fahrenheit): ").upper()
            target_unit = input("Enter the target unit (C for Celsius, F for Fahrenheit): ").upper()

            if source_unit == "C" and target_unit == "F":
                result = celsius_to_fahrenheit(value)
                print(f"{value}°C is equal to {result}°F.")
            elif source_unit == "F" and target_unit == "C":
                result = fahrenheit_to_celsius(value)
                print(f"{value}°F is equal to {result}°C.")
            else:
                print("Unsupported unit conversion. Please enter 'C' or 'F' for Celsius or Fahrenheit.")

            another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
            if another_conversion != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
