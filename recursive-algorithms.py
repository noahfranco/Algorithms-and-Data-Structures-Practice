def recursive_n(n):
    print(n)
    # base case 
    if n == 0:
        return
    # recursive case ~~ just like a call back function  
    recursive_n(n / 2)