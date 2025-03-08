# iterators vs generators
#iterators 
lst = (1,2,3,4,5)
i = iter(lst)
# print(i)# this will be printing the memory location of the values
'''the below syntex will be printing the values one by one '''
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print('\n')

#Generator
def squre(n):
    for i in range(n):
        yield i**2
for i in squre(4):
    print(i)



