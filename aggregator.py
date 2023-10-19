#Requirements
#Python 3.x installed on your system.
#Beautiful Soup 4 and the Requests library installed. You can install them using pip:

pip install beautifulsoup4 requests

#Setting Up the Project

#First, create a new directory for your project and navigate to it. Here, you can do this with your terminal:

mkdir news_aggregator
cd news_aggregator

#Next, create a Python file to write your code.terminal:

touch aggregator.py

#Fetching Web Page Content
import requests

url = "https://news.ycombinator.com"
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    page_content = response.text
    print(page_content)
else:
    print(f"Failed to fetch content from {url}")

#Parsing HTML Content with Beautiful Soup

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_content, "html.parser")
print(soup.prettify())

#Extracting News Articles

#After inspecting the HTML structure of Hacker News, we can see that each news article is contained within a ‘tr’ element with a class ‘athing’. Let’s extract all the news articles using Beautiful Soup’s find_all method:

articles = soup.find_all("tr", class_="athing")

for article in articles:
    title = article.find("a", class_="titlelink").text
    url = article.find("a", class_="titlelink")["href"]
    print(f"{title}\n{url}\n")

#Displaying the Aggregated News

#Finally, let’s put it all together and display the aggregated news in a more readable format.

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    if response.status_code == 200:
            page_content = response.text
            soup = BeautifulSoup(page_content, "html.parser")
            articles = soup.find_all("tr", class_="athing")
            for article in articles:
                title = article.find("a", class_="titlelink").text
                url = article.find("a", class_="titlelink")["href"]
                print(f"{title}\n{url}\n")
        else:
            print(f"Failed to fetch content from {url}")
    if __name__ == "__main__":
        main()
