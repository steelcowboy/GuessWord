# GuessWord
A simple python*3* game similar to hangman. Just a project I've been working on as I learn more and more python.

# Dependencies
The following are what I needed to install on my Arch machine:
* python-configargparse
* python-requests (optional -- only if you don't have `random.txt`)
* python-termcolor (optional -- can also use ASCI escape sequences for color)

However, it's possible you may be missing things. YMMV

# Tools
Included in the tools folder are two scripts to encode or decode a dictionary file. Usage: `./tools/{en/de}code file.txt`

# TODO
* ✓ Allow color to be turned off
* Add a cheat mode which runs purposely exploitable code
* ✓ Support for multiple words -- and words with special characters, such as apostrophes!
* Get dictionary definitions for words from random.txt
* ✓ Create an ncurses version
  * May also make a urwid version, depending on if I feel like I'll ever use urwid again
* ~~Add extra dictionary files and store them in a format other than plaintext so you can't cheat~~
  * Encoding the words in hex to discourage cheating
* Improve this game so much that it becomes an operating system


