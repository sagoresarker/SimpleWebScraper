from cgitb import text
from requests_html import HTMLSession
import json


class Scraper():
    def scrapdata(self, tag):
        url = f"https://quotes.toscrape.com/tag/{tag}"
        s = HTMLSession()
        r = s.get(url)


        qlist = []
        quotes = r.html.find('div.quote')

        for q in quotes:
            item = {
                'text': q.find('span.text', first=True).text.strip(),
                'Author': q.find('small.author', first=True).text.strip()
            }

            qlist.append(item)

        return qlist

quotes = Scraper()
quotes.scrapdata('life')