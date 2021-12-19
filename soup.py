
table = {
    1: ">",
    2: "<",
    3: "+",
    4: "-",
    5: ".",
    6: ",",
    7: "[",
    8: "]",
}

reverse_table = {
    ">": 1,
    "<": 2,
    "+": 3,
    "-": 4,
    ".": 5,
    ",": 6,
    "[": 7,
    "]": 8,
}

def soup_to_bf(program):
    lines = program.split('\n')
    compiled = ""
    for line in lines:
        occurrences = line.count("soup")
        if occurrences >= 1 and occurrences <= 8:
            compiled += table[occurrences]
    return compiled

def bf_to_soup(bf):
    soup = ""
    for char in bf:
        if char in reverse_table:
            soup += " ".join(reverse_table[char] * ["soup"])
            soup += "\n"
    return soup
