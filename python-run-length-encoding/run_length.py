import re

#Overload of encode for second possibility
def encode(seq, test):
    character = ""
    result = ""
    counter = 1
    stringlist = []
    for n in seq:
        if character != n:
            character = n
            stringlist.append((character, 1))
        else:
            stringlist[-1] = (stringlist[-1][0], stringlist[-1][1] + 1)
    for n in stringlist:
        if n[1] > 1:
            result += str(n[1])
        result += n[0]
    return result

def encode(seq, test, test2):
    character = ""
    result = ""
    counter = 1
    for n in range(len(seq)):
        if n < len(seq) - 1:
            if seq[n] == seq[n + 1]:
                counter += 1
            else:
                if counter > 1:
                    result += str(counter)
                result += seq[n]
                counter = 1
        else:
            if counter > 1:
                result += str(counter)
            result += seq[n]
            counter = 1
    return result

def encode(seq):
    index = 0
    result = ""
    while len(seq) != index:
        character = seq[index]
        match = re.findall(f"{character}+|$", seq[index:])[0]
        counter = len(match)
        if counter > 1:
            result += str(counter)
        result += character
        index += counter
    return result

def decode(seq):
    declist = re.findall("([0-9]*)?(.)", seq)
    result = ""
    for n in declist:
        if n[0] == '':
            result += n[1]
        else:
            result += (int(n[0]) * n[1])
    return result
