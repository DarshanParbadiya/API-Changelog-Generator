import os
from pathlib import Path

class FileManager:
    def __init__(self, directory: str):
        self.directory = Path(directory).resolve()

    def list_html_files(self):
        """Lists all HTML files in the specified directory."""
        if not self.directory.exists():
            raise FileNotFoundError(f"Directory {self.directory} does not exist.")
        
        html_files = [file for file in self.directory.glob("*.html")]
        return html_files
