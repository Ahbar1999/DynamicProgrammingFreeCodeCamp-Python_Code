#canConstruct() Tabulation implementation
def canConstruct(targetStr, wordBank):

    table = [False]*(len(targetStr)+1)
    # Fill the 0th index of the table with True
    # 0th index stands for '' (empty string) which can always be generated
    table[0] = True

    for i in range(len(targetStr)):
        if(table[i] == True):
            for word in wordBank:
                # Here we are checking if the word in the bank matches the targetString - (substring generated up to that index)
                # So that we can add to it further
                if(targetStr[i:(i+len(word))] == word):
                    # Checking for boundary conditions
                    if(i+len(word) <= len(targetStr)):
                        table[i + len(word)] = True

    return table[len(targetStr)]

#Time: O(m*n*m) // the last 'm' is for slicing/copying of the array
#Space: O(m)

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])); #true
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #false
print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #true
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefff',
                        ['e',
                        'ee',
                        'eee',
                        'eeee',
                        'eeeeee',
                        'eeeeeeee'])) #false
