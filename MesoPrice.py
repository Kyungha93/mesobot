import requests
from bs4 import BeautifulSoup
import urllib.request as req
import time

now = time.localtime()
s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
print('[조회시각]')
print(s, "\n")

headers = {'User-Agent': 'Mozilla/5.0'}

# America Scania
URL = 'https://www.mmogo.com/Maplestory-m-America-scania/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# America Inosys
URL = 'https://www.mmogo.com/Maplestory-m-America-union/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 1 Scania
URL = 'https://www.mmogo.com/Maplestory-m-Asia-1-scania/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 1 Croa
URL = 'https://www.mmogo.com/Maplestory-m-Asia-1-cro/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 1 Zenith
URL = 'https://www.mmogo.com/Maplestory-m-Asia-1-zenith/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 1 Union
URL = 'https://www.mmogo.com/Maplestory-m-Asia-1-union/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 1 Luna
URL = 'https://www.mmogo.com/Maplestory-m-Asia-1-luna/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 1 Elysium
URL = 'https://www.mmogo.com/Maplestory-m-Asia-1-elysium/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 1 Inosys
URL = 'https://www.mmogo.com/Maplestory-m-Asia-1-inosys/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 2 Scania
URL = 'https://www.mmogo.com/Maplestory-m-Asia-2-scania/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 2 Croa
URL = 'https://www.mmogo.com/Maplestory-m-Asia-2-croa/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 2 Zenith
URL = 'https://www.mmogo.com/Maplestory-m-Asia-2-zenith/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 2 Union
URL = 'https://www.mmogo.com/Maplestory-m-Asia-2-union/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Asia 2 Luna
URL = 'https://www.mmogo.com/Maplestory-m-Asia-2-luna/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Europe Scania
URL = 'https://www.mmogo.com/Maplestory-m-Europe-scania/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text)
print('100M Mesos =', prices.strong.text, "\n")

# Japan Momiji
URL = 'https://www.mmogo.com/Maplestory-m-Jp3/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text, " 모미지")
print('100M Mesos =', prices.strong.text, "\n")

# Japan Anju
URL = 'https://www.mmogo.com/Maplestory-m-Jp2/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text, " 안즈")
print('100M Mesos =', prices.strong.text, "\n")

# Japan Karin
URL = 'https://www.mmogo.com/Maplestory-m-Jp1/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text, " 카린")
print('100M Mesos =', prices.strong.text, "\n")

# Japan Sakura
URL = 'https://www.mmogo.com/Maplestory-m-Jp4/Mesos.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
server = soup.find(class_= 'items-server')
prices = soup.find(class_='tian-price col-lg-6 col-xs-6')
print(server.em.text, " 사쿠라")
print('100M Mesos =', prices.strong.text, "\n")