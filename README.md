# Pap-ey: Stock Trading Application

**Pap-ey** is a Tkinter-based desktop application designed to help users manage their stock investments. It allows users to view stock prices, perform transactions (buy/sell), and visualize stock price trends using Plotly.

## Features

- **Stock Price Lookup**: Retrieve and display the current price of a stock.
- **Transaction Management**: Perform buy and sell transactions, and track portfolio changes.
- **Portfolio Tracking**: View the current state of your investment portfolio and calculate profit and loss.
- **Stock Price Visualization**: Generate and view candlestick charts for stock price trends.
- **Interactive UI**: User-friendly graphical interface for easy interaction.

## Requirements

- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `yfinance`
  - `plotly`
  - `pandas`
  - `requests`
  - `beautifulsoup4`
    
## Files

- variables.csv: Stores variables such as money account, money invested, and profit/loss.
- portfolio.csv: Stores the user's stock portfolio.
- 1234.png: Background image for the Tkinter window.
- redirect.png: Image for the redirect button (if available).
- stock_plot.html: Generated HTML file for stock price visualization (created dynamically).

## How to Run

1. Clone or download the repository.
2. Ensure all required libraries are installed.
3. Place the necessary image files (1234.png, redirect.png) in the working directory.

## Usage

- View Current Prices:
   - Enter the stock symbol in the text entry field.
   - Click "Get Price" to retrieve and display the current price of the stock.
- Perform Transactions:
  - Enter the stock symbol and quantity in the respective fields.
  - Click "BUY" to purchase the stock or "SELL" to sell it.
  - The application will update the portfolio and display the current state of money in the account and money invested.
- Calculate Profit and Loss:
  - Click "Current P&L" to calculate and display the profit or loss based on the current portfolio value and money invested.
- View Stock Charts:
  - Enter the stock symbol and click "View Chart" or the redirect button to open a candlestick chart of the stock's price trends in your default web browser.

## Notes

- Ensure that the variables.csv and portfolio.csv files are in the same directory as the script. These files are automatically created if they do not exist.
- The application uses requests and BeautifulSoup for web scraping stock prices. Ensure that you have a stable internet connection.
