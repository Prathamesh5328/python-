# classes and object

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00 
    def description (self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "fer"
car1.color = "red"
car1.kind = "convertable"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "jumb"
car2.colour = "blue"
car2.kind = "van"
car2.value =10000.00


# test code
print(car1.description())
print(car2.description())

class mobile:
    company_name = ""
    colour = ""
    price = 100.00

    def descriptionmob(self):
     desc_mob ="this %s mobile is of %s colour and its price is %d" %(self.company_name , self.colour , self.price)
     return desc_mob

mobile1 = mobile()
mobile1.company_name = "redmi"
mobile1.colour = "ice white"
mobile1.price = 12000.00

print(mobile1.descriptionmob())