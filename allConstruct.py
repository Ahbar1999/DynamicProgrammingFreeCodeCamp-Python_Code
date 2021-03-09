#allConstruct implementation

#Brute Force
def allConstructUnopt(targetStr, wordBank):
    if(targetStr == ''):
        return [[]]

    result =  []

    for word in wordBank:

        if(targetStr.find(word) == 0):
            suffix = targetStr[len(word):]
            #ways to construct suffix
            suffixWays = allConstruct(suffix, wordBank)
            #ways to construct current word of the iteration
            targetWays = list(map((lambda lstr: [word, *lstr]), suffixWays))

            #add it to our final collection
            for ls in targetWays:
                result.append(ls)

    return result

# print(allConstruct('purple', ['purp', 'p', 'ur',
#     'le', 'purpl']))
# print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def',
#     'abcd', 'ef', 'c']))
# print(allConstruct('skateboard', ['bo', 'rd',
#     'ate', 't', 'ska', 'sk', 'boar']))
# #Slow test for memoization
# print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa',
#     'aaa', 'aaaaaa', 'aaaaaaa']))


#Memoized Implementation
def allConstructOpt(targetStr, wordBank):

    memo = {}
    def allConstruct(targetStr, wordBank, memo):

        if(targetStr in memo):
            return memo[targetStr]
        if(targetStr == ''):
            return [[]]

        result =  []

        for word in wordBank:

            if(targetStr.find(word) == 0):
                suffix = targetStr[len(word):]
                #ways to construct suffix
                suffixWays = allConstruct(suffix, wordBank, memo)
                #ways to construct current word of the iteration
                targetWays = list(map((lambda lstr: [word, *lstr]), suffixWays))

                #add it to our final collection
                for ls in targetWays:
                    result.append(ls)

        memo[targetStr] = result
        return result

    return allConstruct(targetStr, wordBank, memo)


print(allConstructOpt('purple', ['purp', 'p', 'ur',
    'le', 'purpl']))
print(allConstructOpt('abcdef', ['ab', 'abc', 'cd', 'def',
    'abcd', 'ef', 'c']))
print(allConstructOpt('skateboard', ['bo', 'rd',
    'ate', 't', 'ska', 'sk', 'boar']))
#Slow test for memoization
print(allConstructOpt('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa',
    'aaa', 'aaaaaa', 'aaaaaaa']))


#THIS PROBLEM HAS SOME SPECIAL RESULTS FOR TIME AND SPACE COMPLEXITY,
#I HAVE WRITTEN DOWN IN MY NOTEBOOK THE RESULTS AND THE EXPLANATION

