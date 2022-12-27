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

# Site1
url = "https://www.supplychaindive.com/"
webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, "html5lib")
i = 1 # Counter

# Checks Status Code
if webpage:
    print(f"{Fore.GREEN}{Style.BRIGHT}Accessed site!\n")
else:
    print(f"{Fore.RED}Something went wrong!\n")

# Display

# Shows top 5 Stories
for section in soup.find_all("section", attrs={"class": "top-stories"}):

    if i > 5:
        break

    title = section.h2.text
    print(f"{Fore.WHITE}{Style.BRIGHT}{title}\n")   

    for article in soup.find_all("section", attrs={"class":"top-stories"}):
        temp = article.ol.text
        print(f"{Fore.MAGENTA}{temp}")
    

print(f"{Fore.LIGHTCYAN_EX}Pulled from 'https://www.supplychaindive.com/'\n\n{time}")