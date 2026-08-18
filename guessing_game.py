import random
easy_word=["apple","train","mango","motor","car"]
medium_word=["mountain","railway","drawing","laptop","computer"]
hard_word=["artificial","intelligent","pineapple","education","meteroid"]
print("Welcome to the password guessing game!")
print("Choose the difficulty level:easy,medium,hard:")
level=input("Enter difficulty:").lower()
if level=="easy":
    secret=random.choice(easy_word)
elif level=="medium":
    secret=random.choice(medium_word)
elif level=="hard":
    secret =random.choice(hard_word)
else:
    print("Invalid input.Defaulting to easy level")
    secret =random.choice(easy_word)
attempts=0
print("\n Guess the secret pasword")
while True:
    guess=input("Enter your guess:").lower()
    attempts+=1
    if guess==secret:
        print(f'Congratulations!YOu guessed it in {attempts}attempts')
        break
    hint=""
    for i in range(len(secret)):
        if i<len(guess)and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint:",hint)
print("Gamr Over!")
    