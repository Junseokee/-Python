from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request
import os
from tqdm import tqdm
import time

keyword = input('검색어 입력 : ')
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' +keyword

driver = webdriver.Chrome('C:/Users/sec/Desktop/Junseok/Untitled Folder/chromedriver.exe')
driver.get(url)
time.sleep(2)


for i in range(10):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1.5)    

html_source=driver.page_source
soup=bs(html_source, 'html.parser')

img_list = soup.find('div', class_='photo_group _listGrid').find_all('img')
img_url = soup.find('div', class_='photo_group _listGrid').find_all('img')[0]['src']
print(len(img_list))

# 저장폴더 생성
fDir = 'C:/Users/sec/Desktop/Junseok/Untitled Folder/'
fName = os.listdir(fDir)
# 저장폴더 존재여부 확인
fName_dir = keyword+'0'
cnt = 0
while True:
    if fName_dir not in fName: # 새로 생성한 폴더가 현재 저장 위치에 있으면
        os.makedirs(fDir+fName_dir) # 없ㅇ면 현재 이름으로 생성
        break #생성후 while문 빠져나감
    cnt+=1
    fName_dir=keyword+str(cnt) # 새로운 폴더명 생성
    
print(fDir+fName_dir,'로폴더 생성')

time.sleep(5)
cnt = 0
for img_url in tqdm(img_list, desc = '저장중...'):
    tmp_name = 'C:/Users/sec/Desktop/Junseok/Untitled Folder/'+ fName_dir + '/' + keyword + str(cnt) + '.jpg'
    try:
        urllib.request.urlretrieve(img_url['src'],tmp_name)
    except:
        urllib.request.urlretrieve(img_url['data-src'],tmp_name)
    cnt+=1
    time.sleep(0.1)

driver.close()
