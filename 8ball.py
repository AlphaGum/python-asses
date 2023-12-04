import random
from time import sleep

options = ["yes", "no", "maybe","if your heart wants it","if your feeling bored"] #the 8 balls options 

input("ask me a question: ") #asking the program a question
print("hmmmm")
sleep (2) #making the prgram think for 2 secends before printing
num = random.randint(0,len(options))#randomises the 8 ball options
print(options[num]) #prints the result