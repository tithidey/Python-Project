# take amount as user input
def getAmount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError
            break
        except ValueError():
            print("Invalid amount.")
    return amount
    

# ask what is the source currency
def getCurrency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f"{label} currency (USD/EUR/CAD) : ").upper()
        if currency not in currencies:
            print("Invalid Currency")
        else:
            break
    return currency

def currencyConvertor(amount, source, target):
    exchange_rate = {
        'USD': {'EUR':0.94, 'CAD': 1.40},
        'EUR': {'USD': 1.06, 'CAD': 1.48},
        'CAD': {'USD': 0.72 , 'EUR': 0.68}
        }
    if source == target:
        converted_currency = amount
    else:
        converted_currency = amount * exchange_rate[source][target]
    
    return converted_currency


def main():
    amount = getAmount()
    source_currency = getCurrency('Source')
    target_currency = getCurrency('Target')

    result = currencyConvertor(amount= amount, source= source_currency, target= target_currency)

    print(f"Exchange rate from {source_currency} to {target_currency} = {result} {target_currency}")


main()
    