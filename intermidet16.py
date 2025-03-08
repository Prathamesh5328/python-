#inheritance
'''there are three types of inheritance
1)  single level inheritance
2) multiple inheritance
3) multi level inheritance
'''
#single level inheritance

class parent():
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def test (self):
        print('this is test parent class ')
class child(parent):#here we have inheriated the propertyes of parent class
    def test(self):
        print('this is child class ')

par = parent(1,2,3)
ch = child(4,5,6)
print(ch.a)
(ch.test())
(par.test())

#multiple insheritance 

class c1(object):
    def __init__(self) :
        self.str1 = 'shreyas'
        print('this is class 1 ')

class c2(object):
    def __init__(self) :
        self.str2 = 'shreyas'
        print('this is class 2 ')

class derivied (c1 , c2):
    def __init__(self):
        c1.__init__(self)
        c2.__init__(self)
        print("derivied ")
    def all(self):
            print(self.str1 ,self.str1 )

output = derivied()
output.all()


#multi level inheritance
class parent(object):
    def __init__(self , name ) :
        self.name = name 
    def getname(self): 
        return self.name
  
      
class child(parent):
    def __init__(self, name ,age ):
        parent().__init__(self, name)
        self.age = age  
        def getage(self):
            return self.age
         


class grandchild(child):
    def __init__(self, name, age , adress ):
        child().__init__(self, name, age)
        self.adress = adress 
    def getadress(self):
        return self.adress 

output = parent('shreyas')
output = parent('shreyas', 21)
output = parent('shreyas' , 21 , "india")

print(output.getname() , output.getage() , output.getadress() )
    
