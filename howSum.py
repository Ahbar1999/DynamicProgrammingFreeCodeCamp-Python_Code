

#howSum without memoization
def howSumNoMemo(targetSum, numbers):
    if(targetSum == 0):
        return [] #return an empty list because the problem is virtually solved
    if(targetSum < 1):
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSumNoMemo(remainder, numbers)
        #If we found the solution then just return the solution and stop searching any further
        if(remainderResult != None):
            return [*remainderResult, num] #this will be done m times in the worst case scenario and will take m space in the worst case scenario

    #If we couldnt find a solution through the whole loop then just return null
    return None

#print(howSumNoMemo(7, [2, 3]))
#print(howSumNoMemo(7, [5, 3, 4, 7]))
#print(howSumNoMemo(7, [2, 4]))
#print(howSumNoMemo(8, [2, 3, 5]))
#print(howSumNoMemo(300, [7, 14]))

#Brute Force

#m = targetSum
#n  = numbers.len()

#time: O(n^m*m), the multiplied 'm' is for list copying
#space: O(m+m) = O(m)

#This is howSum with memo
def howSumWithMemo(targetSum, numbers):

    memo = {}
    def helper(targetSum, numbers, memo):
            if(targetSum in memo):
                return memo[targetSum]
            if(targetSum == 0):
                return [] #return an empty list because the problem is virtually solved
            if(targetSum < 1):
                return None

            for num in numbers:
                remainder = targetSum - num
                remainderResult = helper(remainder, numbers, memo)
                #If we found the solution then just return the solution and stop searching any further
                if(remainderResult != None):
                    memo[targetSum] = [*remainderResult, num]
                    return memo[targetSum]

            #If we couldnt find a solution through the whole loop then just return null
            memo[targetSum] = None
            return None

    return helper(targetSum, numbers, memo)


print(howSumWithMemo(7, [2, 3]))
print(howSumWithMemo(7, [5, 3, 4, 7]))
print(howSumWithMemo(7, [2, 4]))
print(howSumWithMemo(8, [2, 3, 5]))
print(howSumWithMemo(300, [7, 14]))

#time: O(n*m*m), the post multiplied 'm' is for list copying
#space: O(m*m), m keys, each key may have an array of m elements



