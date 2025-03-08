#Dictionaries
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook2 = {
   " prathamesh " : 7448259457,
   " baba " : 9890004640,
   " harshal " : 9921442109,
   'kasturi' : 9022450906


}
del phonebook2[" kasturi "] 
phonebook2[" kasturi "] = 9022450906 #this ststment will again add the kasturi in the dictionaries
# for name, number in phonebook2.items():
#     print("phone number of %s is %d " %(name , number))
print(phonebook2)

if " kasturi " in phonebook2:
    print("kasturis contact is in the phonebook list") 
    
    