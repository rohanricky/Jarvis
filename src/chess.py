'''
from splinter import Browser

with Browser() as browser:
    url = "https://www.chess.com/members/search?content_search%5Bphrase%5D=riikkii&content_search%5Bcountry%5D=69&content_search%5Btype%5D="
    browser.visit(url)
    var x=browser.find_by_xpath(div[contains(@class,user-rating)])
    print(x.value)
'''
from bs4 import BeautifulSoup
import requests
r=requests.get("https://www.chess.com/members/search?content_search%5Bphrase%5D=riikkii&content_search%5Bcountry%5D=69&content_search%5Btype%5D=")
soup = BeautifulSoup(r.text, 'html.parser')
x=soup.find("div",{"class":"user-rating"})
print(x.text)
