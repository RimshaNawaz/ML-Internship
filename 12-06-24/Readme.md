# Directory Metadata Analyzer

This project contains a Python script to recursively read all files and folders within a given directory, gather metadata about each file and folder, sort the records by file extension, generate summaries, save the results to CSV files, and create visualizations of the final results.

## Features

- Recursively traverse a directory to gather metadata (file name, file size, folder size, and number of files in the folder).
- Sort the collected file records based on file extension.
- Generate a summary of the results grouped by file extension.
- Save the gathered information and summary to CSV files.
- Create a bar chart visualization of the total size by file extension.

## Prerequisites

Ensure you have the following installed:


- `pandas` library
- `matplotlib` library
- `seaborn` library
- `os` library


## Usage

- Clone the repository:

``` bash 
git clone https://github.com/RimshaNawaz/ML-Internship.git
```

- Navigate to the project directory:

``` bash 
cd 12-06-24
```

- You can install the required Python libraries using the following command:

```bash
pip install pandas matplotlib seaborn
```

- Open the main.py file and set the root_dir variable to the path of the directory you want to analyze.

``` bash 
if __name__ == "__main__":
    root_dir = '/path/to/your/directory'
    main(root_dir)
```

- Run the script:
``` bash 
python main.py
```
## Output

- `file_records.csv:` A CSV file containing metadata for each file and folder.
- `summary.csv: `A CSV file containing a summary of the results grouped by file extension.
- `total_size_by_extension.png:` A bar chart visualization of the total size by file extension.