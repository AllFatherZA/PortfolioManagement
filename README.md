Stock Market Monthly Close Prices Plotter
This Python script fetches historical stock market data for specified tickers using the yfinance library and plots the monthly closing prices for each ticker. The plot provides a visual representation of the stock performance over the last 5 years.

Prerequisites
Before running the script, ensure you have the following installed:

Python 3.x
yfinance library
matplotlib library
You can install the required libraries using pip:

Copy code
pip install yfinance matplotlib
How to Use
Clone this repository or download the plot_stock_prices.py file.

Open the Python script in your preferred Python environment or IDE.

Modify the tickers list to include the stock symbols of the companies you want to plot. For example:

python
Copy code
tickers = ['SBK.JO', 'NED.JO', 'AAPL', 'GOOGL']
Run the script, and it will fetch the historical data for the specified tickers and display a plot of the monthly closing prices.

Example
Suppose you want to plot the monthly close prices for two South African companies, 'Standard Bank' and 'Nedbank', with the tickers 'SBK.JO' and 'NED.JO', respectively. Update the tickers list as follows:

python
Copy code
tickers = ['SBK.JO', 'NED.JO']
Save the changes and run the script. The plot will be displayed with the monthly close prices for both companies.

Note
Please ensure you have a stable internet connection as the script needs to download historical data from Yahoo Finance.

Disclaimer: This script is for educational and informational purposes only. It does not provide financial advice. Always do your own research and consult with a qualified financial advisor before making any investment decisions.

Happy plotting! 📈
