strg = ['flower', 'flow', 'flight']
prefix = strg[0]

for s in strg:
    i = 0
    while i < len(s) and i < len(prefix) and prefix[i] == s[i]:
        i += 1
    prefix = prefix[:i]



print(prefix)


options = ['dog', 'racecar', 'car']
prefix = options[0]
for o in options:
    i = 0
    while i< len(o) and i < len(prefix) and prefix[i] == o[i]:
        i+=1


    prefix = prefix[:i]
    if i == 0:
        break

print(prefix)