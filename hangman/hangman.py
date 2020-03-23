# global variables
words_list = ['legend', 'great', 'cricket', 'bowler', 'batsman', 'googly']
f = open('words_list.txt')
words_list = f.read().splitlines()
f.close()
lives_remaining = 5
word = ''
all_guesses = []
correct_guesses = []
recent_guess = ''

import random

def decrement_lives():
    global lives_remaining
    lives_remaining = lives_remaining - 1
    print('letter does not exist')
    

def process_whole_word_guess():
    if(recent_guess == word):
        for letter in word:
            correct_guesses.append(letter)
        print('Congratulations!!! You guessed it right!!! ')
        return True
    else:
        decrement_lives()
    return False
        
    

def process_single_letter_guess():
    if(word.find(recent_guess) > -1):
        correct_guesses.append(recent_guess)
        for letter in word:
            if letter not in correct_guesses:
                return False
        # if we reached here, then word is guessed completely
        print('Congratulations!!! You guessed it right!!!')
        return True
    else:
        decrement_lives()
    return False
    

def process_user_input():
    if len(recent_guess) == 1:
        return process_single_letter_guess()
    else:
        return process_whole_word_guess()
    

def get_user_input():
    global all_guesses
    global recent_guess
    recent_guess = input('Guess a letter or whole word: ')
    all_guesses.append(recent_guess)

def print_remaining_lives():
    global lives_remaining
    print('Lives Remaining: '+ str(lives_remaining))

def print_word():
    display_word=''
    global word
    global correct_guesses
    
    for letter in word:
        if (letter in correct_guesses):
            display_word = display_word + letter.upper() + ' '
        else:
            display_word = display_word + '__ '
    print(display_word)
        

def select_random_word():
    global words_list
    global word
    word = random.choice(words_list)
    print_word()

def play():
    print('let us play; guess the word below:')
    select_random_word()
    print_remaining_lives()
    
    while (lives_remaining > 0):
        get_user_input()
        if process_user_input():
            print_word()
            exit()
        else:
            print_remaining_lives()
            print_word()
    
    if(lives_remaining == 0):
        print('You lost. Your guesses: ' + str(all_guesses))
        print('Correct Word: '+ word.upper())

play()