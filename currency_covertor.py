while True:
    targetValue = int(input('Enter the amount: '))
    if targetValue <= 0:
        print('Invalid amount')
    else:
        sourceCurrency = input('What is your source currency: USD/EUR/CAD? ')
        targetCurrency = input('What is your target currency: USD/EUR/CAD? ')

        if sourceCurrency == targetCurrency:
            print(sourceCurrency)
        else:
            if sourceCurrency == 'USD' and targetCurrency == 'EUR':
                result = targetValue / .94
                print(result)                
                break
            elif sourceCurrency == 'USD' and targetCurrency == 'CAD':
                result = targetValue * 1.39
                print(result)                
                break
            elif sourceCurrency == 'EUR' and targetCurrency == 'USD':
                result = targetValue * 1.06
                print(result)                
                break
            elif sourceCurrency == 'EUR' and targetCurrency == 'CAD':
                result = targetValue * 1.48
                print(result)                
                break
            elif sourceCurrency == 'CAD' and targetCurrency == 'USD':
                result = targetValue / .74
                print(result)                
                break
            elif sourceCurrency == 'USD' and targetCurrency == 'EUR':
                result = targetValue / .67
                print(result)                
                break
            else:
                break
            
            
            
            

