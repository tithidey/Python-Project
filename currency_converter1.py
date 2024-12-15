## ask the user about amount
while True:
    try:
        amount = float(input('Enter the amount: '))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print('Invalid Amount! ')

# ask the user for source currency
#if invalid print invalid currency

currency = ('USD', 'EUR', 'CAD')
result = 0
exchange_rates = {
    'USD': {'EUR':0.94, 'CAD': 1.40},
    'EUR': {'USD': 1.06, 'CAD': 1.48},
    'CAD': {'USD': 0.72 , 'EUR': 0.68}
}
while True:
     source_currency = input("Source currency? USD/EUR/CAD: ").upper()
     if source_currency  not in currency:
        print("Not Applicable!")
     else:
        break
while True:
    target_currency = input("Target Currency? USD/EUR/CAD: ").upper()
    if target_currency not in currency:
        print("Not Applicable!")
    else:
        break

if source_currency == target_currency:
    print(amount)
else:
    result = amount * exchange_rates[source_currency][target_currency]
    
print(f'Your converted amount is {round(result,2)} {target_currency}')
