#Guess_the_number
import random
print("GUESS A NUMBER BETWEEN \'1-50\':")
number=random.randint(1,50)#number is generated from the computer 
level=input("Choose the level of difficulty ..type \'easy\' or \'hard\':").lower()
def game(guess):
    guessing_count=0
    print(f"YOU HAVE {guess} GUESSES EXACTLY TO GUESS THE NUMBER:")
    for i in range(1,guess+1):
        guessing_number=int(input(f"GUESS A NUMBER YOU HAVE {guess-guessing_count} CHANCES:"))
        guessing_count+=1
        if(guessing_number>number):
            print(f"YOUR GUESS IS TOO HIGH:")
        if(guessing_number<number):
            print(f"YOUR GUESS IS TOO LOW:")
        if(guessing_number==number):
            print(f"YES, YOUR GUESS IS CORRECT AND THE NUMBER IS {guessing_number} ")
            break
        if(guessing_number!=number and guessing_count<guess):
            print("TRY AGAIN!")
    if(number!=guessing_number and guessing_count==guess):
        print("YOU LOSE")
if(level=='easy'):
    game(guess=10)#function call
if(level=='hard'):
    game(guess=5)#function call


