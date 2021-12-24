import requests
from bs4 import BeautifulSoup

from numpy import *
from pandas import *

url = "https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%" \
      "83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B8%D0%" \
      "BD%D0%B4%D0%B5%D0%BA%D1%81_%D1%81%D1%87%D0%B0%D1%81%D1%82%D1%8C%D1%8F"

page = requests.get(url)

text = page.text
soup = BeautifulSoup(text, "lxml")

table = soup.find_all('table')[2]  # поиск нужной таблицы
# print(table)
countries = []
topics = []
hpi = []
happy = []
av_life = []
track = []

for t in table.find_all('th'):
    topics.append(t.text)

for t in range(len(topics)):
    topics[t] = topics[t].replace('\n', '')

# print(topics)
for t in table.find_all('td', align="left"):  # добавление названий стран в список
    countries.append(t.text)

for i in range(len(countries)):  # удаление знаков перед названиями
    countries[i] = countries[i].replace(u'\xa0', u' ')

c = 0
for t in table.find_all('td'):  # добавление названий стран в список
    if c <= 2:
        if c == 2:
            hpi.append(t.text)
    elif (c - 2) % 6 == 0:
        hpi.append(t.text)
    c += 1

c = 0
for t in table.find_all('td'):  # добавление названий стран в список
    if c <= 3:
        if c == 3:
            happy.append(t.text)
    elif (c - 3) % 6 == 0:
        happy.append(t.text)
    c += 1

c = 0
for t in table.find_all('td'):  # добавление названий стран в список
    if c <= 4:
        if c == 4:
            av_life.append(t.text)
    elif (c - 4) % 6 == 0:
        av_life.append(t.text)
    c += 1

c = 0
for t in table.find_all('td'):  # добавление названий стран в список
    if c <= 5:
        if c == 5:
            track.append(t.text)
    elif (c - 5) % 6 == 0:
        track.append(t.text)
    c += 1

for t in range(len(track)):
    track[t] = track[t].replace('\n', '')

mest = []

for i in range(len(countries)):
    mest.append(i + 1)

arr = column_stack((mest, countries, hpi, happy, av_life, track))
arr = row_stack((topics,arr))

# print(arr)

pandas.set_option('display.max_columns', None)
df = pandas.DataFrame(data=arr)

print(df)
