from smtpd import DebuggingServer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

driver = webdriver.Chrome()
#dirve open
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
#사이트를 오픈한다
elem = driver.find_element(By.NAME, "q")
#검색창을 찾는다
elem.send_keys("사과")
#이름을 입력하고 검색한다
elem.send_keys(Keys.RETURN)
#검색된갓ㅂ에 엔터를 눌러준다.
SCROLL_PAUSE_TIME = 2
#스크롤을 내리고 시간을 기다린다.

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".OuJzKb.Bqq24e").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    image.click()
    time.sleep(3)
    imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, str(count) + "test.jpg")
    count +=1
driver.close()

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()