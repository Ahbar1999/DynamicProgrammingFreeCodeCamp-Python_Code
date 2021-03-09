#allConstruct() Tabulation implementation

#this function will return a 2D array of all the possible solutions
def allConstruct(targetStr, wordBank):

    table = [None]*(len(targetStr)+1)
    table = list(map((lambda i: []), table)) #creating 2D array/ inserting a new array into every index replacing None
    table[0] = [[]]

    for i in range(len(table)):
        for word in wordBank:
            if(targetStr[i: i+len(word)] == word):
                #Replace each subarray/solution of current table cell and add word to each and return  a list
                newCombo = list(map((lambda subarray: [*subarray, word]), table[i]))
                if(i+len(word) <= len(targetStr)):
                    for ls in newCombo:
                        table[i+len(word)].append(ls)
                    #table[i+len(word)].append(newCombo)

    return table[len(targetStr)]

#Time~ O(n^m)
#Space~ O(n^m)

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']));
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(allConstruct('aaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaaaa']))
#Since this program runs in exponential time therefore any test case with a large input wont execute quicklys
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefff',
                        ['e',
                        'ee',
                        'eee',
                        'eeee',
                        'eeeeee',
                        'eeeeeeee'])) #
