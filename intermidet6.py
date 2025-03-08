#filter function 

def odd_even(num):
    if num%2 == 0 :
        return True
    
lst = [1,2,3,4,5,6]   


print(list(filter(odd_even,lst)))

#lambda using filter 

print(list(filter(lambda num : num%2 == 0,lst )))

#map using filter 
print(list(map(lambda num : num%2 == 0,lst )))