import requests
from bs4 import BeautifulSoup
import re
import json

'''
#ชื่อเว็ปที่จะสกัด หน้าที่ 1
ryoii ="https://www.ryoiireview.com/review/?page=1&tag_group=รถไฟฟ้า"

#ส่งคำข้อ
page = requests.get(ryoii)
#ใช้ BeautifulSoup ในการสกัดข้อมูล
soup = BeautifulSoup(page.content, "html.parser")

#สกัดข้อมูล
restaurant1 = soup.find_all(class_ = "caption")
#print(restaurant)


with open("restaurant1.txt", "w", ) as f: 
    for title in restaurant1:
        f.write(str(restaurant1) + "\t")
'''
#ชื่อเว็ปที่จะสกัด หน้าที่ 2
ryoii ="https://www.ryoiireview.com/review/?page=2&tag_group=รถไฟฟ้า"

#ส่งคำข้อ
page = requests.get(ryoii)
#ใช้ BeautifulSoup ในการสกัดข้อมูล
soup = BeautifulSoup(page.content, "html.parser")

#สกัดข้อมูล
restaurant2 = soup.find_all(class_ = "caption")
print(restaurant2)


with open("restaurant2.csv", "w", ) as f: 
    for title in restaurant2:
        f.write(str(restaurant2) + "\t")

'''
#ชื่อเว็ปที่จะสกัด หน้าที่ 3
ryoii ="https://www.ryoiireview.com/review/?page=3&tag_group=รถไฟฟ้า"

#ส่งคำข้อ
page = requests.get(ryoii)
#ใช้ BeautifulSoup ในการสกัดข้อมูล
soup = BeautifulSoup(page.content, "html.parser")

#สกัดข้อมูล
restaurant3 = soup.find_all(class_ = "caption")
#print(restaurant)


with open("restaurant3.txt", "w", ) as f: 
    for title in restaurant3:
        f.write(str(restaurant3) + "\t")

#ชื่อเว็ปที่จะสกัด หน้าที่ 4
ryoii ="https://www.ryoiireview.com/review/?page=4&tag_group=รถไฟฟ้า"

#ส่งคำข้อ
page = requests.get(ryoii)
#ใช้ BeautifulSoup ในการสกัดข้อมูล
soup = BeautifulSoup(page.content, "html.parser")

#สกัดข้อมูล
restaurant4 = soup.find_all(class_ = "caption")
#print(restaurant)


with open("restaurant4.txt", "w", ) as f: 
    for title in restaurant4:
        f.write(str(restaurant4) + "\t")



#ชื่อเว็ปที่จะสกัด หน้าที่ 5
ryoii ="https://www.ryoiireview.com/review/?page=5&tag_group=รถไฟฟ้า"

#ส่งคำข้อ
page = requests.get(ryoii)
#ใช้ BeautifulSoup ในการสกัดข้อมูล
soup = BeautifulSoup(page.content, "html.parser")

#สกัดข้อมูล
restaurant5 = soup.find_all(class_ = "caption")
#print(restaurant)


with open("restaurant5.txt", "w", ) as f: 
    for title in restaurant5:
        f.write(str(restaurant5) + "\t")
'''