
#fib(n) implementation through tabulation in place of recursion

def fib(n):

    #One way for initialising an array/list of specific size
    # table = [None]*(n+1)

    # for i in range(len(table)):
    #     if(i == 1):
    #         table[i] = 1
    #         continue
    #     table[i] = 0


    #Another pythonic way
    table = [0]*(n+1)
    table[1] = 1

    for i in range(len(table)):

        #For until we hit the last two cells
        if(i <= len(table) -3):
            table[i+1] += table[i]
            table[i+2] += table[i]
            continue
        #fill the last cell
        table[i+1] += table[i]
        break

    #print(table)
    return table[n]

#Time: O(n)
#Space: O(n)

print(fib(6));
print(fib(8));
print(fib(50));
