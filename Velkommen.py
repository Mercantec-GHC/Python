import numpy as np
import pandas as pd
from datetime import date, timedelta
import yfinance as yf
import matplotlib.pyplot as plt

Start = date.today() - timedelta(365)
End = date.today()

def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, start=Start, end=End))
    return Asset

microsoft = closing_price('MSFT')

# Konverter 'Adj Close' kolonnen til en NumPy-array
adj_close_prices = microsoft['Adj Close'].values

# Plot af de justerede lukkepriser ved hjælp af NumPy-array
plt.plot(adj_close_prices)
plt.show()

# Beregning af gennemsnit og standardafvigelse ved hjælp af NumPy
avg_price = np.mean(adj_close_prices)
std_dev = np.std(adj_close_prices)

print("Gennemsnitlig justeret lukkepris:", avg_price)
print("Standardafvigelse af justerede lukkepriser:", std_dev)
