import kindlehighl
import argparse 
from os import getcwd

def main():
    p1 = kindlehighl.parsetext(getcwd())



    if args.ind:
        p1.ind_highlight(args.b)
    elif args.excel:
        p1.excel_highlight(args.b)
    elif args.titles:
        print(p1.createdict()[0])
    else:
        p1.all_highlights()
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the quotes of My Clippings.txt")
    parser.add_argument("-i", "--ind", action="store_true", help="Get the highlights of a singular book")
    parser.add_argument("-e", "--excel", action="store_true", help="Convert a singular book of highlights to excel. Requires book argument")
    parser.add_argument("-b", metavar = "book", type=str , help="Name of singular book you want to parse")
    parser.add_argument("--titles", action="store_true", help="Get the titles")

    parser.set_defaults(feature=False)
    args = parser.parse_args()
    main()