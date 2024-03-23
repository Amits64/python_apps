import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Set up your CoinGecko API key
COINGECKO_API_KEY = "CG-Tgnxg1EuxNrg6nzQTyGZrJk4"

# Set the float format for pandas to avoid scientific notation
pd.options.display.float_format = '{:.2f}'.format

def get_crypto_data():
    """
    Fetches cryptocurrency data from CoinGecko.
    Returns a DataFrame with relevant information.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "inr",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)
    return df

def analyze_crypto_data(df):
    """
    Analyzes cryptocurrency data and identifies potential investments.
    """
    df["expected_return"] = (df["price_change_percentage_24h"] / 100) + 1
    df["expected_price"] = df["current_price"] * df["expected_return"]
    df.sort_values(by="expected_return", ascending=False, inplace=True)
    top_n = 10
    top_cryptos = df.head(top_n)
    return top_cryptos[["name", "symbol", "current_price", "expected_return", "expected_price"]]

def predict_crypto_prices(df):
    """
    Predicts cryptocurrency prices using a linear regression model.
    """
    X = df.select_dtypes(include=[np.number]).drop('current_price', axis=1)
    y = df['current_price']
    X = X.fillna(0)
    y = y.fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return predictions, X_test

if __name__ == "__main__":
    crypto_df = get_crypto_data()
    if crypto_df is not None:
        top_investments = analyze_crypto_data(crypto_df)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write("<html><head><title>Crypto Analysis</title></head><body>")
            f.write("<h1>Top Cryptocurrencies for Investment:</h1>")
            f.write(top_investments.to_html(index=False))

            predictions, X_test = predict_crypto_prices(crypto_df)
            if predictions is not None:
                predictions_df = pd.DataFrame({
                    'Cryptocurrency': crypto_df.loc[X_test.index, 'name'],
                    'Current Prediction (INR)': predictions,
                    'Previous Price (INR)': crypto_df.loc[X_test.index, 'current_price']
                })

                f.write("<h1>Predicted Prices for Cryptocurrencies:</h1>")
                f.write(predictions_df.to_html(index=False))
            f.write("</body></html>")
