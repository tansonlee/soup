RAM_SIZE = 100

def closing_bracket_index(program, start):
    count = 1
    for i in range(start, len(program)):
        if program[i] == '[':
            count += 1
        elif program[i] == ']':
            count -= 1
        if count == 0:
            return i
    return -1

def interpret(program):
    ram = [0] * RAM_SIZE
    pc = 0

    ip = 0
    stack = []

    while True:
        if ip >= len(program):
            break
        if program[ip] == '>':
            pc += 1
        elif program[ip] == '<':
            pc -= 1
        elif program[ip] == '+':
            ram[pc] += 1
        elif program[ip] == '-':
            ram[pc] -= 1
        elif program[ip] == '.':
            print(chr(ram[pc]), end='')
        elif program[ip] == ',':
            ram[pc] = ord(input())
        elif program[ip] == '[':
            if ram[pc]:
                stack.append(ip)
            else:
                count = 0;
                while True:
                    ip += 1
                    if not program[ip]:
                        break
                    if program[ip] == "[":
                        count += 1
                    elif program[ip] == "]":
                        if count:
                            count -= 1
                        else:
                            break
        elif program[ip] == ']':
            ip = stack.pop() - 1;
        ip += 1

        
