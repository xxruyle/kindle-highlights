# kindle-highlights
 Gathers and parses all higlighted text from kindle My Clippings.txt file and places them into individual text files based on book title

# Setup Guide
1) Place your My Clippings.txt file in the project directory
2) Add the directory you want the parsed clippings file to be exported to in main.py -> `kindlehighl.parsetext(path)`
3) Run `main.py` 

```powershell
usage: main.py [-h] [-i] [-e] [-b book] [--titles]

Get the quotes of My Clippings.txt

optional arguments:
  -h, --help   show this help message and exit
  -i, --ind    Get the highlights of a singular book
  -e, --excel  Convert a singular book of highlights to excel. Requires book argument
  -b book      Name of singular book you want to parse
  --titles     Get the titles
```

3) For -b book, use --titles list as the book argument 

# Parsing every book highlight 
```
python main.py 
```

# Parsing to a singular txt file
```
python main.py -i -b "title"
```

# Parsing to excel
 parse to excel
```
python main.py -e -b "title" 
```


# Future To Do
- [X] Remove bad characters when creating text file name
- [X] Better formatting for quotes
- [X] Pandas support
- [X] Custom file directory 
- [X] Command line arguments
- [ ] Refactoring