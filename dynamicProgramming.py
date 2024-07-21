#%%
def fib_bottom_up(n):
    global count 
    list1 = [0,1]
    for i in range(2,n+1):
        count += 1 
        sum = list1[i-1] + list1[i-2] 
        list1.append(sum) 
    return list1,count
count = 0  
fib_bottom_up(7) 


def fib_up_bottom(n):
    global memo 
    if memo[n] is not None:
        return memo[n] 
    if n == 0 or n == 1:
        return n 
    
    memo[n] = memo[n-1] + memo[n-2] 
    return memo[n]
fib_up_bottom(6)