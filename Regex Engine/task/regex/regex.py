def comp_beg(reg, inp):
    if not reg:
        return True
    if not inp:
        return False
    if reg[0] not in '.' and reg[0] != inp[0]:
        return False
    return comp_beg(reg[1:], inp[1:])


def compare(reg, inp):
    if not reg:
        return True
    while inp:
        if comp_beg(reg, inp):
            return True
        else:
            inp = inp[1:]
    return False


reg, inp = input().split('|')
print(compare(reg, inp))
