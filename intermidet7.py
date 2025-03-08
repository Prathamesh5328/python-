#list comprension 
lst = [ 1,2,3,4,5,6,7,8,9,10]
print([i*i for i in lst if i%2 == 0 ])#this will show the squres of only even numbers  of the lst
print([i*i for i in lst if i%2 == 1 ])#this will show the squres of only odd numbers of the lst
print([i*i for i in lst  ])#this will show the squres of all the numbers in the lst
print([i for i in lst  if  i%3 ==0  ])#this will show all the multiples of 3
'''the below stuff is out of teachings done for just quoricity'''
print('the table of 5 is ' + str(([i*5 for i in lst])))

#dict comprension
print({x:x**2 for x in lst if x%2 == 0})#this will show the squres of only even numbers  of the lst
print({x:x**2 for x in lst if x%2 == 1})#this will show the squres of only odd numbers of the lst
print({x:x**2 for x in lst })#this will show the squres of all the numbers in the lst
print({x for x in lst if x%3 == 0})#this will show all the multiples of 3

#set comprensition
print({x for x in [1,2,3,4,5,3,2,4,6,6,7,8,3,4,5,6,8,1,2,3,4,5,6,7,8]})
'''the above syntex will replace all the duplicates and just print them once '''

 



