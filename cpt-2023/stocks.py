import robin_stocks as r

# Login to Robinhood using your API credentials
r.login(username='<YOUR_USERNAME>', password='<YOUR_PASSWORD>', 
        expiresIn=86400, by_sms=True)

# Define the stock you want to buy and the number of shares
stock_symbol = 'AAPL'  # Replace with the stock symbol you want to trade
shares_to_buy = 10  # Replace with the number of shares you want to buy

# Get the latest price for the stock
stock_price = r.stocks.get_latest_price(stock_symbol)[0]
print(stock_price)
# Place a limit order to buy the stock at the current market price
order_response = r.orders.order_sell_limit(TSLA, 10, stock_price)

# Print the order response
print(order_response)

# Logout from Robinhood
r.logout()