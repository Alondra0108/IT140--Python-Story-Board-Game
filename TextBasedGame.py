# Alondra Paulino Santos
# Function to show instructions
def show_instructions():
    """Prints the instructions at the start of the game."""
    print("Welcome to the Mario Text Adventure Game!!!")
    print(
        "Goal: Collect 6 items to help Mario save Princess Peach from Bowser and win the game, or be defeated by "
        "Bowser.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("To exit the game, type 'exit'.\n")


# Function to display the player's current status
def show_status(current_room, inventory, items):
    print(f"\nYou are in the {current_room}.")

    # Show the item in the room if there is one
    if items[current_room]:
        print(f"You see a {items[current_room]} here.")

    # Show the player's current inventory
    print(f"Inventory: {inventory}")


# Main function to run the Mario Text Adventure Game
def main():
    """Main function to run the Mario Text Adventure Game."""

    # Define the room connections and items using dictionaries
    rooms = {
        "Great Hall": {"north": "Gallery", "south": "Bedroom", "east": "Kitchen", "west": "Library"},
        "Library": {"east": "Great Hall"},
        "Master Bedroom": {"west": "Bedroom"},  # Master Bedroom is east of Bedroom
        "Gallery": {"south": "Great Hall", "east": "Solar"},  # Solar is east of Gallery
        "Bedroom": {"north": "Great Hall", "east": "Master Bedroom"},
        "Dining Room": {"south": "Kitchen"},  # Bowser's room, accessible from Kitchen
        "Kitchen": {"north": "Dining Room", "west": "Great Hall"},
        "Solar": {"west": "Gallery"}
    }

    # Define the items in each room (all items are lowercase)
    items = {
        "Great Hall": None,
        "Library": "mega star",
        "Master Bedroom": "super hammer",
        "Gallery": "catsuit",
        "Bedroom": "joshi",
        "Dining Room": None,  # Bowser's room
        "Kitchen": "mushroom",
        "Solar": "fire flower"
    }

    # Initialize player's starting room and inventory
    current_room = "Great Hall"
    inventory = []

    # Show the instructions at the start of the game
    show_instructions()

    # Main gameplay loop
    while True:
        # Display player's current status
        show_status(current_room, inventory, items)

        # Get player input (command)
        command = input("Enter your move: ").lower().split()

        # Check for empty input
        if not command:
            print("You must enter a command. Please try again.")
            continue

        # Exit the game if the player types 'exit'
        if command[0] == 'exit':
            print("You have exited the game. Thanks for playing!")
            break

        # Handle movement commands (go north, go south, etc.)
        elif len(command) == 2 and command[0] == 'go':
            direction = command[1]

            # Validate the direction and move to the new room
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Handle item collection command (get item_name)
        elif len(command) >= 2 and command[0] == 'get':
            item_name = " ".join(command[1:])

            # Check if the item is in the current room and not None
            if items[current_room] and items[current_room].lower() == item_name.lower():
                inventory.append(items[current_room])  # Add the item to the player's inventory
                print(f"{items[current_room]} added to your inventory.")
                items[current_room] = None  # Remove the item from the room after collecting
            else:
                print(f"There is no {item_name} in this room or you've already collected it.")

        # Invalid command
        else:
            print("Invalid command. Please use 'go [direction]' or 'get [item name]' or type 'exit' to leave the game.")

        # Check if the player has won or lost the game
        if current_room == "Dining Room" and len(inventory) == 6:
            print("Congratulations! You have collected all the items and defeated Bowser to save Princess Peach!")
            break
        elif current_room == "Dining Room" and len(inventory) < 6:
            print("Game Over! You did not collect all the items. Bowser defeated you.")
            break

    # Display the player's inventory at the end
    print("\nGame Over!")
    print("Your inventory:", inventory)


# Run the game
if __name__ == "__main__":
    main()
