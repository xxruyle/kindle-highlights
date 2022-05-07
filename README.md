# kindle-highlights
 Gathers and parses all higlighted text from kindle My Clippings.txt file and places them into individual text files based on book title

# Setup Guide
1) Place your My Clippings.txt file in the project directory
2) Run `main.py` 

```powershell
usage: main.py [-h] [--ind] [--no-ind] [--excel] [--no-excel] [--b book] [--titles] [--no-titles] path

Get the quotes of My Clippings.txt

positional arguments:
  path         Path of where you want the outputted .txt files

optional arguments:
  -h, --help   show this help message and exit
  --ind        Get the highlights of a singular book
  --no-ind     Get the highlights of every book
  --excel      Convert a singular book of highlights to excel. Requires book argument
  --no-excel   Disables converting to excel
  --b book     Name of singular book you want to parse
  --titles     Get the titles
  --no-titles  Don't get the titles
```

3) For -b book, use --titles list as the book argument 

# Future To Do
- [X] Remove bad characters when creating text file name
- [X] Better formatting for quotes
- [X] Pandas support
- [ ] Custom file directory 
- [ ] Command line arguments
- [ ] Refactoring