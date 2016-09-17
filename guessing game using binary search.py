#Computer guessing game using Binary Search
#author: Leonardo Mazuran
#last modified: 8 September 2016
import random
input1 = int(input("Input maximum range from 1 to 1000: "))
while input1 >1000 or input1 <1:
            input1 = int(input("Incorrect input! Try again: "))
first = 1
last = input1

while first <= last:
    m = (first + last) //2
    print ("Is " + str(m) + " Correct?")
    guess = input(" Input < for too low, > for too high, or y for corrrect: ")
    
    if guess ==">":
        last = m -1
    if guess =="<":
        first = m +1
    if guess =="y":
        break      
if guess == "y":
    print("Yeah " +str(m)+ " Is the number!" )
# no solution random  responses
if guess != "y":
    n = random.randint(1,5)
    switch = n
    while switch== n:
        if switch == 1:
            print ("What if I told you, you were messing with me.")
            break
        if switch == 2:
            print ("I dont understand you response therefor I will end this game.")
            break
        if switch == 3:
            print ("When curiosity killed the game. Nice Try.")
            break
        if switch == 4:
            print ("Not sure if your trolling me but, nice try.")
            break
        if switch == 5:
            print ("Nice try")
            break

      

