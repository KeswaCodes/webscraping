
import requests
from bs4 import BeautifulSoup

URL = "https://za.indeed.com/jobs?q=software+engineering"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())