import random
print("Number Guessing Game")
number=random.randint(1,9)

chances=0

print("Guess the number between 1 and 9")

while chances<3:
    guess=int(input("Enter your guess, it should be a number\n"))
    if guess==number:
        print("Congratulations")
        break
    elif guess<number:
        print("Try a higher number",guess)
    else:
        print("Try a lower number", guess)
    chances+=1

if not chances<3:
    print("You Loose... Loser, the number was", number)
