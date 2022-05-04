with open("My Clippings.txt", mode='r', encoding="utf-8") as f: 
    txt = f.read()
    list = txt.split("==========")




books = {}
for i, quote in enumerate(list[1:-1]): 
    if len(list) > 3:
        quote = list[i]
        parse = quote.split("\n")
        title = parse[1] 
        if title not in books:
            books[title] = 1
        else:
            books[title] = books[title] + 1

        data = parse[2]
        highlight = parse[4]
        print(highlight)