import requests as req

usd = float(input("Enter amount in USD"))
current_rate = req.get('http://free.currencyconverterapi.com/api/v5/convert?q=USD_NPR&compact=y').json()['USD_NPR'][
    'val']  # here ['USD_NPR'] is key of first dictionary and 'val'] is key of dictionary of that dictionary
print('Amount in NPR :', current_rate * usd)
