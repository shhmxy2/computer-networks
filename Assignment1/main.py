#from server import ServerSocket
from client import ClientSocket
import subprocess

def start_a_new_game():
    clientserver = ClientSocket().start()
    print("The game has started!")
    clientserver.run()
    clientserver.close()

def main():
    while True:
        print("Welcome to the number guessing game!")
        start_a_new_game()
        again = input("Do you want to play again? (y/n): ")
        new_game = True
        while True:
            if again.lower() == 'n' or again.lower() == 'no':
                new_game = False
                print("Thank you for playing!")
                break
            elif again.lower() == 'y' or again.lower() == 'yes':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                again = input("Do you want to play again? (y/n): ")
        if new_game:
            continue
        else:
            break

if __name__ == '__main__':
    main()