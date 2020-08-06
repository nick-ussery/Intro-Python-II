from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room
player = Player("outside")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def north():
    if(room[player.location].n_to != ""):
        print("  Player moves North")
        player.location = room[player.location].n_to
        # print("player location ", room[player.location])
        # print("room n to: ", room[player.location].n_to)


def south():
    if(room[player.location].s_to != ""):
        print("  Player moves South")
        player.location = room[player.location].s_to


def east():
    if(room[player.location].e_to != ""):
        print("  Player moves East")
        player.location = room[player.location].e_to


def west():
    if(room[player.location].w_to != ""):
        print("  Player moves West")
        player.location = room[player.location].w_to


x = ''
while x != "q":
    print(room[player.location].name)
    print(room[player.location].description)
    # print(room[player.location])
    # print("Room keys", room.keys())

    x = input(">")
    if(len(x) == 0):
        print("")
    elif(x == "n"):
        north()
    elif(x == "s"):
        south()
    elif(x == "e"):
        east()
    elif(x == "w"):
        west()
