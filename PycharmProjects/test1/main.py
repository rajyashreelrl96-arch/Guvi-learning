import random

# Number Guessing game(1 to 50)
print("Number Guessing game")
num = random.randint(1, 50)
while True:
    user_input = int(input("Guess a number between 1-50: "))
    if user_input < num:
        print("Your guess is too low")
    elif user_input > num:
        print("Your guess is too high")
    else:
        print("your guess is Correct!")
        break

# Scramble list of words
words = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"]

print("Unscramble the programming language names!")
for word in words:
    word_list = list(word)
    random.shuffle(word_list)
    scrambled_word = ''.join(word_list)

    while True:
        print("Scramble word : " + scrambled_word)
        guess = input("Your guess: ").lower()
        if guess == word:
            print("Correct!")
            break
        else:
            continue
