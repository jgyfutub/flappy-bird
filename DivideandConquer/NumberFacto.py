def numberFactor(n):
    if n is (0,1,2):
        return 1
    elif n==3:
        return 2
    else:
        subP1=numberFactor(n-1)
        subP2=numberFactor(n-3)
        subP3=numberFactor(n-4)
        return subP1+subP2+subP3