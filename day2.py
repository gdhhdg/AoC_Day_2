import re
import functools
f = open('./input.txt', 'r')
text = f.read()
f.close()
splitText = re.sub(r'[\n]', ', ', text )
textArray = splitText.split(', ')
#textArray = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee','ababab','aabcde']
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
findMults(textArray)
print(countDict['two']*countDict['three'])

## part 2

