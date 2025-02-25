import re

class DateParser:
    @staticmethod
    def parse_dates_from_filename(filename: str):
        """Extracts the date range from the filename."""
        match = re.search(r'Diff-(\d{4}-\d{2})(?:-(\d{2}))?-api-docs.yaml-(\d{4}-\d{2})(?:-(\d{2}))?-api-docs.yaml', filename)
        
        if match:
            start_date = f"{match.group(1)}/{match.group(2) if match.group(2) else '01'}"  # Use '01' if day is missing
            end_date = f"{match.group(3)}/{match.group(4) if match.group(4) else '01'}"  # Use '01' if day is missing
            return start_date, end_date
        
        return "Unknown", "Unknown"
