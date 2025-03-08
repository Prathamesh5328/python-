#encapsulation 
'''there are two methodes in the encapsulation
 1)  protacted
 2)  private '''
#protected methode
class student:
    def __init__(self ,name ,age ,gender):
        self._name = name 
        self._age = age 
        self._gender = gender
    def det(self):
        print('age is : ' ,  self._age )
        print('gender is : ' , self._gender )

class out(student):
    def __init__(self, name, age, gender):
        student.__init__(self ,name, age, gender)

    def details(self):
        print('name is : ', self._name )
        self.det()

x = out('shreyas', 17 , 'male')
x.details()


#private methode

'''class student:
    def __init__(self ,name ,age ,gender):
        self.name = name 
        self.__age = age 
        self.__gender = gender
  

class out(student):
    def __init__(self, name, age, gender):
        student.__init__(self ,name, age, gender)

    def details(self):
        print('name is : ', self.name )
        print('age is :', self.__age)
        print('gender is :', self.__gender)


x = out('ninad', 17 , 'male')
x.details()'''
#the above syntes will only print the name of the applicant in this case its 'ninad'other it will not print and it will show error 
#the below example will also be the private but it will stil print the pravate data on our command
#private methode

class student:
    def __init__(self ,name ,age ,gender):
        self.name = name 
        self.__age = age 
        self.__gender = gender
    def det(self):
        print('age is :', self.__age)
        print('gender is :', self.__gender)

class out(student):
     def __init__(self ,name ,age ,gender):
        student.__init__(self ,name, age, gender)
    
     def details(self):
         print('name is : ', self.name )
         self.det()

x = out('harshal',17,'femail')
x.details()

'''the reason why the above methode didnt throw error and even print the stuff which was private 
is ,it was already defined inside the class in line no 67('self.det()') to call the stuff and we again call it
from outside so therefor it didnt throw the error and alos print it down '''
'''and in the private methode example one it throws the error because it was not pre defined in the 
  class by itself and we still call it from the outside '''