import random
print("WELCOME TO THE NUMBER GUESSINHG GAME")
val=input("ENTER YOUR NAME:")
print(val)
print("entering number should be in between 1 to 99")
print("guess the number and have fun")
real_num = random.randrange(1, 50)
total_attempts = 10
while True:
    guess = int(input("Enter a number between 1 to 99: "))
    if guess == real_num:
        break
    total_attempts -= 1
    if total_attempts == 0:
        break
    if guess < real_num:
        print("Guess higher")        
    else:
        print("Guess lower")    

if total_attempts != 0:
    print("YOU WIN")
else:
    print("completed 10 attempts")
