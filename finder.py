from bs4 import BeautifulSoup as bs
import requests as r
from tkinter import *

def find(item_name: str) -> str:

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

        if columns != []:
            item = columns[1].text.strip().lower()
            desc = columns[2].text.strip()

            items[item] = desc
    
    for item in items:
        if item_name in item:
            return str(item) + ":\n" + str(items[item])
    return "Nothing found"


window = Tk()
window.title("Abyss Item Finder")
window.geometry('600x200')
window.config(bg="#565656")
window.resizable(False, False)

prompt = Label(window, text = "Enter Item", font=("Arial Bold", 20), bg="#565656", fg = "#B6D0E2")
prompt.place(relx = .5, rely = .05, anchor = 'center')

name_entry = Entry(window, font=("Arial Bold", 15), fg="#B6D0E2", bg="#565656", width = 16)
name_entry.place(relx = .5, rely = .2, anchor = 'center')

description = Text(window, width = 40, fg = "#FF00FF", bg = "#000000", height = 4, wrap=WORD, font=("Arial Bold", 15))
description.place(relx = .5, rely = .7, anchor = 'center')

def get_input():
    description.delete('1.0', 'end')
    description.insert('1.0', find(name_entry.get()))

submit_button = Button(window, 
                text="Submit", 
                fg = "#FF00FF", 
                highlightbackground="#565656", 
                bg = "#565656", 
                height = 1, 
                width = 8, 
                borderwidth = 2, 
                relief="solid",
                command=get_input)

submit_button.place(relx = .5, rely = .35, anchor = 'center')

window.mainloop()
