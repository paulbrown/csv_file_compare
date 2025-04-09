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
