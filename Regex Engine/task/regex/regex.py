def comp_beg(reg, inp):
    if not reg:
        return True
    if not inp:
        return False
    if reg[0] == '\\':
        return reg[1] == inp[0]
    if len(reg) > 1 and reg[1] in '?+*':
        if '?' in reg and reg[1] == '?':
            if reg[0] == inp[0] and reg[2] == inp[1]:
                return True
            return comp_beg(reg[2:], inp)
        elif ('*' in reg or '+' in reg) and reg[1] in '*+':
            if reg[0] == inp[0]:
                return True
            if reg[0] == '.':
                if len(reg) < 3 or reg[2] == inp[0]:
                    return True
                return comp_beg(reg, inp[1:])
            return comp_beg(reg[2:], inp) if '*' in reg else False
    if reg[0] not in '.\\' and reg[0] != inp[0]:
        return False
    return comp_beg(reg[1:], inp[1:])


def compare(reg, inp):
    if not reg:
        return True
    reg0 = reg.lstrip('^').rstrip('$')
    f_beg = reg and reg[0] == '^'
    f_end = reg and reg[-1] == '$'
    f_mult = '*' in reg or '+' in reg
    f_last = reg0[-1] in '.*+'
    is_beg, is_end = True, True
    if f_beg:
        is_beg = comp_beg(reg0, inp)
    if f_end:
        if '\\' in reg0 and reg0[-1] in '.?*+' and reg0[-2] == '\\':
            return reg0[-1] == inp[-1]
        inp0 = inp if f_mult else inp[-len(reg0):]
        if f_last:
            is_end = reg0[-1] == '.' or reg0[-2] in ['.', inp0[-1]]
        else:
            is_end = reg0[-1] == inp0[-1]
        is_end = is_end and comp_beg(reg0, inp0)
    if f_beg or f_end:
        return is_beg and is_end
    while inp:
        if comp_beg(reg, inp):
            return True
        else:
            inp = inp[1:]
    return False


reg, inp = input().split('|')
print(compare(reg, inp))
