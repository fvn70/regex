def compare(reg, inp):
    if not reg:
        return True
    if not inp:
        return False
    if reg == '.' or reg == inp:
        return True
    else:
        return False


reg, inp = input().split('|')
print(compare(reg, inp))
