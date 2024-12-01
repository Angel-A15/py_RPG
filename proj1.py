# we want to start off by identifying the player with an input
name: str = input("Hey type your name:")

print("Hello",name, "welcome to my game!") #This will grab the input from variable name and reference it into the string
# we need to ask if they want to play

should_we_play = input("Do you want to play?").lower()
    # Varied on the answer, our game will start or end

    #Will define is input is the desired answer to start game
if should_we_play == "y" or should_we_play == "yes":
    print("We are going to play!!")

    item1 = input("Do you want to carry a weapon? (yes/no) ").lower()

    if item1 == 'yes' or 'y':

        weapon = input('Select a weapon: (sword/crossbow)').lower()

        if weapon == "sword":
            print("Sword was added to inventory.")

        elif weapon == "crossbow":
            print("Crossbow was added to inventory.")

        else:
            print("Please select an option.")
    elif item1 == 'no' or 'n':
        print("You start your path withouth a weapon.")
    else:
        print("Please select an option.")

 

    # options come next
    direction = input("Do you want to go left or right? (left/right)").lower()

    if direction == "l" or "left":
        print("Left we go! Unexpectedly, you fall off a cliff...")
        print("THE END")
    elif direction == 'right'or 'r':

        print('Right we go! You see a castle over the horizon, but a river seperates your path...')
        river = input("Do you wish to swim across or keep looking for another way across? (swim/search)").lower
        
        if river == "swim":
            print("You start to swim...")
            print("You are about to reach the other side!")
            print("Although...an alligator lunges at you!")
            print("You die! THE END")
        else:
            print("You take a look at your surrounding and notice a boat!")
            print("You raft across the river and get to the otherside.")
            print("You get to the castle and fall head over heals for a maiden on the top corner of the castle tower.")
    else:
        ("Sorry not a vallid response, try again.")


    # #otherwise, the game will end
else:
    print("We are not going to play...goodbye!")