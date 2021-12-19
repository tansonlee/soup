
from interpreter import interpret
from soup import soup_to_bf, bf_to_soup
from sys import stdin, argv


# python3 main.py
# python3 main.py -help
# python3 main.py -compile-soup
# python3 main.py -generate-soup

def usage():
    print("""
    Usage:
        python3 main.py                 [Interprets a soup program]
        python3 main.py -help           [Prints this message]
        python3 main.py -compile-soup   [Compiles a soup program into bf]
        python3 main.py -generate-soup  [Generates a soup program from bf]
    """)

def main():
    # python3 main.py -help
    if len(argv) == 2 and argv[1] == '-help':
        usage()
        return

    data = ""
    for line in stdin:
        data += line

    # python3 main.py
    if len(argv) == 1:
        bf = soup_to_bf(data)
        interpret(bf)
        return

    # python3 main.py -compile-soup
    if len(argv) == 2 and argv[1] == '-compile-soup':
        bf = soup_to_bf(data)
        print(bf)
        return

    # python3 main.py -generate-soup
    if len(argv) == 2 and argv[1] == '-generate-soup':
        soup = bf_to_soup(data)
        print(soup)
        return

    usage()


    

main()
