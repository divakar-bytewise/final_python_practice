def finding_missing_num(lst1):
    n=lst1[-1]
    final=set(range(1,n+1))
    given=set(lst1)
    res=sorted(list(final-given))
    return res

a=list(map(int,input("Enter the list of numbers").split()))
result=finding_missing_num(a)
print("The missing number is : ",result)