# Add the path to the file that containes the final scraped content
# EXAMPLE - fd = open("./textFiles/finalContent.txt", "r", encoding="utf-8")
fd = open("<YOUR FILE PATH>", "r", encoding="utf-8")

linksRead = fd.readlines()

# Add path to final optimized file
# EXAMPLE - fd2 = open("./textFiles/optimised.txt", "a", encoding="utf-8")
fd2 = open("<YOUR FILE PATH>", "a", encoding="utf-8")

for i in linksRead:
    if i != "\n":
        fd2.write(i)
