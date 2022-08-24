from requests_html import HTMLSession
import re


class Scraper:
    def __init__(self) -> None:
        self.session = HTMLSession()
        self._title: str

    def extract(self, link: str) -> str:
        """
        Extract download URL from onlyfiles link
        Usage: Scraper().extract('urlhere')
        """
        r = self.session.get(link)
        scraped_info = r.html.find("div[onclick]")
        new = " ".join(map(str, scraped_info))

        result_of_pattern = re.findall(r"'([^']*)'", new)
        self._title = result_of_pattern[3]
        new_url = f"https://onlyfiles.io/{result_of_pattern[2]}"
        return new_url

    @property
    def title(self) -> str:
        """
        Extract song title from onlyfiles link
        Usage: Scraper().title
        """
        return self._title
