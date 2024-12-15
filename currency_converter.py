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
    if source_currency == 'USD' and target_currency == 'EUR':
        result = amount * 0.94        
    elif source_currency == 'USD' and target_currency == 'CAD':
        result = amount * 1.40
    elif source_currency == 'EUR' and target_currency == 'USD':
        result = amount * 1.06
    elif source_currency == 'EUR' and target_currency == 'CAD':
        result = amount * 1.48
    elif source_currency == 'CAD' and target_currency == 'USD':
         result = amount * 0.72
    elif source_currency == 'CAD' and target_currency == 'EUR':
        result = amount * 0.68
    else:
        print('NO NO NO. Choose wisely!')
    
    print(f'Your converted amount is {round(result,2)} {target_currency}')
