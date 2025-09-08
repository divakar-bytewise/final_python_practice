def updating_list(lst1):
    update=[]
    for i in lst1:
        if i>200:
            update.append(i * 10)
        else:
            update.append(i)
    return update

li=list(map(int,input("Enter the list of numbers : ").split()))
result=updating_list(li)
print(result)