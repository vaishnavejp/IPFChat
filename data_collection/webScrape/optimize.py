fd = open("./textFiles/finalContent.txt", "r", encoding="utf-8")

linksRead = fd.readlines()

fd2 = open("./textFiles/optimised.txt", "a", encoding="utf-8")

for i in linksRead:
    if i != "\n":
        fd2.write(i)
