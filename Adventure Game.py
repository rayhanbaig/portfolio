def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You have two paths in front of you.")
    first_choice()

def first_choice():
    print("\n1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Which path do you choose? (1 or 2): ")
    
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Please select 1 or 2.")
        first_choice()

def left_path():
    print("\nYou walk down the left path and encounter a wild wolf!")
    print("1. Try to fight the wolf.")
    print("2. Run away.")
    choice = input("What do you do? (1 or 2): ")
    
    if choice == '1':
        print("\nYou bravely fight the wolf but get injured. You manage to escape but lose some health.")
        end_game("You survived but are injured. Game Over.")
    elif choice == '2':
        print("\nYou run away safely and find a hidden treasure chest!")
        end_game("You found the treasure! You win!")
    else:
        print("Invalid choice. Please select 1 or 2.")
        left_path()

def right_path():
    print("\nYou take the right path and find a mysterious old man.")
    print("1. Talk to the old man.")
    print("2. Ignore him and keep walking.")
    choice = input("What do you do? (1 or 2): ")
    
    if choice == '1':
        print("\nThe old man gives you a magical potion that grants you invincibility!")
        end_game("You feel invincible! You win!")
    elif choice == '2':
        print("\nYou ignore the old man and fall into a hidden trap!")
        end_game("You got trapped! Game Over.")
    else:
        print("Invalid choice. Please select 1 or 2.")
        right_path()

def end_game(outcome):
    print("\n" + outcome)
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        print("Thank you for playing! Goodbye!")
    else:
        print("Invalid choice. Please respond with 'yes' or 'no'.")
        play_again()

# Start the game
start_game()
