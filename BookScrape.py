from bs4 import BeautifulSoup
import requests

url="https://books.toscrape.com"
response=requests.get(url)

print(response.status_code)

soup=BeautifulSoup(response.text,"html.parser")
books=soup.find_all("article",class_="product_pod")


for item in books:
    title=item.h3.a["title"]
    price=item.find("p",class_="price_color").text
    print(title, price)
