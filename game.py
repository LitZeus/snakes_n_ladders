import random
import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Snake and Ladders")
window.resizable(False, False)

# Create the canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Define the snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Set the player's initial position
player_position = 0

# Variable to store the previous player position
previous_position = None

# Function to draw the board
def draw_board():
    canvas.delete("all")

    # Draw the spaces
    for i in range(10):
        for j in range(10):
            x1 = j * 40
            y1 = (9 - i) * 40
            x2 = x1 + 40
            y2 = y1 + 40
            space_number = i * 10 + j + 1  # Calculate the space number
            canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(space_number))

    # Draw the snakes
    for start, end in snakes.items():
        start_row = 9 - (start - 1) // 10
        start_col = (start - 1) % 10
        end_row = 9 - (end - 1) // 10
        end_col = (end - 1) % 10

        canvas.create_line(
            (start_col + 0.5) * 40,
            (9 - start_row + 0.5) * 40,
            (end_col + 0.5) * 40,
            (9 - end_row + 0.5) * 40,
            fill="red",
            width=3,
        )

    # Draw the ladders
    for start, end in ladders.items():
        start_row = 9 - (start - 1) // 10
        start_col = (start - 1) % 10
        end_row = 9 - (end - 1) // 10
        end_col = (end - 1) % 10

        canvas.create_line(
            (start_col + 0.5) * 40,
            (9 - start_row + 0.5) * 40,
            (end_col + 0.5) * 40,
            (9 - end_row + 0.5) * 40,
            fill="green",
            width=3,
        )

    # Draw the player
    row = 9 - (player_position // 10)
    col = (player_position % 10)
    x1 = col * 40
    y1 = row * 40
    x2 = x1 + 40
    y2 = y1 + 40
    canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")

    # Update the canvas
    canvas.update()

# Function to check for snakes and ladders
def check_snakes_ladders(position):
    if position in snakes:
        print("Oops! You got swallowed by a snake!")
        return snakes[position] - 1
    elif position in ladders:
        print("Hooray! You found a ladder!")
        return ladders[position] - 1
    elif position == 99:
        messagebox.showinfo("Game Over", "Congratulations! You won the game!")
        window.quit()
    else:
        return position

# Function to handle key press events
def handle_keypress(event):
    if event.keysym == "space":
        roll_dice()

# Function to roll the dice
def roll_dice():
    roll = random.randint(1, 6)
    print("You rolled a", roll)
    move_player(roll)

# Function to move the player
def move_player(roll):
    global player_position, previous_position

    # Store the previous player position
    previous_position = player_position

    new_position = player_position + roll
    if new_position > 99:
        new_position = 99

    while player_position < new_position:
        player_position += 1
        draw_board()
        canvas.after(200)  # Delay between each space movement

    player_position = check_snakes_ladders(player_position)
    draw_board()

def undo_move():
    global player_position, previous_position

    # Check if there is a previous position to undo
    if previous_position is not None:
        player_position = previous_position
        previous_position = None

    draw_board()

# Function to handle key press events
def handle_keypress(event):
    if event.keysym == "space":
        roll_dice()
    elif event.keysym == "r":
        undo_move()

# Bind the key press event to the window
window.bind("<KeyPress>", handle_keypress)
window.focus_set()

# Draw the initial board
draw_board()

# Start the main event loop
window.mainloop()
