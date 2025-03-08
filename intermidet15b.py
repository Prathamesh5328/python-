#exception handlining 
#finally and rais
#finally 

try :
    a = int(input('value \n'))
    b = int(input('value \n'))
except Exception as e:
    print(e)
else:
    print(a+b)
finally:
    print('code is succesfully executed with no error ')

# rise 
 
a = int(input('enter the number \n'))
b = int(input('enter the number \n'))
c = a + b

if c  < 50:
    raise Exception('value %d  is less thean 50  '%(c))
elif c < 100 :
     raise Exception('value %d is less thean 100 '%(c))
else:
     print("code %d is above 100" %(c))
 



