#polymorphism 
'''there are two types of polymorphysm
   1) built in 
   2) user defined '''
'''basic examples are as folloows'''
#built in functions 
print('len of strinfg', len("youtube"))
print('len of list', len([1,2,3,4]))

#user defined fun 
def add(x,y,z = 0 ):
    return x+y+z

        #derivied coad
print('sum  of two num ', add(2,3))
print('sum  of three num ', add(2,3,4)) 

class man_1():
    def name(self):
       print('ninad')
    def hight(self):
       print('5.10')
    def language(self):
       print('marathi')

class man_2():
    def name(self):
       print('shreyas')
    def hight(self):
       print('5.9')
    def language(self):
       print('english')

m1 = man_1()
m2 = man_2()

for details in (m1,m2):
   details.name()
   details.hight()
   details.language()

#polyorphism  using inheritance
class animal:
   def intro(self):
      print('there are many types of animal in the world')
   def types(self):
      print('wild animals and domastic animal') 

class wild(animal):
   def animal_1(self):
      print('lion, tiger, chitta')
   

class wild(animal):
   def animal_1(self):
      print('lion, tiger, chitta')


class domastic(animal):
   def animal_1(self):
      print('dog, cat , cow ')

ani = animal()
ani_wild = wild()
ani_domastic = domastic()

print(ani.types())
print(ani.intro())
print('\n')
print(ani_wild.intro())
print(ani_wild.types())
print(ani_wild.animal_1())
print('\n')
print(ani_domastic.intro())
print(ani_domastic.types())
print(ani_domastic.animal_1())