def remove_duplicates(lst1):
    unique=[]
    for n in lst1:
        if n not in unique:
            unique.append(n)

    return unique

li=list(map(int,input("Enter the list values : ").split()))
result=remove_duplicates(li)
print("The unique values are = ",result)