# Custom Dataset Loader

This Python utility function, `load`, is designed to load and display basic information about datasets in various formats. It supports `.csv`, `.xlsx`, `.txt`, and `.json` file types and provides essential insights into the data, such as dimensions, data types, missing values, duplicate rows, and memory usage.

## Features

- **File Format Support**: The function can load datasets in CSV, Excel, JSON, and TXT formats.
- **Automatic Data Inspection**: Displays key information about the dataset, including dimensions, data types, presence of missing values, and duplicate rows.
- **Memory Usage**: Provides memory usage details of the dataset.

## Installation

Ensure that you have the following dependencies installed:

```bash
pip install pandas numpy
```
## Usage

### Function Signature

```bash
load(path, info=True)
```
- **'path'**(str):  The file path to the dataset you wish to load. Supported formats include '.csv', '.xlsx', '.txt', and '.json'.
- **'info'**(bool, default=True):  When set to 'True', the function will print detailed information about the dataset.

## Example

```python
from custom_loader import load

# Load a dataset and display information
path = "path/to/your/dataset.csv"
data = load(path, info=True)

# Access the data for further analysis
print(data.head())
```

## Output
When info = True, the function will output:

- Confirmation of successful data import.
- The number of rows and columns in the dataset.
- Details about the data types of columns, including the count of object, integer, float, and boolean types.
- Information about missing values in the dataset.
- Information about duplicate rows, if any.
- The data types of each column.
- Memory usage of the dataset.

## Notes
- The function will raise a ValueError if the provided file format is unsupported.
- Ensure that the dataset is properly formatted and accessible at the specified path.

**This utility is a helpful starting point for data exploration and can be easily integrated into data analysis workflows.**

