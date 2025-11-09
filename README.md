# Market Data Scraper (Financial Times)

This Python script retrieves market data from the Financial Times Markets Data page and saves it into four structured CSV files. The script uses `requests` to download the page, `BeautifulSoup` to parse the HTML tables, `pandas` to structure the data, and `re` (regular expressions) to clean and extract values.

## Data Extracted

### 1. Equity Indices
- Index name
- Last recorded value (commas removed for numeric use)
- Daily numeric change
- Daily percentage change

Regex is used to split combined change strings such as `-0.45-0.72%` into:
- `-0.45` (numeric change)
- `-0.72%` (percentage change)

Output file: `Equity_Indices.csv`

### 2. Currency Cross Rates
- Major currency pairs
- Exchange rates relative to: Eurozone, Japan, United Kingdom, United States

No regex cleanup applied in this section.

Output file: `Currency.csv`

### 3. Commodities
- Commodity name (timestamps removed using regex such as `as of ...`)
- Last price (currency/unit text removed)
- Contract information (extracted from price field)
- Daily numeric and percentage change (split using the same regex method as equity indices)

Regex usage includes:
- Removing text after "as of" in commodity names.
- Removing currency/unit suffixes from prices.
- Extracting numeric and percentage change from combined change strings.

Output file: `Commodity.csv`

### 4. Bonds and Interest Rates
- Country
- Two-year bond yield
- Ten-year bond yield

No regex cleanup required here.

Output file: `Bonds_and_Yields.csv`

## Regex Summary

| Purpose | Example Input | Regex Used | Result |
|--------|---------------|------------|--------|
| Split numeric + percentage change | `-0.45-0.72%` | `([+-]?\d+(\.\d+)?)([+-]\d+(\.\d+)?%)` | `-0.45` and `-0.72%` |
| Remove thousands separators | `3,512.24` | `re.sub(",", "", text)` | `3512.24` |
| Remove trailing timestamp text | `Gold as of Nov 07 2025 21:59 GMT` | `re.sub(r"as of.*", "", text, flags=re.IGNORECASE)` | `Gold` |
| Remove currency/unit suffixes | `82.51 USD/t` | `re.sub(r"U.*", "", text, flags=re.IGNORECASE)` | `82.51` |

## Requirements

Install dependencies:
