import random

# human is player
print("Human is player!")
print("which one should choose a number?")
print("1. Human")
print("2. Computer")
input1 = int(input("1/2:"))
if input1 == 1:
    number1 = int(input("Give a number between 1 and 100: "))
    while number1 >100 or number1 <1:
            number1 = int(input("Incorrect input! Try again: "))
if input1 == 2:
    number1 = random.randint(1,100)

guess = int(input("Guess a number between 1 and 100."))
count = 1
while guess != number1:
    
    if guess > number1:
         print( guess, "to high")
         
    if guess < number1:
         print (guess, "too low")
    guess = int (input("Try again: "))
    count = count + 1
print(guess, "is the winning number!")
if count == 1:
    print ("It took you 1 try")
else:
        print ("It took:" , count, "tries")
print()

# Computer is player
print ("Computer is player!")
print()
print("which one should choose a number")
print("1. Human")
print("2. Computer")
input2 = int(input("1/2:"))
if input2 == 1:
    number2 = int(input("Give a number between 1 and 100: "))
    while number2 >100 or number2 <1:
            number2 = int(input("Incorrect input! Try again: "))
if input2 == 2:
    number2 = random.randint(1,100)
    print("The computer has choosen: ", number2)

a = 1
z = 100
count1 =1
guess = random.randint(1,100)
while guess != number2:
    
    if guess > number2:
       z = guess-1
       print(guess,"to high")
         
    if guess < number2:
        a = guess+1
        print(guess,"to low")
        
    guess = random.randint(a,z)
    count1 = count1 + 1
print(guess, "is the winning number!")
if count1 == 1:
    print ("It took the computer 1 try")
else:
    print ("It took:" , count1, "tries")  
