n = int(input())
if n>=1 and n<=150:
    sumiss=0
    for i in range(0,n):
        if n>=10:
            if i==0:  
                sumiss+=(n-i)*(10**i)
            else:
                sumiss+=(n-i)*(10**i+1)
        else:
            sumiss+=(n-i)*(10**i)
    print(sumiss)