async def finetune_interpreter(author_name):
    return [
{'role':'user','content':"""Save the titanic dataset to a csv file. Make sure to import seaborn as sns"""},
{'role':'assistant','content':f"""
import seaborn as sns
import pandas as pd

# Load the Titanic dataset from seaborn
titanic_data = sns.load_dataset('titanic')

# Save the Titanic dataset to a CSV file
filename = 'app/downloads/{author_name}/titanic_dataset.csv'
titanic_data.to_csv(filename, index=False)
"""},
{'role':'user','content':"Can you create a candlestick chart of Tesla's stock price with volume bars for the past six months."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "TSLA"

# Get today's date
end_date = datetime.today()

# Calculate the start date as six months ago from today
start_date = end_date - timedelta(days=180)

# Fetch the historical data for Tesla using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a custom color palette inspired by Tesla's brand colors
colors = ['#E82127', '#FABD42', '#6E6E6E', '#BFBFBF']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the candlestick chart for Tesla stock price for the past six months
filename = "app/downloads/{author_name}/Tesla_candlestick.png"
mpf.plot(data, type='candle', style='yahoo', title="Tesla Stock Price (Last Six Months)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'), volume=True)
plt.close()
"""},{'role':'user','content':"Can you create a candlestick chart of Microsoft's stock price for the past three quarters? Add bars for volume as well."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "MSFT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as three quarters (nine months) ago
start_date = end_date - timedelta(days=270)

# Fetch the historical data for Microsoft using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a custom color palette inspired by Microsoft's brand colors
colors = ['#3C6EB4', '#FFB900', '#B4009E', '#00A300']
sns.set_palette(sns.color_palette(colors))

# Set fivethirtyeight background theme for the plot using Matplotlib
plt.style.use('fivethirtyeight')

# Plot the candlestick chart for Microsoft stock price for the past three quarters
filename = "app/downloads/{author_name}/Microsoft_candlestick.png"
mpf.plot(data, type='candle', style='yahoo', title="Microsoft Stock Price (Last Three Quarters)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'))
plt.close()
"""},
{'role':'user','content':"Can you create a candlestick chart for Apple's stock price in the past 128 days? Add bars for volume."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "AAPL"

# Get today's date
end_date = datetime.today()

# Calculate the start date as 128 days ago from today
start_date = end_date - timedelta(days=128)

# Fetch the historical data for Apple using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a custom color palette inspired by Apple's brand colors
colors = ['#b6b6b6', '#999999', '#e9e9e9', '#d8d8d8']
sns.set_palette(sns.color_palette(colors))

# Set fivethirtyeight background theme for the plot using Matplotlib
plt.style.use('fivethirtyeight')

# Plot the candlestick chart for Apple stock price for the past three quarters
filename = "app/downloads/{author_name}/Apple_candlestick.png"
mpf.plot(data, type='candle', style='yahoo', title="Apple Stock Price (Last 128 days)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'), volume=True)
plt.close()
"""},
{'role':'user','content':"can you plot percent price change for bitcoin, ethereum, and dogecoin for the past three quarters? Use a dark theme, orange for bitcoin, light blue for ethereum, and yellow for dogecoin."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["BTC-USD", "ETH-USD", "DOGE-USD"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as three quarters (nine months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Bitcoin, Ethereum, and Dogecoin using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)["Close"]

# Calculate the percent change for each cryptocurrency
percent_change = data.pct_change()

# Set a dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the percent change for Bitcoin, Ethereum, and Dogecoin for the past three quarters
fig, ax = plt.subplots(figsize=(chart_width, chart_height))
plt.plot(percent_change.index, percent_change[tickers[0]], label="Bitcoin", color='orange')
plt.plot(percent_change.index, percent_change[tickers[1]], label="Ethereum", color='lightblue')
plt.plot(percent_change.index, percent_change[tickers[2]], label="Dogecoin", color='yellow')

plt.title("Percent Change in Cryptocurrency Prices (Last Three Quarters)", fontsize=16, fontweight='bold', color="#FFFFFF")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Percent Change", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()
filename = "app/downloads/{author_name}/bitcoin_ethereum_dogecoin_three_quarters.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot the price of Microsoft and Apple together? Can you add a line of best fit for the pair?"},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["MSFT", "AAPL"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (three months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Microsoft and Apple using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)["Close"]

# Set a custom color palette inspired by Microsoft and Apple's brand colors
colors = ['#3C6EB4', '#FFB900']
sns.set_palette(sns.color_palette(colors))

# Calculate the start date as two quarters (six months) ago
start_date_two_quarters_ago = end_date - timedelta(days=182)

# Filter the historical data for Microsoft and Apple for the past two quarters 
data_two_quarters = data[data.index.to_series() > start_date_two_quarters_ago]

# Take our dates as X. Convert datetime to numerical values.
X = pd.DataFrame((data_two_quarters.index - start_date_two_quarters_ago).days)

# Take the average of the "Close" prices for Microsoft and Apple as Y
y = pd.Series(data_two_quarters.mean(axis=1))

# Fit a linear regression model
regressor = LinearRegression()
regressor.fit(X, y)

# Predict the stock prices using the linear regression model
predicted_prices = regressor.predict(X)

# Set fivethirtyeight background theme for the plot using Matplotlib
plt.style.use('fivethirtyeight')

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Microsoft and Apple for the past two quarters
plt.plot(data.index, data[tickers[0]], label="Microsoft (MSFT)")
plt.plot(data.index, data[tickers[1]], label="Apple (AAPL)")

# Plot the linear regression line
plt.plot(data_two_quarters.index, predicted_prices, color='red', linestyle='--', label='Linear Regression')

plt.title("Microsoft and Apple Stock Prices (Last Two Quarters)", fontsize=16, fontweight='bold', color="#333333")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout() 
filename = "app/downloads/{author_name}/Microsoft_Apple_Two_Quarters.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot Krispy Kreme's stock price for the past six months, as well as a regression line. Do not show volume and do not use candlesticks."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns
import statsmodels.api as sm

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "DNUT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as six months ago from today
start_date = end_date - timedelta(days=180)

# Fetch the historical data for Krispy Kreme using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a custom color palette inspired by Krispy Kreme's brand colors
colors = ['#FFB900', '#DD1100']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the stock price for Krispy Kreme for the past six months
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data['Close'], label="Stock Price")

# Generate regression line
X = np.arange(len(data)).reshape(-1, 1)
X = sm.add_constant(X)
y = data['Close'].values
model = sm.OLS(y, X).fit()
regression_line = model.predict(X)
plt.plot(data.index, regression_line, 'r--', label="Regression Line")

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Krispy Kreme Stock Price (Last Six Months)")

# Set legend
plt.legend()

# Save the plot as an image file
filename = "app/downloads/{author_name}/Krispy_Kreme_Six_Months.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot the price of Microsoft and Apple together? Can you add a line of best fit for each? Furthermore, can you add information about the lines of best fit?"},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["MSFT", "AAPL"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (three months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Microsoft and Apple using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)["Close"]

# Set a custom color palette
colors = ['#3C6EB4', '#FFB900']
sns.set_palette(sns.color_palette(colors))

# Calculate the start date as two quarters (six months) ago
start_date_two_quarters_ago = end_date - timedelta(days=182)

# Filter the historical data for Microsoft and Apple for the past two quarters 
data_two_quarters = data[data.index.to_series() > start_date_two_quarters_ago]

# Take our dates as X. Convert datetime to numerical values.
X = pd.DataFrame((data_two_quarters.index - start_date_two_quarters_ago).days)

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Microsoft and Apple for the past two quarters
plt.plot(data.index, data[tickers[0]], label="Microsoft (MSFT)")
plt.plot(data.index, data[tickers[1]], label="Apple (AAPL)")

# Fit a linear regression model for Microsoft
regressor_msft = LinearRegression()
regressor_msft.fit(X, data_two_quarters[tickers[0]])

# Fit a linear regression model for Apple
regressor_aapl = LinearRegression()
regressor_aapl.fit(X, data_two_quarters[tickers[1]])

# Predict the stock prices using the linear regression models
predicted_prices_msft = regressor_msft.predict(X)
predicted_prices_aapl = regressor_aapl.predict(X)

# Plot the linear regression lines
plt.plot(data_two_quarters.index, predicted_prices_msft, color='red', linestyle='--', label='MSFT Linear Regression')
plt.plot(data_two_quarters.index, predicted_prices_aapl, color='blue', linestyle='--', label='AAPL Linear Regression')

# Add information about the lines of best fit
plt.annotate(f"MSFT: {{regressor_msft.coef_[0]:.2f}}", xy=(data_two_quarters.index[-1], predicted_prices_msft[-1]), xytext=(data_two_quarters.index[-1] - pd.DateOffset(months=1), predicted_prices_msft[-1]), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate(f"AAPL: {{regressor_aapl.coef_[0]:.2f}}", xy=(data_two_quarters.index[-1], predicted_prices_aapl[-1]), xytext=(data_two_quarters.index[-1] - pd.DateOffset(months=1), predicted_prices_aapl[-1]), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.title("Microsoft and Apple Stock Prices (Last Two Quarters)", fontsize=16, fontweight='bold', color="#333333")
plt.xlabel("Date", fontsize=14, color="#333333")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#333333")
plt.legend()

plt.tight_layout()

filename = "app/downloads/{author_name}/Microsoft_Apple_Two_Quarters.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot Disney's volume for the past two blood moons?"},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "DIS"

# Get today's date
end_date = datetime.today()

# Calculate the start date as two blood moons (approximately 59 days) ago
start_date = end_date - timedelta(days=59)

# Fetch the historical data for Disney using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the "Volume" for Disney for the past two blood moons
fig, ax = plt.subplots(figsize=(chart_width, chart_height))
plt.plot(data.index, data["Volume"], color='cyan')  # Change color to cyan

plt.title("Disney Stock Volume (Past Two Blood Moons)", fontsize=16, fontweight='bold', color="#FFFFFF")  # Change color to white
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Volume", fontsize=14, color="#FFFFFF")

plt.tight_layout() 

filename = "app/downloads/{author_name}/Disney_Two_Blood_Moons.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot Disney's volume for the past two blood moons? Use bars and a white background."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "DIS"

# Get today's date
end_date = datetime.today()

# Calculate the start date as two blood moons (approximately 59 days) ago
start_date = end_date - timedelta(days=59)

# Fetch the historical data for Disney using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the volume for Disney for the past two blood moons using bars
fig, ax = plt.subplots(figsize=(chart_width, chart_height))
plt.bar(data.index, data["Volume"], color='blue')

plt.title("Disney Stock Volume (Past Two Blood Moons)", fontsize=16, fontweight='bold', color="#000000")
plt.xlabel("Date", fontsize=14, color="#333333")
plt.ylabel("Volume", fontsize=14, color="#333333")

plt.tight_layout() 
filename = "app/downloads/{author_name}/Disney_Two_Blood_Moons_With_Volume.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot Disney's stock price for the past 28 days? Also include bars for volume."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "DIS"

# Get today's date
end_date = datetime.today()

# Calculate the start date as 28 days ago
start_date = end_date - timedelta(days=28)

# Fetch the historical data for Disney using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a custom color palette inspired by Disney's brand colors
colors = ['#0033CC', '#FF9900']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Disney for the past 28 days
plt.plot(data.index, data["Close"], label="Disney (DIS)")

# Add bars for volume
ax2 = ax.twinx()
ax2.bar(data.index, data["Volume"], alpha=0.3, width=0.5, align='center', color='#FF9900', label="Volume")

plt.title("Disney Stock Price (Past 28 Days)", fontsize=16, fontweight='bold', color="#FFFFFF")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#FFFFFF")
ax2.set_ylabel("Volume", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout() 

filename = "app/downloads/{author_name}/Disney_28_Days_with_Volume.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot Microsoft's stock price for the past three quarters using candlesticks?"},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "MSFT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as three quarters (nine months) ago
start_date = end_date - timedelta(days=365*0.75)

# Fetch the historical data for Microsoft using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a custom color palette inspired by Microsoft's brand colors
colors = ['#3C6EB4', '#FFB900', '#B4009E', '#00A300']
sns.set_palette(sns.color_palette(colors))

filename = "app/downloads/{author_name}/Microsoft_Candlestick_Three_Quarters.png"
# Plot the candlestick chart for Microsoft for the past three quarters
mpf.plot(data, type='candle', style='yahoo', title="Microsoft Stock Price (Last Three Quarters)",
         ylabel="Stock Price (USD)", figsize=(chart_width, chart_height), savefig=filename)
"""},
{'role':'user','content':"can you plot Krispy Kreme's stock price for the past six months, as well as volume?"},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "DNUT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as six months ago from today
start_date = end_date - timedelta(days=180)

# Fetch the historical data for Krispy Kreme using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a custom color palette inspired by Krispy Kreme's brand colors
colors = ['#FF7900', '#E9A600', '#D6D6D6']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the candlestick chart for Krispy Kreme stock price for the past six months
filename = "app/downloads/{author_name}/Krispy_Kreme_Candlestick_Six_Months.png"
mpf.plot(data, type='candle', style='yahoo', title="Krispy Kreme Stock Price (Last Six Months)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'), volume=True)
plt.close()
"""},
{'role':'user','content':"plot Google's stock price chart for the past two weeks using 5-minute data. Then show a line of best fit. Use a dark theme, red for the graph, and green for the line of best fit."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns
import statsmodels.api as sm

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "GOOGL"

# Get today's date and time
end_date = datetime.today()

# Calculate the start date as two weeks ago from today
start_date = end_date - timedelta(days=14)

# Fetch the intraday data for Google using yfinance with 5-minute interval
data = yf.download(ticker, start=start_date, end=end_date, interval='5m',progress=False)

# Set a custom color palette
colors = ['#FF0000', '#00FF00']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the stock price for Google for the past two weeks
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data['Close'], color='red', label="Stock Price")

# Generate regression line
X = np.arange(len(data)).reshape(-1, 1)
X = sm.add_constant(X)
y = data['Close'].values
model = sm.OLS(y, X).fit()
regression_line = model.predict(X)
plt.plot(data.index, regression_line, color='green', linestyle='--', label="Regression Line")

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Google Stock Price (Past Two Weeks)")

# Set legend
plt.legend()

# Save the plot as an image file
filename = "app/downloads/{author_name}/Google_Two_Weeks.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"plot Bumble's stock price chart for the past month using 60-minute interval data. Then add a line of best fit of the form y=mx+b. Add the defining function for the line of best fit to the chart. Use a white theme and yellow for the line graph, green for the line of best fit. Make the lines very thick and stamp a big heart on it."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "BMBL"

# Get today's date
end_date = datetime.today()

# Calculate the start date as one month ago from today
start_date = end_date - timedelta(days=30)

# Fetch the historical data for Bumble using yfinance with 60-minute interval
data = yf.download(ticker, start=start_date, end=end_date, interval="60m",progress=False)

# Set a white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the stock price for Bumble for the past month
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data['Close'], label="Stock Price", color="yellow", linewidth=3)

# Fit a linear regression model
X = np.arange(len(data)).reshape(-1, 1)
y = data['Close'].values
regressor = LinearRegression()
regressor.fit(X, y)
m = regressor.coef_[0]
b = regressor.intercept_

# Generate the line of best fit
line_of_best_fit = m * X + b

# Plot the line of best fit
plt.plot(data.index, line_of_best_fit, 'g--', label="Line of Best Fit", linewidth=3)

# Add the defining function for the line of best fit
defining_function = f"y = {{m:.2f}}x + {{b:.2f}}"
plt.text(data.index[0], data['Close'].iloc[0], defining_function, fontsize=16, color='green', ha='left', va='bottom')

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Bumble Stock Price (Last Month)")

# Add a heart stamp on the chart
plt.text(data.index[-1], data['Close'].iloc[-1], u'\u2764', fontsize=100, color='red', ha='center', va='center')

# Set legend
plt.legend()

# Save the plot as an image file
filename = "app/downloads/{author_name}/Bumble_Stock_Price.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"plot Bumble's stock price chart for the past 2 months using 60-minute interval data. Then add a linear line of best fit of the form y=mx+b. Add the defining function for the line of best fit to the chart. Use a black theme and yellow for the line graph, green for the line of best fit. Make the title HUGE and bold. Make the lines very thick and stamp a big heart on it."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import statsmodels.api as sm

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "BMBL"

# Get today's date
end_date = datetime.today()

# Calculate the start date as 2 months ago from today
start_date = end_date - timedelta(days=60)

# Fetch the historical data for Bumble using yfinance
data = yf.download(ticker, start=start_date, end=end_date, interval='60m',progress=False)

# Set a custom color palette
colors = ['#FFD700', '#008000']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the stock price for Bumble for the past 2 months
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data['Close'], label="Stock Price", linewidth=3)
plt.title("Bumble Stock Price (Past 2 Months)", fontsize=30, fontweight='bold')
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")

# Generate line of best fit
X = np.arange(len(data)).reshape(-1, 1)
X = sm.add_constant(X)
y = data['Close'].values
model = sm.OLS(y, X).fit()
regression_line = model.predict(X)
plt.plot(data.index, regression_line, 'g--', label="Line of Best Fit", linewidth=3)

# Add equation of line of best fit to the chart
equation = f"y = {{model.params[1]:.2f}}x + {{model.params[0]:.2f}}"
plt.text(data.index[1], data['Close'].max(), equation, fontsize=14, color='white', va='top')

# Add a big heart stamp on the chart
plt.text(data.index[-1], data['Close'].min(), '❤', fontsize=100, color='#FFD700', ha='right', va='bottom')

# Set legend
plt.legend()

# Save the plot as a .png image file
filename = "app/downloads/{author_name}/Bumble_2_Months.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot Match Group, Bumble, and Hello Group (NASDAQ:MOMO) for the past two years? Add a line of best fit and information about the line of best fit. Use a white theme, blue for match group, orange for bumble, and green for hello group."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["MTCH", "BMBL", "MOMO"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as two years ago from today
start_date = end_date - timedelta(days=365*2)

# Fetch the historical data for Match Group, Bumble, and Hello Group using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)["Close"]

# Set a white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the stock prices for Match Group, Bumble, and Hello Group for the past two years
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data.index, data[tickers[0]], label="Match Group (MTCH)", color="blue")
plt.plot(data.index, data[tickers[1]], label="Bumble (BMBL)", color="orange")
plt.plot(data.index, data[tickers[2]], label="Hello Group (MOMO)", color="green")

# Calculate the start date as one year ago from today
start_date_one_year_ago = end_date - timedelta(days=365)

for ticker in tickers:
    # Fit a linear regression model for the past year
    X = np.arange(len(data[ticker])).reshape(-1, 1)
    y = data[ticker].values
    regressor = LinearRegression()
    regressor.fit(X, y)

    # Generate the line of best fit for the past year
    line_of_best_fit = regressor.predict(X)

    # Plot the line of best fit for the past year
    plt.plot(data.index, line_of_best_fit, linestyle='--', linewidth=2, label=f"{{ticker}} Regression Line")

    # Add information about the regression line
    equation = f"y = {{regressor.coef_[0]:.2f}}x + {{regressor.intercept_:.2f}}"
    plt.text(data.index[-1], data[ticker].iloc[-1], equation, fontsize=10, color='black', ha='right', va='bottom')

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Match Group, Bumble, and Hello Group Stock Prices (Past Two Years)")

# Set legend
plt.legend()

# Save the plot as a .png image file
filename = "app/downloads/{author_name}/Stock_Prices_Match_Bumble_Hello.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot Match Group, Bumble, and Hello Group (NASDAQ:MOMO) for the past two years? Add a line of regression for the past year for each symbol and information about the regression lines. Use a white theme, blue for match group, orange for bumble, and green for hello group."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import statsmodels.api as sm

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["MTCH", "BMBL", "MOMO"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as two years ago from today
start_date = end_date - timedelta(days=365*2)

# Fetch the historical data for Match Group, Bumble, and Hello Group using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)['Adj Close']

# Set a custom color palette for each stock
colors = ['#007BFF', '#FF8800', '#00C851']
sns.set_palette(sns.color_palette(colors))

# Set white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the stock prices for Match Group, Bumble, and Hello Group for the past two years
plt.figure(figsize=(chart_width, chart_height))
for ticker in tickers:
    plt.plot(data[ticker], label=ticker)

# Generate regression lines for the past year for each stock
for ticker in tickers:
    stock_data = data[ticker].iloc[-365:]
    X = np.arange(len(stock_data)).reshape(-1, 1)
    X = sm.add_constant(X)
    y = stock_data.values
    model = sm.OLS(y, X).fit()
    regression_line = model.predict(X)
    plt.plot(stock_data.index, regression_line, '--', linewidth=2)

    # Add information about the regression line
    m = model.params[1]
    b = model.params[0]
    defining_function = f"y = {{m:.2f}}x + {{b:.2f}}"
    plt.text(stock_data.index[0], stock_data.iloc[0], defining_function, fontsize=12, color='black', ha='left', va='bottom')

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Stock Prices for Match Group, Bumble, and Hello Group (Last Two Years)")

# Set legend
plt.legend()

# Save the plot as an image file
filename = "app/downloads/{author_name}/Stock_Prices.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"can you plot apples, google's, and Microsoft's stock price for the last four quarters. Add a best fit line for the group for the last two quarters. Use a dark theme, make the lines very thick, white for apple, orange for google, and blue for Microsoft."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["AAPL", "GOOGL", "MSFT"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (one year) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Apple, Google, and Microsoft using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)["Close"]

# Set a dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the stock prices for Apple, Google, and Microsoft for the last four quarters
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data.index, data[tickers[0]], color='white', linewidth=3, label="Apple (AAPL)")
plt.plot(data.index, data[tickers[1]], color='orange', linewidth=3, label="Google (GOOGL)")
plt.plot(data.index, data[tickers[2]], color='blue', linewidth=3, label="Microsoft (MSFT)")

# Calculate the start date as two quarters (six months) ago
start_date_two_quarters_ago = end_date - timedelta(days=182)

# Filter the historical data for Apple, Google, and Microsoft for the last two quarters
data_two_quarters = data[data.index.to_series() > start_date_two_quarters_ago]

# Take our dates as X. Convert datetime to numerical values.
X = pd.DataFrame((data_two_quarters.index - start_date_two_quarters_ago).days)

# Fit a linear regression model for the group
regressor_group = LinearRegression()
regressor_group.fit(X, data_two_quarters.mean(axis=1))

# Predict the stock prices using the linear regression model
predicted_prices_group = regressor_group.predict(X)

# Plot the linear regression line for the group
plt.plot(data_two_quarters.index, predicted_prices_group, color='green', linestyle='--', linewidth=3, label='Group Linear Regression')

plt.title("Stock Prices for Apple, Google, and Microsoft (Last Four Quarters)", fontsize=16, fontweight='bold', color="#FFFFFF")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()

filename = "app/downloads/{author_name}/Stock_Prices_Last_Four_Quarters.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"create a matrix plot using the iris dataset."},
{'role':'assistant','content':f"""
import seaborn as sns
import matplotlib.pyplot as plt

# Set the dark background theme
plt.style.use('dark_background')

# Load the iris dataset from seaborn
iris = sns.load_dataset('iris')

# Create a matrix plot using the iris dataset
sns.pairplot(iris)

# Save the plot as a .png image
filename = "app/downloads/{author_name}/iris_matrix_plot.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()

"""},
{'role':'user','content':"Plot Tesla's stock price for the past 5 years. For each 12 month period in the date range, add a line of best fit. There should be a total of 5 lines of best fit. Use a white background and a thick red line for Tesla's price."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "TSLA"

# Get today's date
end_date = datetime.today()

# Calculate the start date as 5 years ago from today
start_date = end_date - timedelta(days=365 * 5)

# Fetch the historical data for Tesla using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)["Close"]

# Set a white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the stock price for Tesla for the past 5 years with a thick red line
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data.index, data, color='red', linewidth=2)

# Calculate the start and end dates for each 12-month period
date_ranges = []
current_date = start_date
while current_date < end_date:
    next_date = current_date + timedelta(days=365)
    date_ranges.append((current_date, next_date))
    current_date = next_date

for i, (start, end) in enumerate(date_ranges):
    # Filter the data for the current 12-month period
    filtered_data = data[(data.index >= start) & (data.index < end)]
    X = np.arange(len(filtered_data)).reshape(-1, 1)
    y = filtered_data.values

    # Fit a linear regression model for the current 12-month period
    regressor = LinearRegression()
    regressor.fit(X, y)

    # Generate the line of best fit for the current 12-month period
    line_of_best_fit = regressor.predict(X)

    # Plot the line of best fit for the current 12-month period
    plt.plot(filtered_data.index, line_of_best_fit, linestyle='--', linewidth=1.5, label=f"Line of Best Fit {{i+1}}")

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Tesla Stock Price (Past 5 Years)")

# Set legend
plt.legend()

# Save the plot as a .png image file
filename = "app/downloads/{author_name}/Tesla_Stock_Price_With_Lines_Of_Best_Fit.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"Plot Tesla's stock price for the past five years. Then add a line to approximate the price using a polynomial of degree 2, 3, and 4."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

ticker = "TSLA"

# Get today's date
end_date = datetime.today()

# Calculate the start date as five years ago from today
start_date = end_date - timedelta(days=5*365)

# Fetch the historical data for Tesla using yfinance
data = yf.download(ticker, start=start_date, end=end_date,progress=False)

# Set a dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the stock price for Tesla for the past five years
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data['Close'], label="Stock Price", linewidth=3)
plt.title("Tesla Stock Price (Past Five Years)", fontsize=16, fontweight='bold')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Stock Price (USD)", fontsize=14)

# Generate polynomial features of degrees 2, 3, and 4
X = np.arange(len(data)).reshape(-1, 1)
poly_features_2 = PolynomialFeatures(degree=2).fit_transform(X)
poly_features_3 = PolynomialFeatures(degree=3).fit_transform(X)
poly_features_4 = PolynomialFeatures(degree=4).fit_transform(X)

# Fit linear regression models for each polynomial degree
regressor_2 = LinearRegression().fit(poly_features_2, data['Close'])
regressor_3 = LinearRegression().fit(poly_features_3, data['Close'])
regressor_4 = LinearRegression().fit(poly_features_4, data['Close'])

# Predict the stock prices using the linear regression models
predicted_prices_2 = regressor_2.predict(poly_features_2)
predicted_prices_3 = regressor_3.predict(poly_features_3)
predicted_prices_4 = regressor_4.predict(poly_features_4)

# Plot the polynomial approximations
plt.plot(data.index, predicted_prices_2, label="Degree 2", linewidth=2)
plt.plot(data.index, predicted_prices_3, label="Degree 3", linewidth=2)
plt.plot(data.index, predicted_prices_4, label="Degree 4", linewidth=2)

plt.legend()
plt.tight_layout()

# Save the plot as a .png image file
filename = "app/downloads/{author_name}/Tesla_Stock_Price_Polynomial_Approximation.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"Plot Apple, Microsoft, Google, Meta's stock price percent change for the past two years. Use a white theme and playful colors. Stamp a large heart on it using unicode."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["AAPL", "MSFT", "GOOGL", "META"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as two years ago from today
start_date = end_date - timedelta(days=365*2)

# Fetch the historical data for Apple, Microsoft, Google, and Meta using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)["Close"]

# Calculate percent change for each stock
percent_change_data = data.pct_change() * 100

# Set a playful color palette
colors = ['#FF4081', '#448AFF', '#FFC107', '#4CAF50']
sns.set_palette(sns.color_palette(colors))

# Set white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the percent change for Apple, Microsoft, Google, and Meta for the past two years
plt.figure(figsize=(chart_width, chart_height))
for ticker in tickers:
    plt.plot(percent_change_data.index, percent_change_data[ticker], label=ticker)

# Add a large heart stamp on the chart
plt.text(percent_change_data.index[-1], percent_change_data.max().max(), '❤', fontsize=200, color='black', ha='right', va='top')

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Percent Change")
plt.title("Stock Price Percent Change for Apple, Microsoft, Google, and Meta (Last Two Years)")

# Set legend
plt.legend()

# Save the plot as an image file
filename = "app/downloads/{author_name}/Stock_Price_Percent_Change.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"Plot Apple, Google, Meta, and Microsofit's stock price on a chart. Standardize the results and add a line of best fit for the group. Use playful colors and a large font for the title. Make the font for the axis text larger as well."},
{'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["AAPL", "GOOGL", "FB", "MSFT"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as one year ago from today
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Apple, Google, Meta, and Microsoft using yfinance
data = yf.download(tickers, start=start_date, end=end_date,progress=False)["Close"]

# Standardize the stock prices
standardized_data = (data - data.mean()) / data.std()

# Set a playful color palette
colors = ['#FF0000', '#00FF00', '#0000FF', '#FF00FF']
sns.set_palette(sns.color_palette(colors))

# Set plot style and size
plt.style.use('default')
plt.figure(figsize=(chart_width, chart_height))

# Plot the standardized stock prices for Apple, Google, Meta, and Microsoft
for ticker in tickers:
    plt.plot(standardized_data.index, standardized_data[ticker], label=ticker)

# Fit a linear regression model
X = np.arange(len(standardized_data)).reshape(-1, 1)
y = standardized_data.mean(axis=1).values
regressor = LinearRegression()
regressor.fit(X, y)

# Generate the line of best fit for the group
line_of_best_fit = regressor.predict(X)

# Plot the line of best fit
plt.plot(standardized_data.index, line_of_best_fit, 'k--', label='Line of Best Fit')

# Set plot labels and title
plt.xlabel("Date", fontsize=14)
plt.ylabel("Standardized Stock Price", fontsize=14)
plt.title("Standardized Stock Prices of Apple, Google, Meta, and Microsoft", fontsize=24, fontweight='bold')

# Set font size for tick labels
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Set legend
plt.legend()

# Save the plot as a .png image file
filename = "app/downloads/{author_name}/Stock_Prices_Apple_Google_Meta_Microsoft.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"""Plot Google's stock price for the past year. Add a line of best fit."""},
    {'role':'assistant','content':f"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Download Google's stock price data
data = yf.download('GOOGL','2020-01-01','2021-12-31')

# Prepare data for linear regression line
X = (data.index - data.index[0]).days.values.reshape(-1,1)
y = data['Close'].values

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Generate a prediction y based on X
y_pred = model.predict(X)

# Plotting the actual prices
plt.figure(figsize=(10,5))
plt.plot(data.index, data['Close'])

# Plotting the line of best fit
plt.plot(data.index, y_pred, color='red')

plt.title("Google's Stock Price for the Past Year with Line of Best Fit")
plt.xlabel('Date')
plt.ylabel('Price')
plt.savefig('app/downloads/{author_name}/google_stock_price.png')
plt.show()

"""}
]