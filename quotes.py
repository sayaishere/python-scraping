from bs4 import BeautifulSoup
import requests

url="https://quotes.toscrape.com/"
response=requests.get(url)

print(response.status_code)

response_text=response.text


bautifulSoup=BeautifulSoup(response_text,"html.parser")
quotes=bautifulSoup.find_all("div",class_="quote")
print(quotes)


for item in quotes:
    title=item.find("span",class_="text").text
    print(title)
