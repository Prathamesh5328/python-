#string formating

def dub(name):
    return 'hello {} this is advance string formating'.format(name)

print(dub('shreyas'))

def hotel(name,room): 
    return 'hello {} your room number is {}'.format(name,room)
print(hotel('shreyas','21'))
'''the function hotel and hotel_1 are not same the
   difference between them is you cants disturbe the sequance of the output but 
   in hotel_1 yo can, as they are properly defined '''
def hotel_1(name,room):
    return 'hello {name} your room number is {room}'.format(room = room , name =name)
print(hotel_1('shreyas','21'))