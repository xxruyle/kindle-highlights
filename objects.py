class readclippings():
    def __init__(self):
        self.encoding = "utf-8"

    def readtxt(self):
        with open("My Clippings.txt", mode='r', encoding="utf-8") as f: 
            txtlist = f.read().split("==========")
            return txtlist

class parsetext(readclippings):
    def __init__(self):
        super().__init__()
        self.dictionary = {}
        self.parse = self.readtxt()

    def createdict(self):
        for i, quote in enumerate(self.parse[2:-1]):
            quote = self.parse[i]
            sectioned = quote.split("\n")
            title = sectioned[1] 
            if title not in self.dictionary:
                self.dictionary[title] = []


            data = sectioned[2]
            highlight = sectioned[4]
            agg_quote = data + "\n" + highlight + "\n\n"
            self.dictionary[title].append(agg_quote)

        title_names = list(self.dictionary) 
            
        return title_names

    def getquotes(self):
        titles = self.createdict()
        print(titles[10])
        with open(f"{titles[10]}.txt", "w", encoding="utf-8") as f:
            for quote in self.dictionary[titles[10]]:
                f.write(quote)
    

p1 = parsetext()

print(p1.getquotes())
