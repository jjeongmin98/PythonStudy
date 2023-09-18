import requests
from bs4 import BeautifulSoup
import openpyxl

page_num=0
product_list = list()
def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook
    excel_sheet = excel_file.active
    excel_sheet.column_dimension['A'].width = 100
    excel_sheet.column_dimension['B'].width = 100

    if sheetname !='':
        excel_sheet.title = sheetname
    
    for item in listdata:
        excel_sheet.appen(item)
    excel_file.save(filename)
    excel_file.close()

if page_num == 0 :
    res = requests.get("https://davelee-fun.github.io/")
else:
    res = requests.get("https://davelee-fun.github.io/"+str(1+page_num))

soup = BeautifulSoup(res.content, "html.parser")

items = soup.select("div.h-100 card-group")
for item in items:
    product_name = item.select_one('div.card h4.card-text')
    product_data = item.select_one('div.wrapfooter span.post-date')
    product_info = [product_name.get_text().strip(), product_data.get_text()]
    product_list.append(product_info)

excel_file = openpyxl.load_workbook('tmp.xlsx')
