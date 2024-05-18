from html.parser import HTMLParser;
from urllib import parse

class linkFinder(HTMLParser):

    def __init__(self, *, convert_charrefs: bool = True, baseUrl, pageUrl) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.baseUrl = baseUrl
        self.pageUrl = pageUrl
        self.links = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for(attribute, value) in attrs:
                if attribute == "href":
                    url = parse.urljoin(self.baseUrl, value)
                    self.links.add(url)
        # return super().handle_starttag(tag, attrs)

    def pageLinks(self):
        return self.links

    def error(self, message):
        pass

# finder = linkFinder()
# finder.feed('<html>')