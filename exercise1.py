import random
winning_no=random.randint(1,100)
# number=int(input("Enter a number between 1 and 100 to guess the winning number"))
# if number==winning_no:
#     print("Congratulations! You have won the game")
# if number>winning_no:
#     print("too high")
# if number<    

print("Welcome to the guessing game! Please enter a number between 1 and 10")
guess = int(input('Please enter your first guess? '))
if guess == winning_no:
    print('Well done, you got it right in your first try!')
else:
    if guess > winning_no:
        print('Too high! Try again.')
    elif guess < winning_no:
        print('Too low! Try again.')
            
guess = int(input('Please enter your next guess? '))
tries = 2