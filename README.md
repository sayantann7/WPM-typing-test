# WPM Typing Test - README

## Overview
This Python project is a simple terminal-based typing speed test. It measures your **Words Per Minute (WPM)** as you type a random quote. The program provides visual feedback for correct and incorrect keystrokes and gives you the opportunity to retake the test or exit at the end.

## Features
- Displays a random quote fetched from an online API.
- Measures typing speed in **Words Per Minute (WPM)**.
- Provides feedback on correct (green) and incorrect (red) letters while typing.
- Allows the user to restart the test or exit after completing a test.
- Uses the `curses` library for a clean, interactive terminal interface.

## Requirements
To run this project, you need:
- Python 3.x
- `curses` module (built-in with most Python installations)
- `requests` module (for fetching random quotes from an API)

You can install the `requests` module using:
```
pip install requests
```

## How to Run
1. Clone or download the project files.
2. Install the required modules.
3. Run the Python script using the command:
   ```
   python main.py
   ```
4. The game starts with a welcome screen. Press any key to begin the typing test.

## Controls
- **Typing**: Type the text shown on the screen.
- **Backspace**: Correct mistakes by deleting the last typed character.
- **ESC**: Press to exit the game at any time.
- **Restart**: After completing the test, press any key to restart or press ESC to exit.

## How it Works
1. **Start Screen**: The program displays a welcome message. Press any key to start the test.
2. **Typing Test**: A random quote from the [Quotable API](https://api.quotable.io) is displayed. As you type, correct letters are shown in green, and incorrect ones are shown in red. The program calculates WPM dynamically based on your typing speed.
3. **Completion**: Once you've typed the entire quote correctly, the game will show a completion message and give you the option to restart or exit.

## Code Breakdown
- **start_screen()**: Displays the welcome screen before starting the test.
- **display_text()**: Renders the target text and highlights correct/incorrect letters as the user types. Also displays the current WPM.
- **wpm_test()**: Main logic for the typing test. Handles text input, WPM calculation, and monitors when the test is completed.
- **main()**: Initializes color pairs and handles the game loop, including starting the test, displaying the results, and restarting or exiting based on user input.

## Example Output
```
Welcome to WPM Typing Test!
Press any key to begin!
```

Once the test begins, it shows:
```
The quick brown fox jumps over the lazy dog.
WPM = 65
```

Correctly typed characters will appear in green, and incorrect ones in red.

## Notes
- The program runs in the terminal using `curses`, so make sure to use a terminal environment that supports this library (Linux, macOS, or Windows Subsystem for Linux).
- Make sure your terminal window is large enough to accommodate the display text.
