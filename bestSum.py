
#bestSum implementation

#Unoptimised
def bestSumUnOPt(targetSum, numbers):
    if(targetSum == 0): return []
    if(targetSum < 0): return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        #If we find a solution
        if(remainderCombination != None):
            combination = [*remainderCombination, num]
            #If the combination is shorter than the current shortest
            if(shortestCombination == None or len(combination) < len(shortestCombination)):
                shortestCombination = combination

    return shortestCombination

#m = target sum
#n = numbers.lenghth


#Brute force
#time: O(n^m*m)
#space: O(m*m) = O(m^2) we have to store in worst case an m lenght list for every call




#Test Cases                      #Answers
#print(bestSum(7, [5, 3, 4, 7]))  #[7]
#print(bestSum(8, [2, 3, 5]))     #[3, 5]
#print(bestSum(8, [1, 4, 5]))     #[4, 4]
#print(bestSum(100, [1, 2, 5, 25])) #[25, 25, 25, 25]


#Memoized
def bestSumOpt(targetSum, numbers):
    #Keeping a memo as always
    memo = {}

    def bestSum(targetSum, numbers, memo):
        if targetSum in memo:
            return memo[targetSum]
        if(targetSum == 0): return []
        if(targetSum < 0): return None

        shortestCombination = None

        for num in numbers:
            remainder = targetSum - num
            remainderCombination = bestSum(remainder, numbers, memo)
            #If we find a solution
            if(remainderCombination != None):
                combination = [*remainderCombination, num]
                #If the combination is shorter than the current shortest
                if(shortestCombination == None or len(combination) < len(shortestCombination)):
                    shortestCombination = combination

        #only returning once also,
        #we just wanna keep track of optimal sums so here we'll store optimal solution only
        memo[targetSum] =  shortestCombination
        return shortestCombination

    return bestSum(targetSum, numbers, memo)

#Memoized
#time: O(n*m*m)
#space: O(m^2)


#Test Cases                      #Answers
print(bestSumOpt(7, [5, 3, 4, 7]))  #[7]
print(bestSumOpt(8, [2, 3, 5]))     #[3, 5]
print(bestSumOpt(8, [1, 4, 5]))     #[4, 4]
print(bestSumOpt(100, [1, 2, 5, 25])) #[25, 25, 25, 25]
