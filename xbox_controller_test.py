import pygame
import sys

# Initialize pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

# Ensure at least one joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected")
    sys.exit()

# Get the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Define button and axis names
button_names = [
    "A", "B", "X", "Y",         # 0, 1, 2, 3
    "LB", "RB",                 # 4, 5
    "Back", "Start",            # 6, 7
    "Guide",                    # 8
    "Left Stick", "Right Stick" # 9, 10
]

axis_names = [
    "Left Stick X", "Left Stick Y", # 0, 1
    "Right Stick X", "Right Stick Y", # 2, 3
    "LT", "RT"                      # 4, 5
]

hat_names = [
    "D-pad" # 0
]

print(f"Joystick name: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

# Function to print axis movement details
def print_axis_movement():
    for i in range(joystick.get_numaxes()):
        axis = joystick.get_axis(i)
        axis_name = axis_names[i] if i < len(axis_names) else f"Unknown axis {i}"
        if abs(axis) > 0.1:  # Deadzone threshold to avoid noise
            print(f"{axis_name} value: {axis:.3f}")

# Function to print button press/release details
def print_button_details(pressed):
    for i in range(joystick.get_numbuttons()):
        if joystick.get_button(i) == pressed:
            button_name = button_names[i] if i < len(button_names) else f"Unknown button {i}"
            state = "pressed" if pressed else "released"
            print(f"Button {button_name} {state}")

# Function to print D-pad movement details
def print_hat_details():
    for i in range(joystick.get_numhats()):
        hat = joystick.get_hat(i)
        hat_name = hat_names[i] if i < len(hat_names) else f"Unknown hat {i}"
        directions = {
            (0, 1): "up",
            (0, -1): "down",
            (1, 0): "right",
            (-1, 0): "left",
            (1, 1): "up-right",
            (-1, 1): "up-left",
            (1, -1): "down-right",
            (-1, -1): "down-left",
            (0, 0): "center"
        }
        direction = directions.get(hat, f"unknown {hat}")
        print(f"{hat_name} moved {direction}")

# Main loop
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print_axis_movement()

            elif event.type == pygame.JOYBUTTONDOWN:
                print_button_details(True)

            elif event.type == pygame.JOYBUTTONUP:
                print_button_details(False)

            elif event.type == pygame.JOYHATMOTION:
                print_hat_details()

except KeyboardInterrupt:
    print("Exited by user")
finally:
    pygame.quit()
