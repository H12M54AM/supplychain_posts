'''
Simple Web Scraper
Grabs the Latest Headlines
Dec 27, 2022
Edward Naidoo 
'''

# Modules
from colorama import Fore, Style
from bs4 import BeautifulSoup
import requests
import datetime

# Variables
time = datetime.datetime.now()

# Site1
url = "https://www.supplychaindive.com/"
webpage = requests.get(url)

soup = BeautifulSoup(webpage.text, "html5lib")

i = 1 # Counter

# Checks Status Code ---------------------
if webpage:
    print(f"{Fore.GREEN}{Style.BRIGHT}Accessed site!\n")
else:
    print(f"{Fore.RED}Something went wrong!\n")

# Display --------------------------------

# Shows Latest Stories
for div in soup.find_all("div", attrs={"class": "medium-6 columns "}):

    feed_title = div.h3.a.text
    feed_description = div.p.text
    secondary_label = div.span.text
    topic = div.a.text
    
    print(f"\n{Fore.LIGHTBLUE_EX}{feed_title}")
    print(f"{Fore.LIGHTBLUE_EX}{feed_description}")
    print(f"{Fore.LIGHTBLUE_EX}{secondary_label}")
    print(f"{Fore.LIGHTBLUE_EX}{topic}\n")


print(f"{Fore.LIGHTCYAN_EX}Pulled from '{url}'\n\n{Fore.LIGHTMAGENTA_EX}{time}")