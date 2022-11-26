# Import Modules
import requests
from bs4 import BeautifulSoup
import re
import json

# CONSTANTS
URL = "https://thegreatestbooks.org/?page="  # Example website for collecting the greatest books

# Choose how many pages you want to grab of the overall list
pages = 10
page_range = [n+1 for n in range(0, pages)]  # When opening another page to scrape data


def greatest_books(url, page):
    # Create variable that connects to the given URL
    response = requests.get(url=URL + str(page))
    # Variable for the raw page data
    raw_page_data = response.text
    # Create an object from BS4 Class
    soup = BeautifulSoup(raw_page_data, "html.parser")
    # Locate the elements in the HTMl specific to "h4"
    books = soup.select(".list-body h4")
    # Create a new list with the items and stripping the extras out
    book_list = [book.getText().strip("\n\t ") for book in books]
    # Split the list elements into their own lists split by ranking, title, author
    new_list = [re.split("\n. |  by | by ", n) for n in book_list]
    # Create a dictionary of the new list
    book_dict = {item[0]: {"Book Title": item[1], "Author": item[2]} for item in new_list}
    return book_dict


# Create a new list of all of the books
greatest_book_list = []
for n in page_range:
    greatest_book_list.append(greatest_books(url=URL, page=n))

# Dump the list to a json file
with open("book_list.json", "w") as file:
    json.dump(greatest_book_list, file)









