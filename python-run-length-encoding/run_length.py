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

def encode(seq):
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




def decode(seq):
    pass