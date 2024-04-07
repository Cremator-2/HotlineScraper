# Hotline Scraper Usage Guide

## Running the Script

To run the script, use the following command in your terminal:

```python main.py -s Search_Term1 Search_Term2 -p Number_of_Pages```


- Replace `Search_Term1` and `Search_Term2` with your search queries. Use underscores (`_`) instead of spaces in your search terms.
- Replace `Number_of_Pages` with the number of pages you want to scrape for each search term.

### Examples

```python main.py -s GeForce_RTX_4080_SUPER Intel_Core_i7-14700 -p 2```


```python main.py --search GeForce_RTX_4080_SUPER Intel_Core_i7-14700 --pages 2```


```python main.py -s GeForce_RTX_4080_SUPER```

Default: 1 page


This command will search for "GeForce RTX 4080 SUPER" and "Intel Core i7-14700" across 2 pages each.

## Output

The script outputs CSV files with the search results. Each search term generates a separate CSV file named using the pattern `hotline_search__Search_Term__Current_Time.csv`.

### CSV Format

The CSV files contain the following columns:

- Name
- Price
- Link
- Description
- Offers
- Product website
- Specification

## Multiple Searches

You can perform multiple searches in one run by specifying multiple search terms separated by spaces (use underscores for spaces within search terms).
