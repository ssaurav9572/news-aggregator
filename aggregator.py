import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

if response.status_code == 200:
    page_content = response.text
    soup = BeautifulSoup(page_content, "html.parser")
    headline_links = soup.find_all("span", class_="titleline")

    for headline_link in headline_links:
        title = headline_link.text.strip()
        article_url = headline_link.find("a")["href"]
        print(f"Title: {title}")
        print(f"URL: {article_url}")
        print()  # Add a newline for better readability between articles
else:
    print(f"Failed to fetch content from {url}")


