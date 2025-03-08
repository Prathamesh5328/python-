#logging and debugging 
import logging as lg 
import os
#os.mkdir('log')
os.chdir(os.getcwd() + '/' + 'log')
print(os.getcwd())
lg.basicConfig(filename = 'yt.log', level=lg.INFO , format = '%(asctime)s %(message)s \n')
# lg.info("hey subscribers")
# lg.warning('warning!!! subscribe my channel')
# lg.error('this is error message')

#exception handling log code 
import logging as lg 
import os

def yt(a,b):
     try :
        lg.info(str(a) + str(b))
        div = a/b
        return div 
     except Exception as e :
         print('ther is an error check the log file ')
         lg.error('error has occured ')
         lg.exception(str)
print(yt(1,0))