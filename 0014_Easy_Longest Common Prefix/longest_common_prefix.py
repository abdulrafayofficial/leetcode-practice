strg = ['flower', 'flow', 'flight']
prefix = strg[0]

for s in strg:
    i = 0
    while i < len(s) and i < len(prefix) and prefix[i] == s[i]:
        i += 1
    prefix = prefix[:i]


