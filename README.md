# API Changelog Generator

This project is a tool to extract API changes (added, deleted, and deprecated APIs) from HTML files containing API documentation diffs and generate a structured changelog in a CSV format.

## Project Structure

```
.
├── main.py                 # Main entry point to execute the program
├── changelog
│   ├── __init__.py         # Marks the changelog directory as a Python package
│   ├── file_manager.py     # Manages file I/O, including listing HTML files and reading file names
│   ├── html_parser.py      # Handles HTML parsing logic for extracting data
│   ├── date_parser.py      # Handles filename date extraction logic
│   ├── csv_writer.py       # Handles CSV writing logic
└── HTML output files       # Directory where HTML files are stored
```

## Features

- **HTML File Parsing**: Extracts information from HTML files about API changes including newly added, deleted, and deprecated APIs.
- **Flexible Date Parsing**: Handles filenames containing dates in formats such as `YYYY-MM` or `YYYY-MM-DD`.
- **CSV Export**: Generates a CSV file with structured data for easy analysis.
  
## Installation

To use the API Changelog Generator, you'll need Python 3.7 or higher. Follow the steps below to set it up:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/api-changelog-generator.git
   cd api-changelog-generator
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Step 1: Prepare HTML Files

Place your HTML files containing the API diff data in the `HTML output files` directory. Each HTML file should follow a naming convention like:

```
Diff-YYYY-MM-DD-api-docs.yaml-YYYY-MM-DD-api-docs.yaml.html
```

For example: `Diff-2020-11-19-api-docs.yaml-2020-11-27-api-docs.yaml.html`.

### Step 2: Run the Script

Run the `main.py` script to generate the CSV changelog:

```bash
python main.py
```

The script will read the HTML files, extract the relevant API change data, and generate a CSV file named `changelog.csv` in the root directory.

### Step 3: Review the Changelog

The generated `changelog.csv` will contain the following columns:

- `Diff from`: The start date of the diff (extracted from the filename).
- `To`: The end date of the diff (extracted from the filename).
- `APIs Added`: The number of APIs added in this diff.
- `Method`: The HTTP method (GET, POST, etc.) for the API.
- `URI`: The endpoint URI for the API.
- `Description`: A description of the change.
- `APIs Deleted`: The number of APIs deleted in this diff.
- `Notes`: Additional notes.

## Dependencies

The project relies on the following Python libraries:

- `BeautifulSoup4`: For parsing the HTML files.
- `csv`: For writing the changelog data into CSV format.
- `os`, `pathlib`: For handling file system operations.
- `re`: For regular expressions.

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Requirements
Install beautifulsoup4 with the help of `requirements.txt`;

```plaintext
pip install -r requirements.txt
```

or install it manually using
```cmd
pip install beautifulsoup4
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Feedback

If you have any feedback, please reach out to us at darshanparbadiya@gmail.com

## Features

- Sending bulk messages
- Sending same or different message choice
- No need to save contacts before sending messages
- Sending images with or without text.
- Cross platform

## 🚀 About Me

I'm a full stack developer...
