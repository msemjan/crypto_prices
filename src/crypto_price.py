#!/usr/bin/env python3
import os
import json
import requests
import datetime

# Configuration
cryptos = ['ADA', 'BTC', 'LTC', 'ETH']
currency = 'EUR'
savefile = os.getenv('HOME') + '/vimwiki/crypto_data.wiki'

def get_crypto_price(crypto, currency):
    ans = dict()

    # Prepare url and get data for buy prices
    url = 'https://api.coinbase.com/v2/prices/{}-{}/buy'.format(crypto, currency)
    resp = requests.get(url)
    
    # Decode received JSON into a python dict
    resp = json.loads(resp.content)

    # Check for the expected format and grab inner dict
    if 'data' in resp:
        resp = resp['data']

    # Check for the expected format and print buy values of crypto 
    if 'base' in resp and 'currency' in resp and 'amount' in resp:
        ans['base'] = resp['base']
        ans['currency'] = resp['currency']
        ans['buy'] = resp['amount']

    # Prepare url and get data for sell prices
    url = 'https://api.coinbase.com/v2/prices/{}-{}/buy'.format(crypto, currency)
    resp = requests.get(url)
    
    # Decode received JSON into a python dict
    resp = json.loads(resp.content)

    # Check for the expected format and grab inner dict
    if 'data' in resp:
        resp = resp['data']

    # Check for the expected format and print buy values of crypto 
    if 'base' in resp and 'currency' in resp and 'amount' in resp:
        ans['sell'] = resp['amount']
    
    return ans

if __name__ == "__main__":
    # Loop over all desired cryptos
    for crypto in cryptos:
        resp = get_crypto_price(crypto, currency)

        print('{}: Buy 1 {} = {} {},\t\tSell 1 {} = {} {}'.format(resp['base'], resp['base'], resp['buy'], resp['currency'],resp['base'], resp['sell'], resp['currency']))

        if savefile is not None and savefile != '':
            with open(savefile, 'a') as f:
                f.write('{},{},{},{},{}\n'.format(datetime.datetime.now().strftime('%x %X'),resp['base'],resp['currency'],resp['buy'],resp['sell']))
