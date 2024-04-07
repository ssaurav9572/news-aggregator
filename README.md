# news-aggregator


The Python code provided demonstrates how to create a simple news aggregator that fetches and displays news articles from the Hacker News website (news.ycombinator.com). Here's a breakdown of the key components and functionalities of the code:

# Requirements:

The code requires Python 3.x installed on the system.
It also relies on the Beautiful Soup 4 and Requests libraries, which can be installed via pip.

# Setting Up the Project:

The project structure is initialized by creating a directory named 'news_aggregator' and a Python file named 'aggregator.py' within it.

# Fetching Web Page Content:

The Requests library is used to send an HTTP GET request to the Hacker News website (https://news.ycombinator.com) to fetch the web page content.
If the request is successful (status code 200), the HTML content of the page is stored for further processing.

# Parsing HTML Content with Beautiful Soup:

Beautiful Soup is employed to parse the HTML content of the web page and create a BeautifulSoup object, allowing easy navigation and extraction of data.
The 'prettify()' method is used to display the well-formatted HTML content.

# Extracting News Articles:

The news articles are identified within the HTML structure by locating 'tr' elements with the class 'athing'.
For each article, the title and URL are extracted and printed to the console.

# Displaying the Aggregated News:

The main function encapsulates the logic for fetching, parsing, and displaying news articles.
The aggregated news articles are printed in a readable format, with each article's title and URL displayed on separate lines.
