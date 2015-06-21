# GuessWord
A simple python2 game similar to hangman. Just a project I've been working on as I learn more and more python.

# Dependencies
The following are what I needed to install on my Arch machine:
* python2-configargparse
* python2-requests (only if you don't have `random.txt`)
* ~~python2-termcolor~~ Switched to ASCII escape sequences for color
* simple-cipher module to use guessword_enc

However, it's possible you may be missing things. YMMV

# TODO
* ✓ ~~Allow color to be turned off~~
* Add a cheat mode which runs purposely exploitable code
* Support for multiple words
* Get dictionary definitions for words from random.txt
* Create an ncurses version
* Add extra dictionary files and store them in a format other than plaintext so you can't cheat
* Improve this game so much that it becomes an operating system
