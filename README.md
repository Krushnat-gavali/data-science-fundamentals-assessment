# Data Science Fundamentals Assessment

## About the Project

This project covers basic concepts of data science using Python. It includes simple Python programs, statistical calculations, and an analysis of sample order data.

The project helped me practise working with data, calculating summary statistics, identifying relationships between numerical columns, and presenting results using a chart.

## Project Structure

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
│   ├── correlation_matrix.csv
│   ├── orders_by_region.png
│   └── region_summary.csv
└── report/
    └── Data_Science_Fundamentals_Assessment.docx
```

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Topics Covered

### 1. Python Basics
- Variables and data types
- Conditional statements
- Functions
- Lists, tuples, dictionaries, and sets

### 2. Statistics
- Mean, median, and mode
- Minimum and maximum values
- Sample variance
- Sample standard deviation

### 3. Data Analysis
- Reading CSV files using Pandas
- Converting date columns
- Checking missing values
- Generating descriptive statistics
- Grouping data by region
- Calculating correlations between numerical columns

### 4. Data Visualization
- Creating a bar chart using Matplotlib
- Saving the chart for later use

## Dataset

The file `data/sample_data.csv` contains a small sample dataset with information about order regions, product categories, order counts, delivery duration, customer ratings, and dates.

The dataset is intended for practice and does not contain real customer information.

## Results

The analysis generates the following outputs:

- `region_summary.csv` — summary statistics grouped by region.
- `correlation_matrix.csv` — correlations between numerical variables.
- `orders_by_region.png` — a bar chart showing order counts by region.

The sample dataset is small, so the results are useful for practising data analysis rather than drawing conclusions about real-world business operations.

## How to Run the Project

### 1. Install Python

Install Python if it is not already available on your computer.

### 2. Install the required libraries

Open a terminal in the project directory and run:

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Python programs

Run each program from the project root:

```bash
python src/python_basics.py
python src/statistics_analysis.py
python src/data_analysis.py
```

### 4. Open the Jupyter Notebook

Run:

```bash
jupyter notebook
```

Open `notebooks/data_science_fundamentals.ipynb` in the notebook interface.

## Important Note

Correlation shows a relationship between variables, but it does not prove that one variable causes changes in another. Since this project uses a small sample dataset, its results should not be generalized to larger datasets without further analysis.