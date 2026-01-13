#Kyle Payne

# room dictionary associated with map
rooms  = {
    'Docking Bay': {'North': 'Observation Dome', 'East': 'Security Hub', 'South': 'Engineering Bay', 'West': 'Cargo Hold'},
    'Observation Dome': {'East': 'AI Core', 'South': 'Docking Bay', 'item': 'Scrambler'},
    'AI Core': {'West': 'Observation Dome', 'item': 'Shipmind'},
    'Security Hub': {'North': 'Med Lab', 'West': 'Docking Bay', 'item': 'Keycard'},
    'Med Lab': {'South': 'Security Hub', 'item': 'Medkit'},
    'Engineering Bay': {'North': 'Docking Bay', 'East': 'Crew Quarters', 'item': 'Spanner'},
    'Crew Quarters': {'West': 'Engineering Bay', 'item': 'Cloak'},
    'Cargo Hold': {'East': 'Docking Bay', 'item': 'Torch'}
}
# initialize items list, when len() == 6, user has won
items = []

# initialize current room variable and starting room
current_room = 'Docking Bay'

# define show instructions function
def show_instructions():
    print('Shipmind Text Game')
    print('Collect 6 items save the ship "Aurora" and win the game before being caught by the evil AI Core!!!')
    print('Move Commands: go South, go North, go East, go West')
    print('Add to Inventory: get "item name"')
    print('---------------------------------------------')

    # define show room information function
def room_info(current_room, items, rooms):
    print(f'You are in the {current_room}')
    print(f'Inventory: {items}')
    if current_room != 'Docking Bay' and current_room != 'AI Core':
        if rooms[current_room]['item'] not in items:
            print(f'You see a {rooms[current_room]["item"]}')
    print('---------------------------------------------')

show_instructions()

def main():

    current_room = 'Docking Bay'

    #begin main loop
    while True:

        room_info(current_room, items, rooms)

        #get user input and Strip and Capitalize it
        user_input = input('Where to move?').strip().capitalize()

        #split words from user
        words = user_input.split()

        #make sure length of input is 2 words
        if len(words) != 2:
            print('Invalid input. Please try again.')
            continue

        #check if first word is either go or get
        if words[0].capitalize() != 'Go' and words[0].capitalize() != 'Get':
            print('Invalid input. Please try again. You can use go South, go North, go East, go West or get "item name')
            continue

        #if go check direction
        if words[0].capitalize() == 'Go':
            #check if you can go in that direction
            if words[1].capitalize() in rooms[current_room]:
                #change room
                current_room = rooms[current_room][words[1].capitalize()]

                #if in villian room then game is over
                if current_room == 'AI Core':
                    print('You have been found by Shipmind!')
                    print('"Warning: Organic detected. Solution: Ctrl+Alt+Delete the organic"')
                    print('GAME OVER!!!!!!!')
                    break
            else:
                print('That is not a valid move. You can go North, go East, go South, or  go West, or exit')
                continue

        elif words[0].capitalize() == 'Get':
            #if room is Docking Bay cant get the item
            if current_room == 'Docking Bay':
                print('There is no item in this room')

            #does current room have an item or is it in inventory?
            elif rooms[current_room]['item'] in items:
                print(f'Cant get {words[1]}')
            #if item is not in possible items then say cant do it

            else:
                items.append(words[1].capitalize())

        #if all items are collected end game
        if len(items) == 6:
            print('Mission complete. Aurora’s systems stabilize as Shipmind goes dark. You saved the crew!!!')
            break

# call main function
main()
