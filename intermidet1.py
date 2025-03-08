#lambda functions 
'''lambda functions are use to minumise the code
   as compair to over reguler code syntrx'''

# a normal code
'''def double_the_number():
    x = 5
    y = 2
    double_num = x * y
    print(double_num)

double_the_number()'''



#example 2 using the lambda function in def fun

def fun(n):
    return lambda a : a * n
double = fun(2)
triple = fun(3)

print(double(5))
print(triple(5))
