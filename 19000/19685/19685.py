s,f=map(int,input().split()) 
for i in range(s,f+1): 
    if str(i)==''.join(reversed(str(i))): 
        print("Palindrome!") 
    else: 
        print(i)