import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
data = [
    112, 118, 132, 129, 121, 135,
    148, 148, 136, 119, 104, 118,
    115, 126, 141, 135, 125, 149,
    170, 170, 158, 133, 114, 140,
    145, 150, 165, 160, 155, 170,
    190, 188, 175, 160, 145, 165,
    170, 180, 195, 190, 185, 200
]
series = pd.Series(data)
print("Time Series Data:")
print(series)
plt.figure(figsize=(10, 4))
plt.plot(series, marker='o')
plt.title("Time Series Data")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.show()
acf_values = acf(series, nlags=35)
print("\nACF Values:")
for lag, value in enumerate(acf_values):
    print("Lag", lag, ":", round(value, 4))
plt.figure(figsize=(12, 5))
plot_acf(series, lags=35)
plt.title("ACF for First 35 Lags")
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.show()
