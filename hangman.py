import random

def prepare_table():
    word = generate_word()
    snake = '-'*(len(word))
    guested_letters = set()
    print('H A N G M A N')
    return [word,snake,guested_letters]

def generate_word():
    words = ['python','java', 'kotlin', 'javascript']
    index = random.randrange(0,len(words))
    return words[index]
   
def events_maker(user_letter,word,hangman_proces,snake):
    if user_letter in word and user_letter not in snake:
        letter_counter = word.count(user_letter)
        last_index = -1
        while letter_counter > 0 :
            letter_counter -= 1
            letter_index = word.index(user_letter,last_index + 1)
            last_index = letter_index
            if letter_index != 0:
                snake = '{0}{1}{2}'.format(snake[0:(letter_index)],user_letter,snake[(letter_index + 1):])
            else:
                snake = '{0}{1}'.format(user_letter,snake[(letter_index + 1):])
    elif user_letter in snake:
        hangman_proces += 1
        print('No improvements')        
    else:
        hangman_proces += 1
        print("That letter doesn't appear in the word")
    return [snake,hangman_proces]
    

def judge(word,snake,hangman_proces):
    if hangman_proces > 7:
        print('You lost!')
        return True
    elif word == snake:
        print(f'{snake}\nYou guessed the word!\nYou survived!')
        return True
    else:
        return False

def checker(user_letter,guested_letters):
    if user_letter in guested_letters:
        print("You've already guessed this letter")
        return False
    elif len(user_letter) != 1:
        print('You should input a single letter')
        return False
    elif ord(user_letter) < 97 or ord(user_letter) > 122:
        print('Please enter a lowercase English letter')
        return False
    else:
        return True

def play_chooser():
    decision = ''
    while decision != 'play' and decision != 'exit':
        decision = input('Type "play" to play the game, "exit" to quit: ')
    else:
        if decision == 'play':
            return False
        elif decision == 'exit' :
            return True

def main():
    first_items = prepare_table()
    snake = first_items[1]
    word = first_items[0]
    guested_letters = first_items[2]
    hangman_proces = 0
    end = False
    play_choice = play_chooser()
    while play_choice == False:
        while end == False:
            print(f'\n{snake}')
            user_letter = input('Input a letter: ')
            if checker(user_letter,guested_letters):
                events = events_maker(user_letter,word,hangman_proces,snake)
                guested_letters.add(user_letter)
                snake = events[0]
                hangman_proces = events[1]
                end = judge(word,snake,hangman_proces)
        play_choice = play_chooser()
    
main()