# Joystick Input Reader

This Python script uses the `pygame` library to read and print joystick input details such as axis movements, button presses/releases, and D-pad (hat) movements. 

## Requirements

- Python 3.x
- pygame library

## Installation

1. Ensure you have Python 3 installed. You can download it from the [official Python website](https://www.python.org/).

2. Install the `pygame` library using pip:

    ```sh
    pip install pygame
    ```

## Usage

1. Connect your joystick to your computer.

2. Save the script to a file, for example, `joystick_reader.py`.

3. Run the script:

    ```sh
    python joystick_reader.py
    ```

4. The script will print the joystick's name and the number of axes, buttons, and hats it has.

5. It will then continuously monitor and print details about axis movements, button presses/releases, and D-pad movements. The script uses a deadzone threshold of `0.1` to filter out minor noise in axis movements.

6. To exit the script, press `Ctrl+C` in the terminal.

## Script Details

- **Joystick Initialization:**
  - The script initializes pygame and the joystick.
  - It checks if at least one joystick is connected and exits if none are found.
  - It prints the joystick's name and the number of axes, buttons, and hats.

- **Event Handling:**
  - The script enters a loop where it processes events.
  - For `JOYAXISMOTION` events, it prints the value of the axis that moved.
  - For `JOYBUTTONDOWN` and `JOYBUTTONUP` events, it prints the button that was pressed or released.
  - For `JOYHATMOTION` events, it prints the direction of the D-pad movement.

- **Button and Axis Names:**
  - The script uses predefined lists for button, axis, and hat names. These can be customized as needed.

## Example Output



Joystick name: Xbox 360 Controller
Number of axes: 6
Number of buttons: 11
Number of hats: 1
Left Stick X value: 0.235
Button A pressed
D-pad moved up



## Notes

- The script uses a deadzone threshold of `0.1` for axis movements to avoid printing small, unintentional movements.
- Customize the `button_names`, `axis_names`, and `hat_names` lists to match your joystick's configuration if necessary.

## License

This project is licensed under the MIT License.
