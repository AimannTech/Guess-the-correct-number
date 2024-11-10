# guess the correct number

import random
n = random.randint(1, 100)
a = -1 # no one will guess neg no
guesses = 1 

while (a != n) :
    a = int(input("Guess the  number:"))
    if (a > n):# a is greeter than n then
        print("Lower number please")
        guesses +=1
    elif (a < n): #a is Lower than n 
        print("Higher number please")
        guesses +=1
print(f"You have Guess the number {n} corretly in {guesses} attempts")
