# MusiCLI - Command Line Music Player

MusiCLI is a simple and lightweight command-line music player written in Python using the `pygame` library. It allows you to organize and play your music collection directly from the terminal.

## Features

- Browse and play your music collection from the command line.
- Automatically retrieve album information from the provided music folder.
- Easily change the music folder path for your convenience.

## Installation

1. Clone this repository to your local machine: `git clone https://github.com/macintushar/MusiCLI.git`
2. Navigate to the project directory: `cd MusiCLI`
3. Install the `pygame` library: `pip install pygame`
4. Run the `MusiCLI.py` script: `python3 MusiCLI.py`


## Initial Setup

On the first run, MusiCLI will prompt you to provide the path to your music folder. This will be used as the source of your music collection. The path will be saved in the `musicli-config.txt` file for future reference.
It will also create a cache of all the paths for all files in the `musicli-cache.csv` file for faster loading.

## Usage

After the initial setup, MusiCLI will automatically use the configured music folder. To run the music player, execute the following command: `python3 MusiCLI.py`


MusiCLI will display a list of albums and songs in your music collection. Use the provided commands to navigate and play your music.

## Changing the Music Folder Path

To change the music folder path, simply edit the `musicli-config.txt` file in the project directory and replace the existing path with the new one. The next time you run MusiCLI, use option 4 in the app to `Reload the Cache` to use the updated files.

## Folder Structure

MusiCLI uses the Folder names as the Album names and the .flac or .mp3 files as the Songs. Make sure you  It is structured like:
```
├── Music Folder
|    ├── Album1
|    |   ├── Song1.flac
|    |   ├── Song2.mp3
|    |   ├── Song3.flac
|
|    ├── Album2
|    |   ├── Song1.flac
|    |   ├── Song2.mp3
|    |   ├── Song3.flac
```

## Dependencies

MusiCLI uses the following Python module:
- `os`: For file and directory operations.
- `pygame`: For audio playback and control.

## Contributions

Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
