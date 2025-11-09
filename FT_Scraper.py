import requests
from bs4 import BeautifulSoup
import pandas
import re

# Get soup.
url = "https://markets.ft.com/data"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get tables.
tables = soup.find_all(class_='mod-ui-table mod-ui-table--freeze-pane')
equity_indices = tables[0]
currencies = tables[1]
commodities = tables[2]
bonds_and_rates = tables[3]

# Build equity indices csv.
equity_indices_data = []
equity_indices_rows = equity_indices.find_all("tr")
for row in equity_indices_rows[1:]:
    cols = row.find_all('td')
    index = cols[0].get_text(strip=True)
    last = cols[1].get_text(strip=True)
    last_cleaned = re.sub(r",", "", last)
    todays_change = cols[2].get_text(strip=True)
    todays_change_cleaned = re.match(r"([+-]?\d+(\.\d+)?)([+-]\d+(\.\d+)?%)", todays_change)
    todays_change_numeric = todays_change_cleaned[1]
    todays_change_percentage = todays_change_cleaned[3]
    equity_indices_data.append({
        "Index": index,
        "Last": last,
        "Today's Change": todays_change_numeric,
        "Today's Change %": todays_change_percentage
    })
df1 = pandas.DataFrame(equity_indices_data)
df1.to_csv("Equity_Indices.csv", index=False)

# Build currencies csv.
currencies_data = []
currencies_rows = currencies.find_all('tr')
for row in currencies_rows[1:]:
    cols = row.find_all('td')
    major_cross_rates = cols[0].get_text(strip=True)
    eurozone = cols[1].get_text(strip=True)
    japan = cols[2].get_text(strip=True)
    united_kingdom = cols[3].get_text(strip=True)
    united_states = cols[4].get_text(strip=True)
    currencies_data.append({
        "Major Cross Rates": major_cross_rates,
        "Eurozone": eurozone,
        "Japan": japan,
        "United Kingdom": united_kingdom,
        "United States": united_states
    })
df2 = pandas.DataFrame(currencies_data)
df2.to_csv("Currency.csv", index=False)

# Build commodities csv.
commodities_data = []
commodities_rows = commodities.find_all('tr')
for row in commodities_rows[1:]:
    cols = row.find_all('td')
    commodity = cols[0].get_text(strip=True)
    commodity_clean = re.sub(r"as of.*", "", commodity, flags=re.IGNORECASE).strip()
    last_price = cols[1].get_text(strip=True)
    last_price_clean = re.sub(r"U.*", "", last_price, flags=re.IGNORECASE).strip()
    contract = re.sub(r"\d{1,3}(,\d{3})*(\.\d+)?", "", last_price)
    todays_change = cols[2].get_text(strip=True)
    todays_change_cleaned = re.match(r"([+-]?\d+(\.\d+)?)([+-]\d+(\.\d+)?%)", todays_change)
    todays_change_numeric = todays_change_cleaned[1]
    todays_change_percentage = todays_change_cleaned[3]
    commodities_data.append({
        "Commodities": commodity_clean,
        "Last Price": last_price_clean,
        "Contract": contract,
        "Today's Change": todays_change_numeric,
        "Today's Change %": todays_change_percentage
    })
df3 = pandas.DataFrame(commodities_data)
df3.to_csv("Commodity.csv", index=False)

# Build bonds and rates csv.
bonds_and_rates_data = []
bonds_and_rates_rows = bonds_and_rates.find_all('tr')
for row in bonds_and_rates_rows[1:]:
    cols = row.find_all('td')
    country = cols[0].get_text(strip=True)
    two_year_yield = cols[1].get_text(strip=True)
    ten_year_yield = cols[2].get_text(strip=True)
    bonds_and_rates_data.append({
        "Country": country,
        "Two Year Yield": two_year_yield,
        "Ten year Yield": ten_year_yield
    })
df4 = pandas.DataFrame(bonds_and_rates_data)
df4.to_csv("Bonds_and_Yields.csv", index=False)

print("Four CSV files have been saved to you current dir.")
