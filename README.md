# Olist e-commerce data cleaning and EDA

Cleaning and exploratory analysis of the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), about 100k orders placed between 2016 and 2018, spread over nine related tables.

## Status

| notebook | what it does | status |
|---|---|---|
| `01_data_cleaning.ipynb` | Audits all nine tables and writes the cleaned versions to `data_clean/` | Done |
| `02_eda.ipynb` | Light exploratory pass on the cleaned tables | In progress |

## What the cleaning notebook covers

Schema and dtypes, missing values, duplicates, referential integrity, cross-table consistency, value ranges and typos, timestamp order, and the reduction of the geolocation table to one point per zip prefix.

Most of what looks wrong is recorded rather than corrected. A value is changed only where it is clearly wrong, and the orders with timestamps out of order are flagged instead of edited. The summary at the end of the notebook lists what was changed, what was left alone and what the analysis has to keep in mind.

## Running it

1. Download the dataset from Kaggle and put the CSV files in `data/`.
2. Install the dependencies in a virtual environment.
   ```
   pip install pandas numpy matplotlib seaborn pyarrow
   ```
3. Run `01_data_cleaning.ipynb` top to bottom. It writes the cleaned tables as parquet to `data_clean/`.

Built with Python 3.14 and pandas 3. `data/` and `data_clean/` are not tracked by git.

## Repository layout

```
01_data_cleaning.ipynb   cleaning notebook
02_eda.ipynb             EDA notebook
data/                    raw Olist CSVs (not tracked)
data_clean/              cleaned tables as parquet (not tracked, rebuilt by the notebook)
```
```
01_data_cleaning.ipynb   cleaning notebook
02_eda.ipynb             EDA notebook
data/                    raw Olist CSVs (not tracked)
data_clean/              cleaned tables as parquet (not tracked, rebuilt by the notebook)
```
