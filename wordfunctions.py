import random, imp, string
from os.path import exists

def get_rand():
    if exists("random.txt"):
        dict_file = "random.txt"
        # Open the file then make a list of all the lines       
        hang_list = open(dict_file).read().splitlines()
        # Remove any blank lines    
        hang_list = list(filter(None, hang_list))
        word = random.choice(hang_list)
        word = bytes.fromhex(word).decode('utf-8').lower()

    else:
        try:
            imp.find_module('requests')
        except ImportError:
            return None

        import requests
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = requests.get(word_site)
        words = response.content.splitlines()
        word = random.choice(words).lower()
    return word

def get_dict(dictionary):
    dict_file = dictionary
    hang_list = open(dict_file).read().splitlines()
    hang_list = list(filter(None, hang_list))
    word = random.choice(hang_list)
    word = bytes.fromhex(word).decode('utf-8').lower()
    return word

def get_tries(level):
    if level:
        tries = 20 - level * 5
    else:
        tries = 15
    return tries

def gen_blank_word(word):
    blank_word = ["_"] * len(word)
    for x in range(0, len(word)):
        if word[x] not in string.ascii_letters:
            blank_word[x] = word[x]
    return blank_word


def get_msg(args):
    try:
        imp.find_module('termcolor')
        found = True
    except ImportError:
        found = False

    messages = {
            "correct": "Correct!",
            "incorrect": "Incorrect. You have %d tries left.",
            "win": "You won! Good job! ",
            "lose": "You lose! ",
            "err_letter": "Please enter only letters.",
            "err_one": "Please enter only one character.",
            "err_guess": "That letter has already been guessed.",
            "word": "The word was \"%s\""
        }

    if args:
        class msgs:    
            correct = messages["correct"]
            incorrect = messages["incorrect"]
            win = messages["win"] + messages["word"] 
            lose = messages["lose"] + messages["word"]
            err_letter = messages["err_letter"]
            err_one = messages["err_one"]
            err_guess = messages["err_guess"]

    elif found:    
        from termcolor import colored
        class msgs:
            correct = colored(messages["correct"], 'green', attrs=['bold'])
            incorrect = colored(messages["incorrect"], 'red', attrs=['bold'])
            win = colored(messages["win"], 'green', attrs=['bold']) + messages["word"]
            lose = colored(messages["lose"], 'red', attrs=['bold']) + messages["word"]
            err_letter = colored(messages["err_letter"], 'magenta', attrs=['bold'])
            err_one = colored(messages["err_one"], 'magenta', attrs=['bold'])
            err_guess = colored(messages["err_guess"], 'red', attrs=['bold'])

    else:
        class msgs:
            correct = "\033[1;32m" + messages["correct"] + "\033[0m"
            incorrect = "\033[1;31m" + messages["incorrect"] + "\033[0m"
            win = "\033[1;32m" + messages["win"] + "\033[0m" + messages["word"]
            lose = "\033[1;31m" + messages["lose"] +  "\033[0m" + messages["word"]
            err_letter = "\033[1;35m" + messages["err_letter"] + "\033[0m"
            err_one = "\033[1;35m" + messages["err_one"] + "\033[0m"
            err_guess = "\033[1;31m" + messages["err_guess"] + "\033[0m"
    
    return msgs
    

