def mults(x, y):
    ### prints the sum of all the multiples of x and y
    sum = 0
    for i in range(1, 1000):
        if (i % x) == 0 or (i % y) == 0:
            sum += i
    
    print(sum)
        

mults(3,5)
 
