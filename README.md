# kindle-highlights
 Gathers and parses all higlighted text from kindle My Clippings.txt file and places them into individual text files based on book title

# Setup Guide
1) Place your My Clippings.txt file in the project directory
2) Run `main.py` 

```powershell
usage: main.py [-h] [--ind] [--excel] [--b book] [--titles] path

Get the quotes of My Clippings.txt

positional arguments:
  path        Path of where you want the outputted .txt files

optional arguments:
  -h, --help  show this help message and exit
  --ind       Get the highlights of a singular book
  --excel     Convert a singular book of highlights to excel. Requires book argument
  --b book    Name of singular book you want to parse
  --titles    Get the titles
```

3) For -b book, use --titles list as the book argument 

# Future To Do
- [X] Remove bad characters when creating text file name
- [X] Better formatting for quotes
- [X] Pandas support
- [X] Custom file directory 
- [X] Command line arguments
- [ ] Refactoring