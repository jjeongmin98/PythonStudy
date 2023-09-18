import requests
from bs4 import BeautifulSoup
import openpyxl

prod
page_num=0
if page_num == 0 :
    res = requests.get("https://davelee-fun.github.io/")
else:
    res = requests.get("https://davelee-fun.github.io/"+str(1+page_num))

soup = BeautifulSoup(res.content, "html.parser")
data = soup.select('div.card')
for item in data:
    product_name = item.select_one('div.card-body h4.card-text')
    product_data = item.select_one('div.wrapfooter span.post-date')

    

