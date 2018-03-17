#!/usr/bin/python

import requests
import json

class DataPuller(object):
    def __init__():
        lunoBidPrice = 0
        lunoAskPrice = 0
        lunoBidUSD = 0
        lunoAskUSD = 0
        zarusd = 0
        coinbaseBidPrice = 0
        coinbaseAskPrice = 0
        lunoFees = 0
        coinbaseFees = 0

        sources = {
            'luno': 'https://api.mybitx.com/api/1/ticker?pair=XBTZAR',
            'alphavantage': 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=ZAR&apikey=9EMJICPXUQ6Q8D9H',
            'coinbase_buy':'https://api.coinbase.com/v2/prices/BTC-USD/buy',
            'coinbase_sell': 'https://api.coinbase.com/v2/prices/BTC-USD/sell'
        }

    def retrieve_data(self, source):
        if source in self.sources.keys:
            data = json.loads(requests.get(self.sources[source]))
            return data

poo bum wee wee
