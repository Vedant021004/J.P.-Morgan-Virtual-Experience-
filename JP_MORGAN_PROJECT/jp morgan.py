
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from datetime import datetime

# Load data
df = pd.read_csv("Nat_Gas.csv")

# Convert dates
df["Dates"] = pd.to_datetime(df["Dates"])

# Convert dates to numerical values
x = df["Dates"].map(datetime.toordinal)
y = df["Prices"]

# Interpolation function
interp_func = interp1d(
    x,
    y,
    kind="linear",
    fill_value="extrapolate"
)

# Estimate price for any date
def estimate_price(date_str):
    """
    Input: date string in YYYY-MM-DD format
    Output: estimated natural gas price
    """
    date = pd.to_datetime(date_str)
    date_num = date.toordinal()

    return float(interp_func(date_num))

# Create future dates (1 year beyond dataset)
future_dates = pd.date_range(
    start=df["Dates"].max(),
    periods=13,
    freq="ME"
)

future_x = future_dates.map(datetime.toordinal)
future_prices = interp_func(future_x)

# Visualization
plt.figure(figsize=(12, 6))

plt.plot(
    df["Dates"],
    df["Prices"],
    marker="o",
    label="Historical Data"
)

plt.plot(
    future_dates,
    future_prices,
    "--",
    label="Extrapolated Prices"
)

plt.xlabel("Date")
plt.ylabel("Natural Gas Price")
plt.title("Natural Gas Price History and 1-Year Forecast")
plt.legend()
plt.grid(True)

plt.show()

# Example usage
print("Estimated price on 2023-06-15:",
      estimate_price("2023-06-15"))

print("Estimated price on 2025-03-15:",
      estimate_price("2025-03-15"))

