worddict = {}
with open("sometext.txt") as file:
    for line in file:
        words = line.strip('').split()
        for word in words:
            if(word in worddict):
                worddict[word] = worddict[word]+1
            else:
                worddict[word] = 1

print(worddict)