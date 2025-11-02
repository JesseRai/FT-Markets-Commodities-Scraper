import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://markets.ft.com/data'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

#  step 1: Download the HTML.
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Find the market movers table
commodities_section = soup.find('div', attrs={'data-f2-app-id': 'mod-commodities-and-news-app'})
with open('file.txt', mode="w") as file:
    file.write(commodities_section.prettify())

tables = commodities_section.find_all(class_="mod-ui-table mod-ui-table--freeze-pane")
table = tables[0]
rows = table.find_all("tr")
data = []
for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            name = cols[0].get_text(strip=True)
            price = cols[1].get_text(strip=True)
            data.append({"Commodity": name, "Last Price": price})

df = pandas.DataFrame(data)
df.to_csv("commodities_prices.csv", index=False)
print("Saved commodities_prices.csv")
