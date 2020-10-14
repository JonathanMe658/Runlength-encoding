import re

def encode(seq):
    character = ""
    result = ""
    counter = 1
    for n in range(len(seq)):
        if n < len(seq) -1:
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

def decode(seq):
    result = ""
    splitted_string = re.findall("(\d*)?(.)", seq)
    for i in splitted_string:
        if i[0] == '':
            result += i[1]
        else:
            result += (int(i[0]) * i[1])
    return result
