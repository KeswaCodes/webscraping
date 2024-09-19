# pip3 install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# the URL of the login page
login_url = "https://www.scrapingcourse.com/login"

# the payload with your login credentials
payload = {
    "email": "zkeswa023@student.wethinkcode.co.za",
    "password": "thisismypassword1",
}

# send the POST request to login
response = requests.post(login_url, data=payload)


# if the request went Ok, you should get a 200 status
print(f"Status code: {response.status_code}")

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# find the page title
page_title = soup.title.string

# print the result page title
print(f"Page title: {page_title}")
