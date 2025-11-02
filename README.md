# FT Markets Commodities Scraper

Scrapes the latest commodity prices from the Financial Times Markets Data page and saves them to a CSV file for analysis.

## Description
The script performs the following steps:
1. Sends a GET request to the FT Markets Data homepage using a valid browser User-Agent.
2. Parses the HTML content using BeautifulSoup.
3. Locates the Commodities and News section of the page.
4. Extracts the table of commodity names and their latest prices.
5. Saves the data to a CSV file named commodities_prices.csv.

## Dependencies
Install the required libraries before running the script:
pip install requests beautifulsoup4 pandas

## Usage
Run the script directly with Python:
python ft_commodities_scraper.py

After running, a file named commodities_prices.csv will be created in the same directory, containing two columns:
- Commodity
- Last Price

## Output Example
| Commodity        | Last Price |
|------------------|-------------|
| Gold             | 2,354.10    |
| Brent Crude Oil  | 87.25       |
| Silver           | 28.13       |

## Notes
- The script uses a user-agent header to simulate a normal browser request and avoid blocking.
- The Financial Times may change its site structure over time. If the script stops working, inspect the HTML again and update the selectors accordingly.
- Output encoding is handled automatically by Pandas.

## License
This project is open-source under the MIT License.

## Author
Created by Jesse Rai.
