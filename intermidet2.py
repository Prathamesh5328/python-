#map function
#some sort of ways to write the code
'''def even_odd(num):
    if num% 2 == 0 :
      return("the number is even")
    else:
       return("the number is odd ")

even_odd(11)'''


def even_odd(num):
    if num% 2 == 0 :
      return("the number {} is even  ").format(num)
    else:
       return("the number {} is odd  ").format(num)

lst = [1,2,3,4,5,6,7,8,9,0,12,34,65,78,97,109,54,76,87,89,]

x = list(map(even_odd,lst))
print(x)

'''this function is used to apply certen function on a iterrable
  in this above case the even_odd function is the function which we had appplyed 
   on the lst iterable '''




    