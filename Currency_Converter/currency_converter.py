def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid amount. Please enter a positive number.")

def get_currency(label):
    currencies = ['USD', 'EUR', 'INR', 'AUD']
    while True:
        currency = input(f"Enter the {label} currency (USD, EUR, INR, AUD): ").upper()
        if currency in currencies:
            return currency
        else:
            print("Invalid currency. Please choose from USD, EUR, INR, AUD.")

def convert(amount, source_currency, target_currency):
    exchange_rates = {
        'USD': {'EUR': 0.85, 'INR': 74.0, 'AUD': 1.35},
        'EUR': {'USD': 1.18, 'INR': 88.0, 'AUD': 1.59},
        'INR': {'USD': 0.013, 'EUR': 0.011, 'AUD': 0.018},
        'AUD': {'USD': 0.74, 'EUR': 0.63, 'INR': 55.0}
    }
    
    if source_currency == target_currency:
        return amount
    
    rate = exchange_rates[source_currency][target_currency]
    return amount * rate

def main():
    amount = get_amount()
    source_currency = get_currency("source")
    target_currency = get_currency("target")
    
    converted_amount = convert(amount, source_currency, target_currency)
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")
    
    
if __name__ == "__main__":
    main()