#iterables vs iterators
#iterables 
lst = [1,2,3,4,5,6]

# for i in lst:
#     print(i)

#iterators
l = iter(lst)
print(next(l))
print('')

'''if i will again print the next l statment then it will not print the stuff '''

for i in l:
    print(i)
    