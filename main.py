'''
Simple Web Scraper
Grabs the Top selected Headlines
Dec 23, 2022
Edward Naidoo 
'''

# Modules
from colorama import Fore, Style
from bs4 import BeautifulSoup
import requests
import datetime

# Variables
time = datetime.datetime.now()
i = 1 # Counter

# Site1
webpage = requests.get('https://www.supplychaindive.com/', )
soup = BeautifulSoup(webpage.text, "html5lib")

hl1 = soup.find("a", attrs={"class": "analytics t-dash-top-1"})
hl2 = soup.find("a", attrs={"class": "analytics t-dash-top-2"})
hl3 = soup.find("a", attrs={"class": "analytics t-dash-top-3"})
hl4 = soup.find("a", attrs={"class": "analytics t-dash-top-4"})
hl5 = soup.find("a", attrs={"class": "analytics t-dash-top-5"})

headlines = [hl1, hl2, hl3, hl4, hl5]

# Checks Status Code
if webpage:
    print(f"{Fore.GREEN}{Style.BRIGHT}Accessed site!\n")
else:
    print(f"{Fore.RED}Something went wrong!\n")

# Display
print(f"{Style.BRIGHT}{Fore.WHITE}Top Stories\n")

for h in headlines:
    print(f"{Fore.MAGENTA} {i}. {h.text}")
    i += 1

print(f"{Fore.LIGHTCYAN_EX}Pulled from 'https://www.supplychaindive.com/'\n\n{time}")