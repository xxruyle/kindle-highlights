import re 

with open("My Clippings.txt", mode='r', encoding="utf-8") as f: 
    txt = f.read()
    list = txt.split("==========")


dic = {}
for i, quote in enumerate(list[2:-1]):
    quote = list[i]
    sectioned = quote.split("\n")
    init_title = sectioned[1]
    # removing bad illegal file name characters
    # Adding title to dictionary if it hasn't been added yet 
    if init_title not in dic:
        dic[init_title] = []
    
    data = sectioned[2]
    page = ' '.join(re.split("[\s|]+", data)[4:6]).upper()  # parses finds the page 
    date = ' '.join(re.split("[\s|]+", data)[10:16])
    dic[init_title].append(page)
    agg_quote = page + " | " + date + "\n" + sectioned[4] + "\n\n"  # Making the date added and quote one string
    dic[init_title].append(agg_quote)  # adding the agg_quote to the dictionary
    

    print(agg_quote)



