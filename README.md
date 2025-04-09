# csv_file_compare

A custom CSV diff utility used to compare records within two CSV files based on known key(s).

## Usage

### Executable (PowerShell)
```bash
./csv_file_compare --previous-csv-filepath="<file.csv>" --current-csv-filepath="<file.csv>" --output-xlsx-filepath="<file.xlsx>" --key="<field>"...
./csv_file_compare --previous-csv-filepath="<file.csv>" --current-csv-filepath="<file.csv>" --key="<field>"...
./csv_file_compare --help
```
  
### Python (Source Code)
```bash
python ./csv_file_compare.py --previous-csv-filepath="<file.csv>" --current-csv-filepath="<file.csv>" --output-xlsx-filepath="<file.xlsx>" --key="<field>" ...
python ./csv_file_compare.py --previous-csv-filepath="<file.csv>" --current-csv-filepath="<file.csv>" --key="<field>" ...
python ./csv_file_compare.py --help
```

## Options

- `--help`                          Show this screen.
- `--previous-csv-filepath=FILE`    Baseline or original file. [default: None] [required] 
- `--current-csv-filepath=FILE`     Current or subsequent file used to compare to baseline. [required]
- `--key=TEXT`                      Primary key(s) or record uniqueness of file. Can be specified multiple times `--key=TEXT --key=TEXT ...` [required]
- `--output-xlsx-filepath=FILE`     Result sent to file containing differences. [defaults to: Differences.xlsx]

## Summary of the Code

The provided Python script is a utility for comparing two CSV files and generating an Excel file with the differences. It uses the `typer` library for CLI functionality and includes the following main features:

### CSV Loading (`load_csv`)

- Reads a CSV file, detects its encoding using `chardet`, and processes its rows into a dictionary keyed by a composite key derived from specified columns.
- Handles specific cases where the first row might contain unwanted metadata (e.g., "Exported").

### Comparison (`compare`)

- Compares two dictionaries (representing the CSV files) to identify:
  - Deleted rows (present in the first file but not the second).
  - Inserted rows (present in the second file but not the first).
  - Updated rows (present in both files but with differing values).

### Excel Output (`build_xlsx_output`)

- Writes the comparison results to an Excel file with three sheets: `DELETED`, `INSERTED`, and `UPDATED`.
- Highlights updated cells in the `UPDATED` sheet using yellow fill.

### Main Functionality (`main`)

- Handles CLI arguments for input/output file paths and keys.
- Validates file paths and keys.
- Calls the `load_csv`, `compare`, and `build_xlsx_output` functions to process the files and generate the output.