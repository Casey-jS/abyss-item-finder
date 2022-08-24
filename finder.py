from bs4 import BeautifulSoup as bs
import requests as r

class Finder:

    def __init__(self, app, desc):
        self.app = app
        self.desc = desc
    
    @property 
    def desc(self):
        return self.__desc
    
    @desc.setter
    def desc(self, input):
        self.__desc = input
    


    def find(self, item_name: str) -> str:

        # url of site with all items and descriptions
        url = "https://neonabyss.fandom.com/wiki/Items"

        # the html generated from the web request
        page = r.get(url)

        # the bs object that parses the page
        bs_page = bs(page.text, 'html.parser')

        # find the table of type wikitable
        table = bs_page.find('table', class_='wikitable mw-collapsible')

        # all items and descriptions
        items = {}

        # for each row in the table
        for row in table.tbody.find_all('tr'):

            # all columns in the row
            columns = row.find_all('td')
            item = columns[1].text.strip().lower()
            if columns != []:
                if item_name in item:
                    return str(item) + ":\n"

            if columns != []:
                item = columns[1].text.strip().lower()
                desc = columns[2].text.strip()

                items[item] = desc
        
        # Basic search
        for item in items:
            if item_name in item:
                return str(item) + ":\n" + str(items[item])
        return "Nothing found"


    











