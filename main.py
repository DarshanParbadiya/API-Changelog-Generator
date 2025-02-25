from changelog.file_manager import FileManager
from changelog.html_parser import HtmlParser
from changelog.date_parser import DateParser
from changelog.csv_writer import CsvWriter

def main():
    # Step 1: Initialize classes
    file_manager = FileManager("HTML output files")
    date_parser = DateParser()
    csv_writer = CsvWriter("changelog.csv")

    # Step 2: List HTML files
    try:
        html_files = file_manager.list_html_files()
    except FileNotFoundError as e:
        print(e)
        return

    # Step 3: Prepare data for CSV
    all_data = []

    for file_path in html_files:
        file_name = file_path.name
        date_start, date_end = date_parser.parse_dates_from_filename(file_name)

        html_parser = HtmlParser(str(file_path))
        data_new, data_deleted, data_deprecated = html_parser.extract_data()

        # Collect CSV rows
        diff_file = file_name
        all_data.append([date_start, date_end, f"{len(data_new)} APIs added", "", "", "", f"{len(data_deleted)} APIs deleted", "", "", "", diff_file])

        max_length = max(len(data_new), len(data_deleted), len(data_deprecated))
        for i in range(max_length):
            new_api = data_new[i] if i < len(data_new) else ["", "", ""]
            deleted_api = data_deleted[i] if i < len(data_deleted) else ["", "", ""]
            deprecated_api = data_deprecated[i] if i < len(data_deprecated) else ["", "", ""]
            all_data.append(["", "", "", *new_api, "", *deleted_api, "", *deprecated_api])

    # Step 4: Write to CSV
    csv_writer.write_data(all_data)
    print(f"CSV file 'changelog.csv' has been created successfully.")

if __name__ == "__main__":
    main()
