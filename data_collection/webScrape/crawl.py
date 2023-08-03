# Crawl through the website link and extract hyperlinks 

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

    # Inspect and find out what tags to scrape to collect urls
    # EXAMPLE - tags = soup.find_all("li", class_="nav-item")
    tags = soup.find_all("<HTML TAG>", class_="<CLASS NAME OF TAG>")

    for j in tags:
        # Add the hyperlinks and its corresponding class name
        # EXAMPLE - x = j.find("a", class_="nav-link", href=True)
        x = j.find("a", class_="<CLASS NAME OF ANCHOR TAG>", href=True)
        if x is not None:
            content += x["href"] + "\n"

    content = content.splitlines()
    finalURLs = []
    for k in content:
        # Manually add base path
        c = "https://docs.ipfdev.co.uk/learn/RELEASE-IPF-2023.1.0/tutorials/"
        c += k
        c += "\n"
        if c not in finalURLs:
            finalURLs.append(c)
    # Add the file path to store crawled URLS
    # EXAMPLE - fd = open("./textFiles/extractURL.txt", "a", encoding="utf-8")
    fd = open("<YOUR FILE PATH>", "r", encoding="utf-8")
    fd.writelines(finalURLs)
