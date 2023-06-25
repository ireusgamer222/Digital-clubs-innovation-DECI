import time
import random


# Checks the input of the player in any event


def inputchecker():
    result = False
    x = None
    while result == False:
        try:
            time.sleep(2)
            x = int(input("Please Enter 1 or 2!\n"))
            if x in range(1, 3):
                result = True
        except ValueError:
            continue
    return int(x)


# Checks the input of the player with considerations of the inventory
def inventorychecker(limit):
    result = False
    x = None
    while result == False:
        try:
            time.sleep(2)
            x = int(input("Please Enter item's index starting from 0!\n"))
            if x in range(limit):
                result = True
        except ValueError:
            continue
    return int(x)


# Player defending functions


def defend(UserInput, Inventory, Monster):
    # Things that happen when the player is approached by an enemy
    # UserInput will determine wether the player will attack or not
    # items can be used to attack a monster by a choice
    # Return value is increase or decrease in score

    if UserInput == 1:
        time.sleep(2)
        print("You Choose to Attack the " + Monster + "!")
        time.sleep(2)
        print("Do you wish to use any items while attacking the monster?")
        UserInput = inputchecker()
        time.sleep(2)
        # User choosing wether he want to attack with item or not
        if UserInput == 1:
            print(Inventory)
            time.sleep(2)
            print("Which item do you like to choose?")
            time.sleep(2)
            UserChoice = inventorychecker(len(Inventory))
            # Item that the player chose to attack with
            x1 = Inventory[UserChoice]
            if Monster == "Wicked Witch":
                if x1 == "Trusty dagger":
                    time.sleep(2)
                    print("Sadly Your Trusty dagger didn't help you well")
                    time.sleep(2)
                    print("The witch damaged you really hard!")
                    time.sleep(2)
                    return -1
                elif x1 == "Iron Sword":
                    time.sleep(2)
                    print("You use the Iron sword to attack the witch!")
                    time.sleep(2)
                    print("She couldn't stop your attacks with her spell")
                    time.sleep(2)
                    print("You killed the witch using the Iron Sword!")
                    time.sleep(2)
                    return 5
                elif x1 == "Wooden Sword":
                    time.sleep(2)
                    print("You are running towards the witch with Wood Sword")
                    time.sleep(2)
                    print("The witch cast some spells to block your attack")
                    time.sleep(2)
                    print("She blocked your attack, damaged you!")
                    time.sleep(2)
                    print("but you also hurt her really bad")
                    time.sleep(2)
                    return 2
                elif x1 == "Weak Wand":
                    print("You are standing at your place and ready to")
                    time.sleep(2)
                    print("cast a spell on the witch usinga Weak Wand!")
                    time.sleep(2)
                    print("Sadly your spell was no match for the spell")
                    time.sleep(2)
                    print("she damaged you and you damaged her a little!")
                    time.sleep(2)
                    return 1
                else:
                    print("You are attacking the witch with nothing.")
                    time.sleep(2)
                    print("She destoryed you and now you started to run away")
                    time.sleep(2)
                    # chance of losing because score of not using an item
                    x = random.randint(-1, 0)
                    return x
            if Monster == "Troll":
                if x1 == "Trusty dagger":
                    time.sleep(2)
                    print("Your Trusty dagger helped you to defend yourself ")
                    time.sleep(2)
                    print("but you didn't damage the troll in any way")
                    time.sleep(2)
                    print("The troll felt scared and started to run away")
                    return 0
                elif x1 == "Iron Sword":
                    time.sleep(2)
                    print("You use the Iron sword to attack the Troll!")
                    time.sleep(2)
                    print("The troll felt scared and stand his place")
                    time.sleep(2)
                    print("You cut the troll into two halves and won")
                    time.sleep(2)
                    return 5
                elif x1 == "Wooden Sword":
                    time.sleep(2)
                    print("You running at troll with Wooden Sword in hand")
                    time.sleep(2)
                    print("The troll also started to run towards you")
                    time.sleep(2)
                    print("You used your Wooden sword and ")
                    time.sleep(2)
                    print("hit him really hard which got to lose his life")
                    time.sleep(2)
                    return 2
                elif x1 == "Weak Wand":
                    time.sleep(2)
                    print("You are standing at your place and ")
                    time.sleep(2)
                    print("ready to cast spell on the troll using Weak Wand!")
                    time.sleep(2)
                    print("The troll started running towards you, ")
                    time.sleep(2)
                    print("but you attacked him with your magic killing him!")
                    time.sleep(2)
                    return 1
                else:
                    time.sleep(2)
                    print("You are attacking the troll with nothing.")
                    time.sleep(2)
                    print("He destoryed you at instant ")
                    time.sleep(2)
                    print("and now you started to run away")
                    time.sleep(2)
                    # chance of losing because score of not using an item
                    x = random.randint(-1, 0)
                    return x
        # The player chose not to attack the monster using any items
        else:
            time.sleep(2)
            print("You are attacking the troll with nothing.")
            time.sleep(2)
            print("He destoryed you at instant, now you started to run away")
            time.sleep(2)
            # chance of losing because score of not using an item
            x = random.randint(-1, 0)
            return x
    # The player didn't choose to attack the monster, he chose to run away
    else:
        print("You decided to run away! this can cause to lose some score!")
        time.sleep(2)
        print("You ran back to the field.")
        time.sleep(2)
        # chance in decreasing the player's score because of running away
        x = random.randint(-2, 0)
        return 0
