def list_to_dict(num1,str1):
    result=dict(zip(num1,str1))
    return result

num1=list(map(int,input("Enter the numeric values").split()))
str1=list(map(str,input("Enter the string values").split()))

final_op=list_to_dict(num1,str1)
print(final_op)

def dict_to_tuple(final_op):
    for i in final_op.items():
        print(i)

dict_to_tuple(final_op)