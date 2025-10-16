import random
def hint(guess,number):
    if abs(guess - number) <= 5:
        return "You're very close!"
    elif abs(guess - number) <= 10:
        return "You're getting closer!"
    else:
        return "You're far away!"

def celebration_message(attempts):
    messages = [
        "Awesome!",
        "Congratulations!",
        "You're a genius!",
        "Well done!"
    ]
    return random.choice(messages) + f" You guessed it in {attempts} tries!"

num = random.randint(1, 50)
guesses = []

for attempt in range(5):
    a = int(input("Guess a number between 1 and 50: "))
    guesses.append(a)

    if a == num:
        print(celebration_message(attempt+1))
        break
    elif a > num:
        print("Too high!", hint(a, num))
    else:
        print("Too low!", hint(a, num))
else:
    print("Sorry! The correct number was {}".format(num))
    print(f"Your guesses were: {guesses}")
