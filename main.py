from nltk.corpus import words
import random

word_list = words.words()
word = random.choice(word_list)
while len(word) < 2:
    word = random.choice(word_list)

print('''
Hangman: A simple game where you guess letters until you can get the whole word.
You can guess the whole word at any point, but if you are wrong you will lose!
''')

correct_letters_guessed = []
false_letters_guessed = []

guess = ''
tries_left = 12

word_as_list = word.split()

while guess != word:
    if tries_left < 1:
        print(f'You ran out of tries, you lose! The word was {word}.')

    partial_word_list = []
    partial_word = ''
    for letter in word:
        if letter in correct_letters_guessed:
            partial_word_list.append(letter)
        else:
            partial_word_list.append('_')
    for character in partial_word_list:
        partial_word += character
    print(f'\nWord: {partial_word}\n'
          f'False letters guessed: {false_letters_guessed}\n'
          f'Tries left: {tries_left}')

    cur_guess = input('What is your guess: ')
    if len(cur_guess) > 1:
        if cur_guess == word:
            print(f'You are correct, you win! The word was, as you guessed, {word}')
            break
        else:
            print(f'You are incorrect, you lose. The word was {word}')
            break
    else:
        if cur_guess in correct_letters_guessed or cur_guess in false_letters_guessed:
            print(f'You already guessed {cur_guess}, try again!')
            continue
        elif cur_guess in word:
            if len(cur_guess) == len(correct_letters_guessed):
                print(f'You guessed all the letters! The word was {word}')

            correct_letters_guessed.append(cur_guess)
            print('Correct!, that letter is in the word')
        else:
            false_letters_guessed.append(cur_guess)
            print(f'Nope! Try another letter, you have {tries_left} tries left. ')
            tries_left -= 1
