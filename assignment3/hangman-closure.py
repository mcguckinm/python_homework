def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display="".join([char if char in guesses else "_" for char in secret_word])
        print(display)

        return "_" not in display
        
    
    return hangman_closure

#Mainline code
secret_word=input("Enter the secret word: ")
hangman=make_hangman(secret_word)
while True:
    letter=input("Guess a letter: ")
    if hangman(letter):
        print("Congratulations! You've guessed the word!")
        break
