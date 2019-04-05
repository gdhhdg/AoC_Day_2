import re
import functools
f = open('./input.txt', 'r')
text = f.read()
f.close()
splitText = re.sub(r'[\n]', ', ', text )
textArray = splitText.split(', ')
textArrayStripped = [x for x in textArray if x] #clear 'falsy'
#testArray = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee','ababab','aabcde']
countDict = {'two': 0, 'three': 0}
def findMults(array):
    for x in array:
        print(x)
        twocount = False
        threecount = False
        for y in x:
            count = x.count(y)
            print(threecount)
            if count is 2:
                if twocount is True:
                    pass
                else:
                    countDict['two'] += 1
                    twocount = True
            if count is 3:
                if threecount is False:
                    countDict['three'] += 1
                    threecount = True
#findMults(textArray)
#print(countDict['two']*countDict['three'])

## part 2

#testArray = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

def arrayDiff(array): # returns ids with 1 difference
    compareArray = []
    for first in array:
        for next in array:
            count = 0
            for i in range(len(next)):
                if first[i] == next[i]:
                    count += 1
            if count == len(first) - 1:
                compareArray.append(first)
                compareArray.append(next)
    return compareArray

print(arrayDiff(list(textArrayStripped)))

