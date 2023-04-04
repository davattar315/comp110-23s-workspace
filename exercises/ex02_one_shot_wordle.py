"""EX02: One Shot Wordle."""
__author__= "730480676"
secret_word: str = ("python")
word: str = input("What is your 6-letter guess? ")
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
All_Box: str = ""
guess_index: int = 0 
nextguess_index: int = 0
word_index: int = 0
#Here I have definied all the variables which will be used in this code#

if word == str(secret_word):
    print("Woo! You got it!")
playing = False
#If the secret word is guessed correctly, the program tells the user that and terminates# 
while len(word) != 6:
    word = input ("That was not 6 letters! Try again! ") 
    if word == str(secret_word):
        print("Woo! You got it!")
        playing = False
    else: print("Not quite. Play again soon!")
playing = False
#Here the code is not acccepting any guess that is not 6 letters, and recertifying the new guess as the input 
while word_index < len(secret_word):
    if word[word_index] == secret_word[word_index]:
        All_Box = All_Box + GREEN_BOX
        word_index = word_index + 1 
        Playing = True
        #Here the code is evaluating the secret at the same index as the word and denoting if there are any exact matches
    else:
        guess_index = 0
        playing = False
        while guess_index < len(secret_word) and playing is False:
            if secret_word[guess_index] == word[word_index]:
                All_Box = All_Box + YELLOW_BOX
                playing = True
            guess_index = guess_index + 1
            #Here the code is evaluating the secret word at n guess index, against all other indexes except its own, and then is relooping to reveluate
        if playing is False:
            All_Box = All_Box + WHITE_BOX
        word_index = word_index + 1 
        #Here the code is denoting that the letter is not found in the secret word and is relooping  to reevaluate 
print(All_Box)
playing = False
#Here the code is printing the final result and terminating