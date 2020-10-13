def encode(seq):
    character = ""
    counter = 1
    result = ""
    for n in seq:
        if n == character:
            counter += 1
        else:
            if character:
            result += str(counter) + n
            counter = 1
            character = n
    return result


def decode(seq):
    pass