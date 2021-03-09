
#countConstruct implementation

#Brute Force
def countConstructUnOPt(targetStr, wordBank):
    if(targetStr == ''):
        return 1

    totalCount = 0;

    for word in wordBank:
        if(targetStr.find(word) == 0):
            suffix = targetStr[len(word):]
            numWaysForRest = countConstruct(suffix, wordBank)
            totalCount += numWaysForRest

    return totalCount


# print(countConstruct('purple', ['purp', 'p', 'ur',
#     'le', 'purpl'])) #2
# print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def',
#     'abcd'])) #1
# print(countConstruct('skateboard', ['bo', 'rd', 'ate',
#     't', 'ska', 'sk', 'boar'])) #0
# print(countConstruct('enterapotentpot', ['a', 'p',
#     'ent', 'enter', 'ot', 'o', 't'])) #4
# print(canConstructOpt('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefff',
#                         ['e',
#                         'ee',
#                         'eee',
#                         'eeee',
#                         'eeeeee',
#                         'eeeeeeee'])) #0, too slow for just brute force


#Memoized
def countConstructOpt(targetStr, wordBank):

    memo = {}
    def countConstruct(targetStr, wordBank, memo):

        if(targetStr in memo):
            return memo[targetStr]

        if(targetStr == ''):
            return 1

        totalCount = 0;

        for word in wordBank:
            if(targetStr.find(word) == 0):
                suffix = targetStr[len(word):]
                numWaysForRest = countConstruct(suffix, wordBank, memo)
                totalCount += numWaysForRest

        memo[targetStr] = totalCount
        return totalCount

    return countConstruct(targetStr, wordBank, memo)


print(countConstructOpt('purple', ['purp', 'p', 'ur',
    'le', 'purpl'])) #2
print(countConstructOpt('abcdef', ['ab', 'abc', 'cd', 'def',
    'abcd'])) #1
print(countConstructOpt('skateboard', ['bo', 'rd', 'ate',
    't', 'ska', 'sk', 'boar'])) #0
print(countConstructOpt('enterapotentpot', ['a', 'p',
    'ent', 'enter', 'ot', 'o', 't'])) #4
print(countConstructOpt('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefff',
                        ['e',
                        'ee',
                        'eee',
                        'eeee',
                        'eeeeee',
                        'eeeeeeee'])) #0, too slow for just brute force
