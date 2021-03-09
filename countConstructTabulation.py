#countConstruct() Tabulation implementation

def countConstruct(targetStr, wordBank):

    table = [0]*(len(targetStr)+1)
    table[0] = 1

    for i in range(len(table)):
        for word in wordBank:
            if(targetStr[i:i+len(word)] == word):
                if(i+len(word) <= len(targetStr)):
                    table[i+len(word)] += table[i]

    return table[len(targetStr)]

print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #2
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])); #1
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #0
print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 't', 'o'])) #4
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefff',
                        ['e',
                        'ee',
                        'eee',
                        'eeee',
                        'eeeeee',
                        'eeeeeeee'])) #0
