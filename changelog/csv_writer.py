import csv

class CsvWriter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write_data(self, data: list):
        """Writes data to the CSV file."""
        with open(self.file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["Diff from", "To", "APIs Added", "Method", "URI", "Description", "APIs Deleted", "Method", "URI", "Description", "Notes"])

            for row in data:
                writer.writerow(row)
