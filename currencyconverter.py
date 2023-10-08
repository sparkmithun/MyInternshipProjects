import requests

def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print("Error:", data["error"])
            return None

        if target_currency in data["rates"]:
            exchange_rate = data["rates"][target_currency]
            return exchange_rate
        else:
            return None
    except requests.exceptions.RequestException:
        print("Error: Failed to fetch exchange rate data. Please check your internet connection.")
        return None

def main():
    print("Welcome to the Currency Converter!")

    while True:
        try:
            base_currency = input("Enter the source currency (e.g., USD, EUR): ").upper()
            amount = float(input(f"Enter the amount in {base_currency}: "))
            target_currency = input("Enter the target currency (e.g., USD, EUR): ").upper()

            exchange_rate = get_exchange_rate(base_currency, target_currency)

            if exchange_rate is not None:
                converted_amount = amount * exchange_rate
                print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency} (Exchange Rate: 1 {base_currency} = {exchange_rate} {target_currency}).")
            else:
                print("Unsupported currency or invalid conversion.")

            another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
            if another_conversion != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")

if __name__ == "__main__":
    main()
