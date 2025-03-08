sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words : 
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)

 #this below code is also based on my logic
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
for x in numbers:
   if x > 0 :
      newlist.append(x)
      x += 1
print(newlist)

#this is beyound the topic so excuse while reading 
import numpy as np
numbers1 = np.array([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])
newlist2 = lambda x : x > 0 
print(list(filter(newlist2 ,numbers1 )))
# the very first coad writen and compose by my own logic
