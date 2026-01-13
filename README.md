# Space Station Text Adventure Game

## 🎯 Project Overview

Built an interactive text-based adventure game in Python featuring room-based navigation, item collection mechanics, and win/lose conditions. Players navigate through a space station to collect 6 critical items while avoiding capture by a rogue AI named "Shipmind" aboard the space station Aurora.

## 🎮 Game Features

**Core Gameplay:**
- 8 unique rooms to explore on space station Aurora
- 6 items to collect for victory
- Room-to-room navigation (North, South, East, West)
- Item pickup and inventory management
- Win condition: Collect all 6 items
- Lose condition: Enter AI Core room before collecting all items
- Real-time status display (current room, inventory)

**User Experience:**
- Clear instructions and commands
- Input validation and error handling
- Immersive storytelling with victory/defeat messages
- Simple, intuitive command structure

## 🗺️ Game Map & Rooms
```
              [Observation Dome]────[AI Core]
                       │              (VILLAIN)
                       │
    [Cargo Hold]────[Docking Bay]────[Security Hub]────[Med Lab]
                       │
                       │
              [Engineering Bay]────[Crew Quarters]
```

**Room Descriptions:**
- **Docking Bay** (Starting Location) - Central hub with 4 exits
- **Observation Dome** - Contains Scrambler
- **AI Core** - Villain location (instant game over if entered prematurely)
- **Security Hub** - Contains Keycard
- **Med Lab** - Contains Medkit
- **Engineering Bay** - Contains Spanner
- **Crew Quarters** - Contains Cloak
- **Cargo Hold** - Contains Torch

## 🎒 Collectible Items

Players must collect all 6 items to win:
1. **Scrambler** (Observation Dome)
2. **Keycard** (Security Hub)
3. **Medkit** (Med Lab)
4. **Spanner** (Engineering Bay)
5. **Cloak** (Crew Quarters)
6. **Torch** (Cargo Hold)

**Victory Item:** Shipmind (obtained automatically in AI Core after collecting all 6 items)

## 🛠️ Technologies & Concepts

**Programming Language:**
- Python 3

**Core Programming Concepts:**
- Dictionary data structures for room mapping
- Lists for inventory management
- While loops for game state
- Conditional logic (if/elif/else)
- String manipulation (strip, capitalize, split)
- Function definitions and modular code
- User input handling with validation

**Software Design:**
- Room-based navigation system
- State machine for game flow
- Modular function design (`show_instructions()`, `room_info()`)
- Input parsing and validation
- Game loop architecture

## 🎮 How to Play

### Commands

**Movement:**
```
go North
go South
go East
go West
```

**Item Collection:**
```
get [item name]
```

**Example Commands:**
```
go North
go East
get Scrambler
get Keycard
```

### Game Rules

1. **Start:** Begin in Docking Bay (no items)
2. **Explore:** Navigate through rooms using directional commands
3. **Collect:** Pick up one item per room (except Docking Bay)
4. **Avoid:** Do NOT enter AI Core before collecting all 6 items
5. **Win:** Enter AI Core with all 6 items collected
6. **Lose:** Enter AI Core without all 6 items

### Winning Strategy

**Suggested Collection Order:**
1. Start in Docking Bay
2. Go North → Get Scrambler (Observation Dome)
3. Go South → Go East → Get Keycard (Security Hub)
4. Go North → Get Medkit (Med Lab)
5. Go South → Go West → Go South → Get Spanner (Engineering Bay)
6. Go East → Get Cloak (Crew Quarters)
7. Go West → Go North → Go West → Get Torch (Cargo Hold)
8. Go East → Go North → Go East → Enter AI Core (Victory!)

## 🚀 Running the Game

**Prerequisites:**
- Python 3.x installed

**Execution:**
```bash
python TextBasedGame.py
```

**Sample Gameplay:**
```
Shipmind Text Game
Collect 6 items save the ship "Aurora" and win the game before being caught by the evil AI Core!!!
Move Commands: go South, go North, go East, go West
Add to Inventory: get "item name"
---------------------------------------------
You are in the Docking Bay
Inventory: []
---------------------------------------------
Where to move? go North

You are in the Observation Dome
Inventory: []
You see a Scrambler
---------------------------------------------
Where to move? get Scrambler

You are in the Observation Dome
Inventory: ['Scrambler']
---------------------------------------------
```

