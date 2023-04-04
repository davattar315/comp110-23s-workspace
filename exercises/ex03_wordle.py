"""Making a structured Wordle"""
__author__ = "730480676"
def contains_char(all_char: str, sing_char: str) -> bool:
    #checks if all_char contains sing_char
    assert len(sing_char) == 1
    all_char: str = ""
    search: bool = True
    idx: int = 0

    while idx < len(all_char):
        if all_char[idx] == sing_char:
            search = True
            return search

        else:
            idx = idx + 1
    search = False
    return search

def emojified(guess: str, secret: str) -> str:  
    #creates different emojis 
    assert len(secret) == len(guess)
    idx: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    final = ""
    idx: int = 0

    while idx<len(secret):
        if guess[idx] == secret[idx]:
            final = final + GREEN_BOX
            #determines if green is correct
        elif contains_char(secret, guess[idx]):
            #determines if yellow is correct
            final = final + YELLOW_BOX
        else:
            final = final + WHITE_BOX
            #determines if white is correct
        idx = idx + 1 
    return final 
    
def input_guess(length : int) -> str:
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} characters! Try again: ")
    return guess

def main () -> None:
    #combines all functions and orders them in a gaming sequence 
    attempt: int = 1 
    secret: str = "codes"
    mguess: str = ""
    win: bool = False
    while not win and attempt <= 6:
        print(f"=== Turn {attempt}/6 ===")
        mguess = input_guess(len(secret))
        print (emojified(mguess, secret))
        if mguess == secret:
            win = True 
        attempt = attempt + 1
    if win:
        print(f"You won in {attempt-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tommorrow!")
if __name__ == "__main__":
    main()