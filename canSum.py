#canSum problem

#THIS ONE WORKS
def canSum(targetSum, numbers):
    memo = {}

    def helper(targetSum, numbers, memo):
        if targetSum in memo:
            return memo[targetSum]
        if(targetSum == 0):
            return True
        if(targetSum < 0):
            return False

        for num in numbers:
            remainder = targetSum - num
            if(helper(remainder, numbers, memo) == True):
                #return values that are not base cases can be stored
                memo[targetSum] = True
                return True

        #return values that are not base cases can be stored
        memo[targetSum] = False
        return False

    return helper(targetSum, numbers, memo)


#THIS ONE DOESNT WORK AND I DONT KNOW WHY
def canSum1(targetSum, numbers, memo = {}):
        if targetSum in memo:
            return memo[targetSum]
        if(targetSum == 0):
            return True
        if(targetSum < 0):
            return False

        for num in numbers:
            remainder = targetSum - num
            if(canSum(remainder, numbers, memo) == True):
                #return values that are not base cases can be stored
                memo[targetSum] = True
                return True

        #return values that are not base cases can be stored
        memo[targetSum] = False
        return False




print(canSum(7, [2, 3])) #true
print(canSum(7, [5, 3, 4, 7])) #true
print(canSum(7, [2, 4])) #false
print(canSum(8, [2, 3, 5])) #true
print(canSum(300, [7, 14])) #false



