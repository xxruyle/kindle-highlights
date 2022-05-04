class readclippings():
    def __init__(self):
        self.encoding = "utf-8"

    def readtxt(self):
        with open("My Clippings.txt", mode='r', encoding="utf-8") as f: 
            txtlist = f.read().split("==========")
            return txtlist

class parsetext(readclippings):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.dictionary = {}  # Stores the hashmap data structure for the quotes
        self.parse = self.readtxt()


    
    def badchar(self, string):  # Removes illegal filename characters 
        for c in '\/:*?"<>|':
            string = string.replace(c,'-')
        return string

    def cleanString(self, string):  # removes illegal unicode characters from track name
        list = []
        for letter in string:
            if letter.isalnum() or letter == ' ' or letter == '(' or letter == ')' or letter == "," or letter == ".":
                list.append(letter)
            else:
                list.append("")
        return ''.join(list)
    

    def createdict(self):
        for i, quote in enumerate(self.parse[2:-1]):
            quote = self.parse[i]
            sectioned = quote.split("\n")
            init_title = sectioned[1]

            # removing bad illegal file name characters
            init_title2 = self.badchar(init_title)  
            title = self.cleanString(init_title2)

            # Adding title to dictionary if it hasn't been added yet 
            if title not in self.dictionary:
                self.dictionary[title] = []


            agg_quote = sectioned[2] + "\n" + sectioned[4] + "\n\n"  # Making the date added and quote one string
            self.dictionary[title].append(agg_quote)  # adding the agg_quote to the dictionary

        title_names = list(self.dictionary) 
            
        return title_names

    def getquotes(self):
        titles = self.createdict()
        for t in titles[1:]:
            with open(f"{self.filepath}\\{t}.txt", "w", encoding="utf-8") as f:
                for quote in self.dictionary[t]:
                    f.write(quote)
    


