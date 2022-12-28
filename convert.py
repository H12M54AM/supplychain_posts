"""
Simple Web Scraper
Converting Scraped data to JSON
Dec 27, 2022
Edward Naidoo
"""
import random
import requests
from bs4 import BeautifulSoup
import json
import datetime
from colorama import Fore, Style

# Variables
time = datetime.datetime.now()
random = random.randint(1, 100)
random_string = str(random)
url = "https://evmagazine.com/sustainability"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')

# Gets data
title = soup.find("div", attrs={"class": "Title_TitleInner__3XUSc"})
print(f"\n{Fore.WHITE}{Style.BRIGHT}{title.text}\n")

for data in soup.find_all("div", attrs={"class":"Card_CardWrapper__jRxGZ"}):
    temp = data.text

    # Convert the data to JSON format
    json_data = json.dumps(temp)
    print(f"{Fore.LIGHTCYAN_EX}{temp}")
    print()

print(f"{Fore.LIGHTMAGENTA_EX}Pulled from {url}\n\nat {time}")

# Save the JSON data to a file
with open(f'./exports/data-{random_string}.json', 'w') as f:
    f.write(json_data)
