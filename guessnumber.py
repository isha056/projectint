import random
number=random.randint(1,100)
print("I have a number i n my mind. Can you guess it?")
number_of_guess_left = 3
while number_of_guess_left > 0:
    guess=int(input("Guess a number: "))
    if guess!=number:
        number_of_guess_left -=1

    if (guess==number):
        print('"congratulation you win"','Your score',10)
        break
    elif(guess<number):
        print('"have one more try"','your guess was too small')
    else:
        print('"have one more chance"','your guess was to high')
if guess==number:
    print('"Congratualtion you win"','your score',10)
else:
    print('"Better luck next time"','Your score',0)

