# Countries I Have Visited Through Books

I want to improve the geographical diversity of the books I read.

Goodreads doesn't show me where my book list authors are from, so I exported my data and wrote a bit of Python code to map the books to countries.

This is not a plug-and-play solution but a starter for people who want to do the same.

![alt text](mydistribution.png)

## Prerequisites

- Python
- Goodreads data exported as CSV
- Time to override the countries that the script got wrong or could not find

## Installation

```bash
python -m venv .venv
source ./.venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage

1. Export your Goodreads data as CSV and save it in the `data` folder.

2. Work in the [scratchpad.ipynb](src/scratchpad.ipynb) Jupyter notebook to get the countries of the authors of the books you read.

3. Manually adjust the [manually_placed.csv](data/manually_placed.csv) file to your needs.
