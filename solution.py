def getseq(letter, size):
    if (size >= 2):
        return letter + ""  + letter
    elif size == 1:
        return "" + letter
    print(size)
    return ""


def get(a, b, c):

    ret = ""
    if (a >= b and a >= c):
        prev = "c"
    if (c >= b and c >= a):
        prev = "a"
    if (b >= a and b >= c):
        prev = "a"
    while (True):
        printed = False
        if prev == "a":
            if (b <= 0 and c <= 0): break
            tempb = getseq("b", b)
            ret += tempb
            b -= len(tempb)
            if (len(tempb) > 0):
                printed = True
                prev = "b"
            tempc = getseq("c", c)
            ret += tempc
            c -= len(tempc)
            if (len(tempc) > 0):
                prev = "c"
        elif prev == "b":
            if (a <= 0 and c <= 0): break
            tempa = getseq("a", a)
            ret += tempa
            a -= len(tempa)
            if (len(tempa) > 0):
                prev = "a"
            tempc = getseq("c", c)
            ret += tempc
            c -= len(tempc)
            if (len(tempc) > 0):
                prev = "c"
        elif prev == "c":
            if (a <= 0 and b <= 0): break
            tempa = getseq("a", a)
            ret += tempa
            a -= len(tempa)
            if (len(tempa) > 0):
                prev = "a"
            tempb = getseq("b", b)
            ret += tempb
            b -= len(tempb)
            if (len(tempb) > 0):
                printed = True
                prev = "b"

    return ret


print(get(0, 5, 5))
