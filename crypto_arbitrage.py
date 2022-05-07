#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:37:18 2022

@author: gboladekayode
"""

import pandas as pd
import json
import requests
from tabulate import tabulate
from kucoin.client import Client

def get_all_coinbase_pairs():
    """Simple script to query the Coinbase API and return pairs"""
    
    if __name__ == "__main__":
        endpoint = 'https://api.exchange.coinbase.com/products'  # this is the coinbase API endpoint for the data
        response = requests.get(endpoint)
        if response.status_code == 200:  # checks if API says our request was OK
            data = json.loads(response.text)  # loads API data response
            # next we create and store the JSON result into a Pandas Dataframe
            data_pd = pd.DataFrame(data)
            data_pd.rename(columns={'id': 'Symbol'}, inplace=True)  # rename one column to be unix
            data_pd.sort_values('Symbol', inplace=True)   # lets sort our results alphabetically
        else:
            print(f"Oops. Bad Response from server. \n {response.status_code}")  # display our error message
    
    coinbase_df=data_pd#[data_pd.quote_currency.isin(['USD','ETH','BTC'])]
    return coinbase_df

def compare_prices(coinbase_df,benchmark=14):
    """compare coinbase price with kucoin price, calculate the percent diff and return pairs greater than benchmark"""
    api_key ='' 
    api_secret = ''
    api_passphrase = ''
    client = Client(api_key, api_secret, api_passphrase)
    d=[]
    for currencys,quote in zip(coinbase_df.Symbol.values,coinbase_df.quote_currency.values):
        if currencys not in ['KEEP-USD','NU-USD','NU-BTC']:
            #response = requests.get("https://api.coinbase.com/v2/prices/"+currencys+"/spot")
            response = requests.get('https://api.pro.coinbase.com/products/'+currencys+'/ticker')
            try:
                data = response.json()
                coinbase_price = float(data["price"])
                if quote!='USD':
                    kucoin_price=float(client.get_ticker(currencys)['price'])
                else:
                    kucoin_price=float(client.get_ticker(currencys+'T')['price'])
                    
                    
                if coinbase_price>kucoin_price:
                    percent_change=((coinbase_price-kucoin_price)/coinbase_price)*100
                elif coinbase_price<kucoin_price:
                    percent_change=((kucoin_price-coinbase_price)/kucoin_price)*100
                else:
                    percent_change=0  
                d.append({'Currency':currencys,'coinbase_price':coinbase_price,'kucoin_price':kucoin_price,
                         'percent_change':percent_change})
            except KeyError:
                pass
            except TypeError:
                pass
    
    df_stat=pd.DataFrame(d)
    benchmark_df=df_stat[df_stat.percent_change>benchmark]
    print(tabulate(benchmark_df, headers = 'keys', tablefmt = 'psql'))
    return benchmark_df


coinbase_df= get_all_coinbase_pairs()
compare_prices(coinbase_df)  



           