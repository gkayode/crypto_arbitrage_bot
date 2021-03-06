In its simplest form, crypto arbitrage trading is the process of buying a digital asset on one exchange and selling it (just about) simultaneously on another where the price is higher.


![image](https://user-images.githubusercontent.com/52835575/167238239-f53123dd-9ac6-48e7-9a5b-da932cebfac1.png)


This is a python based crypto arbitrage bot that detect price differences between Coinbase and Kucoin exchanges. The bot returns crypto pairs with price differences greater than a set benchmark (14%).

A sample output is shown below:

![Screen Shot 2022-05-06 at 10 36 30 PM](https://user-images.githubusercontent.com/52835575/167238581-48d34953-c736-4456-91af-8a4e1c28c3e1.png)

Additional things I did:
- I removed the set of codes that does the actual trading. The code here only returns crypto pairs with price differences greater than a set benchmark (14%).
- I also created a server that runs the above code indefinitely at an interval of 5 mins and then emails me if there's a new pair for potential arbitrage trading. This was done on [repl.it](https://replit.com/).
- Lastly, I created a bot on [discord](https://discord.com/) by linking my code on [repl.it](https://replit.com/).

A few warnings:
- Make sure the network address per crypto pair is the same across both exchanges.
    This is so you can transfer crypto across both platforms without a hitch and also to avoid crypto loss.
- There will be a slight lag when transfering crypto across platforms. This is for network confirmations.
- Also, both exchanges have both transaction and transfer fees.

### How to get up and running

1. Clone the repository into a project folder.

2. Navigate to the root folder of the repository, then run the following code to install the dependencies.
    ```Python
    pip install -r requirements.txt
    ```
3. Run the crypto_arbitrage.py file
    ```Python
    python crypto_arbitrage
    ```
    