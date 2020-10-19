secret = 42

print("Please add your name:")
name = input()
print("Welcome, " + name.title() + "!")

guess = int(input("Guess The number: "))

if guess == secret:
    print("Congratulate! You already know the answer to everything!")
else:
    print("Sorry, keep guessing...")
