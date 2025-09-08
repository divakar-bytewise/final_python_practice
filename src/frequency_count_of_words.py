def freq_count(str1):
    lst1=str1.split()
    dict1={}

    for i in lst1:
        if i not in dict1.keys():
            dict1[i]=0
        dict1[i]=dict1[i]+1
    return dict1

str1=input("Enter your thoughts: ")
result=freq_count(str1)
for i,j in result.items():
    print(f"{i}:{j}")