from bs4 import BeautifulSoup
import requests

# Add the file in which all the extracted URLs are stored
# EXAMPLE - fd = open("./textFiles/extractURL.txt", "r", encoding="utf-8")
fd = open("<YOUR FILE PATH>", "r", encoding="utf-8") 

linksRead = fd.read().splitlines()

links = []
for i in linksRead:
    links.append(i)


for i in links:
    files = requests.get(i)

    content = ""

    soup = BeautifulSoup(files.content, "lxml")

    # Add the html tag you want to scrape along with its corresponding class name
    # EXAMPLE - tags = soup.find("article", class_="doc")
    tags = soup.find("<HTML TAG>", class_="<CLASS NAME>")

    for i in tags:
        content += i.text

    content += "------------------------------"

    # Store the content scraped in desired file 
    # Example - fd = open("./textFiles/finalContent.txt", "a", encoding="utf-8")
    fd = open("<YOUR FILE PATH>", "a", encoding="utf-8")
    
    fd.writelines(content)
