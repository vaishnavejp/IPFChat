import easyocr

reader = easyocr.Reader(["en"], gpu=False)

result = reader.readtext("./images/ipf3.png", paragraph=True, detail=0, batch_size=20)

fd = open("./textFiles/imgContent.txt", "w", encoding="utf-8")
content = ""

for i in result:
    content += i
    content += "\n"

fd.writelines(content)
