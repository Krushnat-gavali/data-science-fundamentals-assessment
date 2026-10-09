# Data Science Fundamentals Assessment

A beginner-friendly project demonstrating Python basics, descriptive statistics, data types, data cleaning, summary analysis, correlation, and visualization.

## Project structure

```text
data-science-fundamentals-assessment/
├── README.md
├── requirements.txt
├── data/
│   └── sample_data.csv
├── notebooks/
│   └── data_science_fundamentals.ipynb
├── src/
│   ├── python_basics.py
│   ├── statistics_analysis.py
│   └── data_analysis.py
├── outputs/
└── report/
    └── Data_Science_Fundamentals_Assessment.docx
```

## Requirements

- Python 3.10 or later recommended
- pandas
- matplotlib
- Jupyter (optional, for running the notebook)

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the project

From the project root:

```bash
python src/python_basics.py
python src/statistics_analysis.py
python src/data_analysis.py
```

To open the notebook:

```bash
jupyter notebook
```

Then open `notebooks/data_science_fundamentals.ipynb`.

## Dataset

`data/sample_data.csv` is a small illustrative dataset created for learning. It includes order region, product category, order counts, delivery duration, customer ratings, and dates. It does not contain real customer information.

## What you will learn

1. Variables, conditionals, functions, and collection types.
2. Mean, median, mode, sample variance, and sample standard deviation.
3. Loading CSV files with pandas and converting date columns.
4. Checking missing values and summarizing numeric columns.
5. Grouping data by region and computing correlation.
6. Creating and saving a bar chart with matplotlib.

## Notes

- Correlation indicates association, not causation.
- The dataset is small and illustrative; conclusions should not be generalized to real operations.
- Run the code in your own environment and check the generated outputs before submitting.
- Add your own name and the final report to `report/` before publishing if required by your assessment.
