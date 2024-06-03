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
    "A", "B", "X", "Y",
    "LB", "RB", "Back", "Start",
    "Guide", "Left Stick", "Right Stick"
]

axis_names = [
    "Left Stick X", "Left Stick Y",
    "Right Stick X", "Right Stick Y",
    "LT", "RT"
]

hat_names = [
    "D-pad"
]

print(f"Joystick name: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

# Main loop
try:
    while True:
      
        for event in pygame.event.get():
            print("???????????",event)
            
            if event.type == pygame.JOYAXISMOTION:
                for i in range(joystick.get_numaxes()):
                    axis = joystick.get_axis(i)
                    if abs(axis) > 0.1:  # Deadzone threshold
                        print(f"{axis_names[i]} value: {axis:.3f}")

            elif event.type == pygame.JOYBUTTONDOWN:
                for i in range(joystick.get_numbuttons()):
                    if joystick.get_button(i):
                        print(f"Button {button_names[i]} pressed")

            elif event.type == pygame.JOYBUTTONUP:
                for i in range(joystick.get_numbuttons()):
                    if not joystick.get_button(i):
                        print(f"Button {button_names[i]} released")

            elif event.type == pygame.JOYHATMOTION:
                for i in range(joystick.get_numhats()):
                    hat = joystick.get_hat(i)
                    print(f"{hat_names[i]} value: {hat}")

except KeyboardInterrupt:
    print("Exited by user")
finally:
    pygame.quit()