# Cave event


def cave(Userchances):
    # Things that happen to the player goes in the cave
    # Items that you can find in the cave
    items_in_cave = ["Strong Wand", "Iron Sword", "Wooden Sword", "Weak Wand"]
    time.sleep(2)
    print("You started to walk torwards the cave to peer into it!")
    time.sleep(2)
    print("It isn't very large cave.")
    time.sleep(2)
    print("You started wandering in the cave and suddenly found something!")
    time.sleep(2)
    if Userchances > 1:
        # Random item in the cave that the play can take
        x = random.choice(items_in_cave)
        print("You found a " + x + " next to a rock!")
        time.sleep(2)
        print("Do you wish to take it or not!")
        time.sleep(2)
        print("Enter 1 to take it and 2 to not")
        time.sleep(2)
        UserInput = inputchecker()
        if UserInput == 1:
            print("You chose to take the item and now it is your in inventory")
            time.sleep(2)
            print("After a while you started to leave the cave and ran")
            time.sleep(2)
            return x
        if UserInput == 2:
            print("You chose to not take the item.")
            time.sleep(2)
            print("After a while you started to leave the cave and ran")
            time.sleep(2)
    # chance of not finding anything inside the cave
    else:
        print("You didn't find anything while wandering through the cave.")
        time.sleep(2)
        print("After a while you started to leave the cave and ran")
        time.sleep(2)
# House event


def house(Userchances, Inventory):
    # Things that happen to the player in the house
    # UserChances will get an item, face a monster
    # Player's Inventory will be inserted
    # Items that can help the player in defending
    items_in_house = ["Strong Wand", "Iron Sword", "Wooden Sword", "Weak Wand"]
    # Enemies or Nice monsters that the player can face in the house
    Enemies_in_House = ["Wicked Witch", "Troll"]
    print("You approach the abandoned house.")
    time.sleep(2)
    print("You Enter the abandoned house!")
    time.sleep(2)
    # Player will find an item
    if Userchances == 1:
        item = random.choice(items_in_house)
        print("You found a " + item + "!")
        time.sleep(2)
        print("Do you wish to take it?")
        time.sleep(2)
        print("Enter 1 to take it or 2 to not")
        choice = inputchecker()
        if choice == 1:
            return item
        else:
            return None
    # Player will find a monster
    else:
        # A Random Monster will appear
        x = random.choice(Enemies_in_House)
        print("A " + x + " has found you inside the house!")
        if x == "Wicked Witch":
            time.sleep(2)
            print("She laughs as she watches you inside the house.")
            time.sleep(2)
            print("She started to cast some magic on you")
            time.sleep(2)
            print("You feel like to do something quick!")
            time.sleep(2)
        else:
            time.sleep(2)
            print("He noticed you!")
            time.sleep(2)
            print("Prepare to do something quick!")
        time.sleep(2)
        print("Do you wish to Attack or run away?")
        time.sleep(2)
        print("Enter 1 to Attack or 2 to Run away.")
        UserInput = inputchecker()
        if UserInput == 1:
            return defend(1, Inventory, x)
        else:
            return defend(2, Inventory, x)
# Main Function


