import random

fruits = ['apple', 'banana', 'cat', 'orange', 'pineapple', 'cow']

word = random.choice(fruits)
guesses = set()

while True:
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    
    print(display)

    if "_" not in display:
        print("You won!!! Word:", word)
        break

    guess = input("Your guess letter: ")
    guesses.add(guess)


    if len(guesses) == 11:
        print("You lost!", word)
        break
 