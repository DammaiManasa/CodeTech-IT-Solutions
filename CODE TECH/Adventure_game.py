#Adventure_game
def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself standing in front of a mysterious cave.")
    print("Do you want to enter the cave? (yes/no)")
    choice = input().lower()
    
    if choice == "yes":
        cave()
    elif choice == "no":
        print("You decide not to enter the cave. The adventure ends here.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        start_game()

def cave():
    print("You enter the cave and see two paths: left and right.")
    print("Which path do you choose? (left/right)")
    choice = input().lower()
    
    if choice == "left":
        print("You encounter a treasure chest! Congratulations, you've found a valuable artifact.")
        print("Do you want to continue exploring the cave? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            continue_exploring()
        elif choice == "no":
            print("You decide to leave the cave with your treasure. The adventure ends here.")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            cave()
    elif choice == "right":
        print("You encounter a fierce dragon! You must fight for your life.")
        fight_dragon()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        cave()

def continue_exploring():
    print("As you continue exploring, you find a hidden passage.")
    print("Do you want to enter the passage? (yes/no)")
    choice = input().lower()
    
    if choice == "yes":
        print("You discover a secret chamber filled with gold!")
        print("Congratulations, you've become rich. The adventure ends here.")
    elif choice == "no":
        print("You decide to leave the passage unexplored. The adventure ends here.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        continue_exploring()

def fight_dragon():
    print("You must decide how to approach the dragon:")
    print("1. Attack with your sword")
    print("2. Try to reason with the dragon")
    choice = input()
    
    if choice == "1":
        print("You engage in a fierce battle with the dragon.")
        print("You manage to defeat the dragon and emerge victorious!")
        continue_exploring()
    elif choice == "2":
        print("You attempt to reason with the dragon, but it's too enraged to listen.")
        print("You have no choice but to fight.")
        fight_dragon()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        fight_dragon()

start_game()
