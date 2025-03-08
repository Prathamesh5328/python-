#opps in python 
#classes and object 
'''as every defined veriable is an object therefore a ia also a object'''
a = 10 
print(type(a))

'''the example of the class which is empty and have nothing means no object'''
class vehicle:
    pass 

'''a class with a object '''

class bike:
    def __init__(self, colour , engine_type , weeles):
        self.colour = colour
        self. engine_type = engine_type
        self.weeles = weeles

yamaha = bike('green','s16' ,'alloy')
yamaha.weeles
yamaha.colour
yamaha.colour

re = bike('silver', 'clasic350', 'alloy')
re.colour
re.engine_type
yamaha.weeles

'''another example of clases and objects '''
'''the code below is the normal way to code '''

l = [1,2,3,4,5,6,7,8,9]
print(len(l))


class lst_l1:
    def l1 (self,a):
        if type(a) == list:
            return(len(a))
        else:
            print('there is an error ')


alist = lst_l1()
print(alist.l1([1,2,3,4,5,6,7,8,9]))
        