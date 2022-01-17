import requests
from bs4 import BeautifulSoup
import json

url = "https://www.nytimes.com/crosswords/game/mini"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'lxml')

data = {}
data['clues']=[]
data['clues1']=[]

section = soup.find('section', attrs={"class": "Layout-clueLists--10_Xl"})

div = section.find_all('div', attrs={"class": "ClueList-wrapper--3m-kd"})
first_div = div[0]

first_title = first_div.find('h3', attrs={"class": "ClueList-title--1-3oW"}).text

first_list = first_div.find('ol', attrs={"class": "ClueList-list--2dD5-"})

number = first_list.find_all('span', attrs={"class": "Clue-label--2IdMY"})

list = first_list.find_all('span', attrs={"class": "Clue-text--3lZl7"})
#for i in range(0 , 5):
    #a = list[i].text
    #b = number[i].text

    #data['group'].append({
    #"string": a,
    #"number": b,
    #"group": first_title
    #})

div = section.find_all('div', attrs={"class": "ClueList-wrapper--3m-kd"})
second_div = div[1]

second_title = second_div.find('h3', attrs={"class": "ClueList-title--1-3oW"}).text

second_list = second_div.find('ol', attrs={"class": "ClueList-list--2dD5-"})

number1 = second_list.find_all('span', attrs={"class": "Clue-label--2IdMY"})

list1 = second_list.find_all('span', attrs={"class": "Clue-text--3lZl7"})
#for j in range(0 , 5):
    #x = list1[j].text
    #y = number1[j].text

    #data['group'].append({
    #"string": x,
    #"number": y,
    #"group": second_title
    #})

def listeler():
    for i in range(5):
        a = list[i].text
        b = number[i].text
        x = list1[i].text
        y = number1[i].text

        data['clues'].append({
            "string": a,
            "number": b,
            "group": first_title
        })

        data['clues1'].append({
            "string": x,
            "number": y,
            "group": second_title
        })
listeler();

print(json.dumps(data))

dosya = open("json.json", "w")
dosya.write(str(data))
dosya.close()
