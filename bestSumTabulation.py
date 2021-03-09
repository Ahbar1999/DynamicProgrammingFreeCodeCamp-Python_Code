#bestSum() tabulation implementation

def bestSum(targetSum, numbers):
    table = [None]*(targetSum+1)
    table[0] = []

    for i in range(len(table)):
        if(table[i] != None):
            for num in numbers:
                if(i + num < len(table)):
                    newCombo = [*table[i], num]
                    #To check for bestSum
                    #also add the value if table[i+num] == None due to which len(i+num) returns undefined since it could be undefined
                    if(table[i+num] == None or (len(newCombo) < len(table[i+num]))):
                        table[i + num] = newCombo

    return table[targetSum]

#Complexities are same as howSumTabulation
#Time: O(m*n*n) = O(m*n^2)
#Space: O(m^2)

#Test cases:
print(bestSum(7, [5, 3, 4, 7]))  #[7]
print(bestSum(8, [2, 3, 5]))     #[3, 5]
print(bestSum(8, [1, 4, 5]))     #[4, 4]
print(bestSum(100, [25, 1, 5, 2]))     #[25, 25, 25, 25]
