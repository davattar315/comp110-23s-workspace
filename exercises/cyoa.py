"""Choose your own adventure: The Castle of L'Frances Rouge."""
__author__ = "730480676"


import random
points: int = 0
player: str = ""
weapon: str = ""
LONGSWORD: str = "\U0001F5E1"
BATTLE_AXE: str = "\U0001F3CF"
CLUB: str = "\U0001FA93"
SWORD_AND_SHIELD: str = "\U0001F6E1"


def greet() -> None:
    """Saying hi!"""
    global player
    print("Hello valiant knight, and welcome to the Castle of L'Frances Rouge. You have been called here among knights from all over Europe to prove yourself as a master in duelling. Before we begin, what is thine name? (please note some of these emojis do not exist so they had to be substituted with similar ones) ")
    player = input()
    

def weapon_select() -> None:
    """Chosing weapon."""
    global weapon
    weapon_list: list[str] = [LONGSWORD, BATTLE_AXE, CLUB, SWORD_AND_SHIELD]
    weapon_choice_1: int = int(input("Before you begin duelling, you must select your weapon. Press 0 for longsword, press 1 for club, press 2 for battle axe and press 3 for sword and shield "))
    weapon_choice_2: str = weapon_list[weapon_choice_1]
    while weapon_choice_1 >= 4 or weapon_choice_1 < 0:
        weapon_choice_2 = input("It seems like you didn't select a weapon, please try again. Press 0 for longsword, press 1 for club, press 2 for battle axe and press 3 for sword and shield ")
    weapon = weapon_choice_2
    

def duel_1(choice: int) -> int:
    """First of two duels.""" 
    global player
    global weapon
    points: int = 0
    if choice == 1:
        points += 100
        print(f"This duel was a rout. {player} easily defeated Gerald the Gentle with their trusty {weapon}. The crowd loved it. Your crowd favor is now {points} ")
    elif choice == 2:
        points += 65
        print(f"This duel was a tough one. {player} and Reginald the Regular traded blows back and forth in a very protracted duel. Ultimately {player}'s {weapon} lead them to victory. Unfortunately, the crowd did not enjoy it very much. Your crowd favor is now {points} ")
    elif choice == 3:
        print(f"After duelling Karl the Killer, {player} was slain. It is clear they are not a master dueller. GAME OVER. FINAL SCORE = {points} ")
        points += 0
    return points


def duel_2() -> None:
    """Second of two duels."""
    global player
    global points
    global weapon 
    print(f"After your first duel, you had some time to rest and recuperate. However, now it is time for your next duel. Remember you have have {points} points of crowd favorability. Please select your opponent for your second duel. ")
    print("Please select your opponent for your second duel. Press 1 for Wilson the Wimpy, press 2 for Austin the Average, and press 3 for Michael the Monstrous ")
    user_input: int = int(input())
    damage_random: int = 100 - random.randint(50, 99)
    if user_input > 3 or user_input < 1:
        print("It seems as though you did not properly select a duel. Please try again. ")
        return duel_2()
    if user_input == 1:
        points += 100
        print(f"This duel was a rout. {player} easily defeated Wilson the Wimpy using their trusty {weapon} And as such the crowd loved it. This added 100 points to your crowd favor. It is {points} ") 
    elif user_input == 2:
        points += damage_random
        print(f"This duel was a tough one. {player} and Austin the Average traded blows back and forth in a very protracted duel. Ultimately {player}'s {weapon} lead them to victory. Unfortunately, the crowd did not enjoy it very much. Your crowd favor is now {points} ")
    elif user_input == 3:
        points == 0
        print(f"After duelling Michael the Monstrous {player} was slain. It is clear they are not a master dueller. GAME OVER. FINAL SCORE = {points} ")


def main() -> None:
    """Piecing together all preceding functions."""
    global player
    global points   
    playing: bool = True
    playing_2: bool = True
    while playing and playing_2:
        greet()
        weapon_select()
        duel_1(0)
        choice: int = int(input(f"{player}, you have the choice to select your opponent for your first duel. Press 1 for Gerald the Gentle, press 2 for Reginald the Regular, and press 3 for Karl the Killer. "))
        while choice > 3 or choice < 1:
            choice = int(input("It seems as though you did not properly select a duel. Please try again. "))
        points += duel_1(choice)
        if points == 0:
            playing = False
        duel_2()
        if points < 75 and points > 1:
            print(f"After two bad duels {player} was determined to be unworthy of remaining in the Castle of L'Frances Rouge, and was banished forever. GAME OVER. FINAL SCORE = {points}")
        if points >= 75 and points < 150:
            print(f"After their two duels {player} was deemed a worthy knight of the Castle of L'Frances Rouge, but was definitely not the best. GAME OVER. FINAL SCORE = {points}")
        if points >= 150:
            print(f"After two excellent duels {player} was deemed to be the most worthy knight in the whole kingdom. Good Job! GAME OVER. FINAL SCORE = {points}")
        NEW_GAME = int(input("Would you like to play again? Press 0 for yes and 1 for no"))
        if NEW_GAME == 0:
            playing = True  
        elif NEW_GAME == 1:
            playing_2 = False
        if int(NEW_GAME) > 1 or int(NEW_GAME) < 0:
            NEW_GAME = input("It seems like you did not select an option. Press 0 to play again, and press 1 to quit")
    if not playing:
        new_var: int = int(input("Would you like to play again? Press 0 for yes and 1 for no "))
        while int(new_var) > 0 or int(new_var) < 1:
            new_var = int(input("Would you like to play again? Press 0 for yes and 1 for no"))
            if input == 1:
                playing_2 = False


if __name__ == "__main__":
    main()
