from bs4 import BeautifulSoup
import requests

fd = open("./textFiles/extractURL.txt", "r", encoding="utf-8")
linksRead = fd.read().splitlines()

links = []
for i in linksRead:
    links.append(i)


for i in links:
    files = requests.get(i)

    content = ""

    soup = BeautifulSoup(files.content, "lxml")
    tags = soup.find("article", class_="doc")

    for i in tags:
        content += i.text

    content += "------------------------------"
    fd = open("./textFiles/finalContent.txt", "a", encoding="utf-8")
    fd.writelines(content)
