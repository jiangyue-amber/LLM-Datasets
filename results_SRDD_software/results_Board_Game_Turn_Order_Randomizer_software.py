# Software Name: Board_Game_Turn_Order_Randomizer
# Category: Board_Game
# Description: Board Game Turn Order Randomizer is a software application that ensures fair gameplay by randomizing the turn order for board games. Players input their names and the number of players, and the software generates a random turn order. This eliminates any bias or advantage associated with a predetermined turn order, creating a balanced gaming experience. The simple implementation and lack of complex requirements make this software easy to use and accessible to all board game enthusiasts.

import random

def randomize_turn_order():
    """
    Randomizes the turn order for a board game based on player names.
    """

    try:
        num_players = int(input("Enter the number of players: "))
        if num_players <= 0:
            print("Invalid number of players. Please enter a positive integer.")
            return

        players = []
        for i in range(num_players):
            name = input(f"Enter the name of player {i+1}: ")
            players.append(name)

        random.shuffle(players)

        print("\nRandomized Turn Order:")
        for i, player in enumerate(players):
            print(f"{i+1}. {player}")

    except ValueError:
        print("Invalid input. Please enter a number for the number of players.")

if __name__ == "__main__":
    randomize_turn_order()