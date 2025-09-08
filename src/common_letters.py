def common_letters(str1,str2):
    s1=set(str1)
    s2=set(str2)
    lower_s1={item.lower() for item in s1}
    lower_s2={item.lower() for item in s2}
    res=lower_s1 & lower_s2
    return res

a=input("Enter the first string value: ")
b=input("Enter the second string value: ")

final_output=common_letters(a,b)
print("The common letter in the both string's are :", final_output)