from bs4 import BeautifulSoup
import requests

# Add the url you want to crawl in textFiles/crawlURL.txt 
# EXAMPLE - fd = open("./textFiles/crawlURL.txt", "r", encoding="utf-8")

fd = open("<YOUR FILE PATH>", "r", encoding="utf-8")
linksRead = fd.read().splitlines()

links = []
for i in linksRead:
    links.append(i)

content = ""

# Manually add base path link
# EXAMPLE - c = "https://docs.ipfdev.co.uk/learn/RELEASE-IPF-2023.1.0/tutorials/"
c = "<YOUR BASE PATH>"

for i in links:
    file = requests.get(i)

    soup = BeautifulSoup(file.content, "lxml")
    tags = soup.find_all("li", class_="nav-item")

    for j in tags:
        x = j.find("a", class_="nav-link", href=True)
        if x is not None:
            content += x["href"] + "\n"

    content = content.splitlines()
    finalURLs = []
    for k in content:
        c = "https://docs.ipfdev.co.uk/learn/RELEASE-IPF-2023.1.0/tutorials/"
        c += k
        c += "\n"
        if c not in finalURLs:
            finalURLs.append(c)
    fd = open("./textFiles/extractURL.txt", "a", encoding="utf-8")
    fd.writelines(finalURLs)
