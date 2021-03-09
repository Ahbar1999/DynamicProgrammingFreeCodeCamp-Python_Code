#gridTraveler tabulation

def gridTraveler(m, n):
    #creating a 2D array with default values filled,
    #here the default value is 0 becuase we have a counting problem at hand
    # table = [[0]*(m+1)]*(n+1) <= This doesn't work!!!!!!!!!!!!!
    table = [0]*(m+1)
    table = list(map((lambda index: [0]*(n+1)), table))
    #Seed the trivial values/Equivalent of creating base cases in recursion implementaion
        table[1][1] = 1
    #Traverse through thre grid
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            #Checking for boundaries
            if(i+1 <= m):
                table[i+1][j] += current
            if(j+1 <= n):
                table[i][j+1] += current

    return table[m][n]

print(gridTraveler(1, 1))   #1
print(gridTraveler(2, 3))   #3
print(gridTraveler(3, 2))   #3
print(gridTraveler(3, 3))   #6
print(gridTraveler(18, 18)) #233606220


#Time: O(m*n)
#Space: O(m*n)
