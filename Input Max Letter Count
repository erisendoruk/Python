input = raw_input('Enter a String ')
input.lower()
inputlist = list(input)
inputdict = dict()
for input in inputlist :
    inputdict[input] = inputdict.get(input,0) + 1
inputtupple = inputdict.items()
bigcount = None
for w, c in inputtupple :
    if bigcount is None or bigcount < c :
        bigcount = c
    else :
        continue
for w, c in inputtupple :
    if c == bigcount :
        print w, c