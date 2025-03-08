#basic os commands need to be learned 

f = open('rough.py','w') 
'''('rough.py'),'r') which is for the read mode and "w" for the write mode
 and ('rough.py','r+') for write as well read the file'''  
f.write("#hello \n")#this argument will just write the stuff which is fidded
f.write("#how are you \n")
f.close()#this should be written to impliment all what you wanted to be in that file 
#print(f.tell())#this will print how many numirical space is taken by the perticular file 
import os
#os.remove('rough.py')#this will deleat the file which was mentained by u in the argument 
print(os.getcwd())#this perticular argument will show you the path of the file u are working on 
print(os.listdir())#this perticular argument will show you all the file names includee in that dirictory 



