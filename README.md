# MusiCLI - Command Line Music Player

MusiCLI is a simple and lightweight command-line music player written in Python using the `pygame` library. It allows you to organize and play your music collection directly from the terminal.

## Features

- Browse and play your music collection from the command line.
- Automatically retrieve album information from the provided music folder.
- Easily change the music folder path for your convenience.

## Installation

1. Clone this repository to your local machine: git clone https://github.com/macintushar/MusiCLI.git 
2. Navigate to the project directory: cd MusiCLI
3. Install the `pygame` library: pip install pygame
4. Run the `MusiCLI.py` script: python3 MusiCLI.py


## Initial Setup

On the first run, MusiCLI will prompt you to provide the path to your music folder. This will be used as the source of your music collection. The path will be saved in the `config.txt` file for future reference.

## Usage

After the initial setup, MusiCLI will automatically use the configured music folder. To run the music player, execute the following command: python3 MusiCLI.py


MusiCLI will display a list of albums and songs in your music collection. Use the provided commands to navigate and play your music.

## Changing the Music Folder Path

To change the music folder path, simply edit the `config.txt` file in the project directory and replace the existing path with the new one. The next time you run MusiCLI, it will use the updated path.

## Dependencies

MusiCLI uses the following Python module:
- `os`: For file and directory operations.
- `pygame`: For audio playback and control.

## Contributions

Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).









