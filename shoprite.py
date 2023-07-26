import yfinance as yf
import matplotlib.pyplot as plt

def plot_monthly_close_prices(tickers):
    # Fetch historical data for the tickers
    data = yf.download(tickers, period='5y', interval='1mo')
    
    # Extract the 'Close' prices for each ticker
    close_prices = data['Close']
    
    # Plot the close prices
    plt.figure(figsize=(10, 6))
    for ticker in close_prices.columns:
        plt.plot(close_prices.index, close_prices[ticker], label=ticker)
    
    # Customize the plot
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Monthly Close Prices')
    plt.legend()
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Specify the tickers
tickers = ['SBK.JO', 'NED.JO',]

# Call the function to plot the monthly close prices
plot_monthly_close_prices(tickers)
