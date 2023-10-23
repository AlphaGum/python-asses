import random
from time import sleep

options = ["yes", "no", "maybe","if your heart wants it","if your feeling bored"]

input("ask me a question")
print("hmmmm")
sleep (2)
num = random.randint(0,len(options))
print(options[num])