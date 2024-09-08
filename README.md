# WPM Typing Test

This is a terminal-based Words Per Minute (WPM) typing test built using Python and the `curses` library. The game presents random sentences from a file, and the user types them out as quickly and accurately as possible. The WPM (Words Per Minute) is displayed in real-time, and the program handles errors and backspaces.

## Features
- **Random sentence selection**: Each test presents a random sentence from a `.txt` file.
- **Real-time WPM calculation**: Your WPM is calculated in real-time as you type.
- **Error highlighting**: Correct characters are shown in green, while incorrect characters are shown in red.
- **Multiple runs**: After completing a test, the user can choose to play again or exit.

## Requirements
- Python 3.x
- The `curses` module (included in most Python installations)

## Setup

1. Clone or download the repository to your local machine.
2. Create a `sentences.txt` file containing a list of sentences, with one sentence per line. For example:
    ```
    The quick brown fox jumps over the lazy dog.
    A journey of a thousand miles begins with a single step.
    ```
3. Run the program using Python:

    ```bash
    python wpm_typing_test.py
    ```

## Usage

- Upon running the script, you'll be greeted with a welcome screen.
- Press any key to begin the typing test.
- As you type, your WPM will be shown in the terminal.
- Correctly typed characters will be displayed in green, and incorrect ones will be displayed in red.
- Press `ESC` at any time to quit.

## Controls
- **Typing**: Start typing to match the given sentence.
- **Backspace**: Press backspace to correct mistakes.
- **Escape (ESC)**: Quit the game at any time.
- **After Completion**: Press any key to play again, or `ESC` to exit.

## Customization

You can customize the following parts of the game:
- **Sentences**: Edit the `sentences.txt` file to include your own sentences.
- **Color Scheme**: Modify the `curses.init_pair()` values to change text colors.