s = "PAYPALSTRING"


def shambles(b, s):
    m = ["" for i in range(b)]
    x = ""
    m[0] = s[0]
    up_down = True
    for i in range(1, len(s)):
        c = i % b
        if up_down:
            if c == 0:
                up_down = False
            m[c] = m[c] + s[i]
        else:
            if c == 0:
                up_down = True
                m[b-c-1] = m[b-c-1] + s[i]
    x = "".join(m)
    print(m)
    return x


some = shambles(3, s)
print(some)
