from bs4 import BeautifulSoup

class HtmlParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_data(self):
        """Extracts API changes from an HTML file."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        
        categories = ["What's New", "What's Deleted", "What's Deprecated"]
        data_new, data_deleted, data_deprecated = [], [], []

        for category in categories:
            section = soup.find("h2", string=category)
            if section:
                ol = section.find_next("ol")
                if ol:
                    for li in ol.find_all("li"):
                        method_tag = li.find("span")
                        method = method_tag.text.strip() if method_tag else ""
                        
                        if category == "What's Deleted":
                            endpoint_tag = li.find("del") if category == "What's Deleted" else method_tag.find_next_sibling(string=True)
                            endpoint = endpoint_tag.text.strip() if endpoint_tag else ""
                        else:
                            endpoint = method_tag.find_next_sibling(string=True).strip() if method_tag and method_tag.find_next_sibling(string=True) else "Unknown"
                        
                        description_tag = method_tag.find_next_sibling("span") if method_tag else None
                        description = description_tag.text.strip() if description_tag else ""
                        
                        if category == "What's New":
                            data_new.append([method, endpoint, description])
                        elif category == "What's Deleted":
                            data_deleted.append([method, endpoint, description])
                        else:
                            data_deprecated.append([method, endpoint, description])

        return data_new, data_deleted, data_deprecated