def main():
    # Random events to happen when entering a house or cave etc...
    Userchances = 0
    inventory = ["Trusty dagger"]  # Inventory to carry items to defend
    UserInput = "y"  # UserInput
    total_score = 0  # The total score of the game
    while UserInput == "y":
        while True:
            print("You find yourself standing in an field, filled with grass")
            print("yellow wildflowers.")
            time.sleep(2)
            print("Rumor has it that a wicked fairie is somewhere here, has")
            print("been terrifying the nearby village.")
            time.sleep(2)
            print("In front of you is a house.")
            time.sleep(2)
            print("To your right is a dark cave.")
            time.sleep(2)
            print("In your hand you hold your trusty dagger.")
            time.sleep(2)
            # First Event!!!
            print("Enter 1 to Enter the House")
            time.sleep(2)
            print("Enter 2 to peer into dark cave")
            time.sleep(2)
            print("What would you like to do?")
            time.sleep(2)
            UserInput = inputchecker()
            # User Input HOUSE EVENT
            if UserInput == 1:
                # Possibilities in the house
                Userchances = random.randint(1, 2)
                # The player will get an item
                if Userchances == 1:
                    new_item = house(Userchances, inventory)
                    inventory.append(new_item)
                # The player will be attacked inside the house
                else:
                    total_score += house(Userchances, inventory)
            # User Input CAVE EVENT
            if UserInput == 2:
                # Possiblilites in the cave
                Userchances = random.randint(1, 5)
                new_item = cave(Userchances)
                inventory.append(new_item)
                CAVE_EVENT = False
            time.sleep(2)
            print("Your current score is " + str(total_score))
            time.sleep(2)
            # Endgame if score is less than 0
            if total_score < 0:
                break
            time.sleep(2)
            print("You are now in the field.")
            time.sleep(2)
            print("Your current inventory is:")
            time.sleep(2)
            print(inventory)
            time.sleep(2)
            print("In front of you is a house.")
            time.sleep(2)
            print("To your right is a dark cave.")
            time.sleep(2)
            while True:
                # Second Event!!!
                print("Enter 1 to Enter the House")
                time.sleep(2)
                print("Enter 2 to peer into dark cave")
                time.sleep(2)
                print("What would you like to do?")
                time.sleep(2)
                UserInput = inputchecker()
                # User Input HOUSE EVENT
                if UserInput == 1:
                    # Possibilities in the house
                    Userchances = random.randint(1, 2)
                    print("You decided to go to another house.")
                    time.sleep(2)
                    # The player will get an item
                    if Userchances == 1:
                        new_item = house(Userchances, inventory)
                        inventory.append(new_item)
                    # The player will be attacked inside the house
                    else:
                        total_score += house(Userchances, inventory)
                    break
                # User Input CAVE EVENT
                if UserInput == 2:
                    if CAVE_EVENT == False:
                        print("You went to the cave again.")
                        time.sleep(2)
                        print("You went to the cave again")
                        time.sleep(2)
                        print("You returned back to the field again.")
                        time.sleep(2)
                    else:
                        # Possiblilites in the cave
                        Userchances = random.randint(1, 5)
                        new_item = cave(Userchances)
                        inventory.append(new_item)
                        CAVE_EVENT = False
            print("Your current score is " + str(total_score))
            time.sleep(2)
            # Endgame if score is less than 0
            if total_score < 0:
                break
            while True:
                # Third Event!!!
                print("Enter 1 to Enter the House")
                time.sleep(2)
                print("Enter 2 to peer into dark cave")
                time.sleep(2)
                print("What would you like to do?")
                time.sleep(2)
                UserInput = inputchecker()
                # User Input HOUSE EVENT
                if UserInput == 1:
                    # Possibilities in the house
                    Userchances = random.randint(1, 2)
                    print("You decided to go to another house.")
                    time.sleep(2)
                    # The player will get an item
                    if Userchances == 1:
                        new_item = house(Userchances, inventory)
                        inventory.append(new_item)
                    # The player will be attacked inside the house
                    else:
                        total_score += house(Userchances, inventory)
                    break
                # User Input CAVE EVENT
                if UserInput == 2:
                    if CAVE_EVENT == False:
                        print("You went to the cave again.")
                        time.sleep(2)
                        print("You went to the cave again, it was empty")
                        time.sleep(2)
                        print("You returned back to the field again.")
                        time.sleep(2)
                    else:
                        # Possiblilites in the cave
                        Userchances = random.randint(1, 5)
                        new_item = cave(Userchances)
                        inventory.append(new_item)
                        CAVE_EVENT = False
            print("Your current score is " + str(total_score))
            time.sleep(2)
            # The end of the journey
            break
        # ENDGAME and checking the score
        time.sleep(2)
        if total_score >= 3:
            print("You won the game with score" + str(total_score))
        elif total_score < 3 and total_score > 0:
            print("You close to winning with score " + str(total_score))
        else:
            print("You lost the game with total score of less than or equal 0")
        time.sleep(2)
        # Waiting for user respone wether play again or no
        print("GAME OVER")
        time.sleep(2)
        UserInput = input("Do you wish to play again? \n")
        time.sleep(2)
        while UserInput != "y" and UserInput != "n":
            UserInput = input("Please Enter y or n \n")
            time.sleep(2)
# Main Code


main()
time.sleep(2)
print("Thank you for playing the game!")
time.sleep(2)
