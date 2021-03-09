
#canConstruct implementation
def canConstructUnOpt(targetStr, wordBank):
    if (targetStr == ''):
        return True

    for word in wordBank:
        if(targetStr.find(word) == 0):
            suffix = targetStr[len(word):]
            if(canConstruct(suffix, wordBank) == True):
                return True

    return False;

#Brute Force
#Time: O(n^m*m)
#Space: O(m*m) = o(m^2)

#print(canConstructUnOpt('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])); #true
#print(canConstructUnOpt('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #false

#Memoized Implementation

def canConstructOpt(targetStr, wordBank):

    memo = {}
    def canConstruct(targetStr, wordBank, memo):

        if(targetStr in memo):
            return memo[targetStr]

        if (targetStr == ''):
            return True

        for word in wordBank:
            if(targetStr.find(word) == 0):
                suffix = targetStr[len(word):]
                if(canConstruct(suffix, wordBank, memo) == True):
                    memo[targetStr] = True
                    return True

        memo[targetStr] = False
        return False;

    return canConstruct(targetStr, wordBank, memo)

#Memoized
#Time: O(n*m*m) = O(n*m^2)
#Space: O(m^2)


print(canConstructOpt('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])); #true
print(canConstructOpt('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #false
#memoization test case
print(canConstructOpt('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefff',
                        ['e',
                        'ee',
                        'eee',
                        'eeee',
                        'eeeeee',
                        'eeeeeeee'])) #false