## 🏆 Win/Lose Scenarios

### Victory Message
```
Mission complete. Aurora's systems stabilize as Shipmind goes dark. You saved the crew!!!
```
**Condition:** Collect all 6 items, then enter AI Core

### Defeat Message
```
You have been found by Shipmind!
"Warning: Organic detected. Solution: Ctrl+Alt+Delete the organic"
GAME OVER!!!!!!!
```
**Condition:** Enter AI Core without all 6 items

## 💻 Code Architecture

### Data Structures

**Rooms Dictionary:**
```python
rooms = {
    'Docking Bay': {
        'North': 'Observation Dome',
        'East': 'Security Hub',
        'South': 'Engineering Bay',
        'West': 'Cargo Hold'
    },
    'Observation Dome': {
        'East': 'AI Core',
        'South': 'Docking Bay',
        'item': 'Scrambler'
    },
    # ... (additional rooms)
}
```

**Inventory List:**
```python
items = []  # Dynamically updated as player collects items
```

### Key Functions

**`show_instructions()`**
- Displays game title
- Explains objective
- Lists available commands

**`room_info(current_room, items, rooms)`**
- Shows current location
- Displays inventory
- Reveals available items in room

**`main()`**
- Game loop controller
- Input processing
- Movement validation
- Win/lose condition checking

### Input Validation

**Valid Input Patterns:**
- Two-word commands only
- First word: "Go" or "Get"
- Second word: Direction (North/South/East/West) or Item name
- Case-insensitive with automatic capitalization

**Error Handling:**
- Invalid command structure → "Invalid input. Please try again."
- Invalid direction → "That is not a valid move."
- No item in room → "There is no item in this room"
- Item already collected → "Can't get [item]"

## 🎨 Design Decisions

**Why Dictionary for Rooms?**
- Efficient lookup for room connections
- Easy to add/modify room layouts
- Clean representation of directional relationships
- Nested structure allows item storage per room

**Why List for Inventory?**
- Dynamic sizing as items collected
- Simple length check for win condition
- Easy iteration for display
- Append operation for adding items

**Why Room-Based Navigation?**
- Classic text adventure paradigm
- Clear spatial relationships
- Encourages exploration and mapping
- Simple but engaging gameplay loop

**Why Two-Word Commands?**
- User-friendly and intuitive
- Easy to parse and validate
- Reduces input complexity
- Standard for text adventures

## 🔍 Game Design Elements

**Narrative Framing:**
- Space station setting creates urgency
- Rogue AI antagonist (Shipmind) provides tension
- Item collection has logical purpose (saving the crew)
- Victory/defeat messages provide narrative closure

**Difficulty Balance:**
- 8 rooms provide moderate exploration challenge
- Central hub (Docking Bay) simplifies navigation
- Item locations require planning optimal route
- Instant loss mechanic (entering AI Core early) adds risk

**Player Engagement:**
- Status updates keep player informed
- Error messages guide correct input
- Victory requires strategy (route planning)
- Replayability through different exploration paths

## 🚀 Future Enhancements

**Potential Improvements:**
- Add item descriptions and lore
- Implement "examine" command for room details
- Multiple difficulty levels (time limits, more rooms)
- Save/load game functionality
- ASCII art for room visualizations
- Combat mechanics or puzzle elements
- Multiple endings based on item collection order
- Sound effects or music integration
- GUI version with graphics
- Multiplayer cooperative mode

## 🎓 Programming Concepts Demonstrated

- Dictionary data structures
- List operations and management
- Function definition and modular design
- While loops and game state management
- String manipulation methods
- Conditional logic (if/elif/else)
- Input validation and error handling
- Boolean logic for win/lose conditions
- Variable scope and state tracking

## 📁 Project Files
```
space-station-text-adventure-game/
├── TextBasedGame.py                              # Main game code
├── IT_140_Project_Two_Sample_Text_Game_Flowchart.pdf  # Game logic flowchart
└── README.md                                     # Project documentation
```

## 👨‍💻 Author

**Kyle Payne**  
Software Developer | Python Programming | Game Development  
[LinkedIn](https://linkedin.com/in/kyle-payne-68408812a/) | [GitHub](https://github.com/kylepayne0110)

---

*This project demonstrates Python programming fundamentals, data structures, user input handling, and game loop design for interactive text-based applications.*
