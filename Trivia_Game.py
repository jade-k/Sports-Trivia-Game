def display_title ():
    """print the title using the player's name"""
    print raw_input('What is your name?')
    print('Welcome to the Ultimate Sports Trivia Game',name)

def randomize_questions (questions):
    """Take all the questions and randomize them"""
    # Write code here
    print 'what?'

def display_question (question, answer, correct):
    """Display question. Get user answer. Return True if correct."""
    # Write code here
    # return True # FIXME
    answer = raw_input(question)
    if answer == (answer):
       print('correct!')
       # help from http://stackoverflow.com/questions/28491833/how-to-count-correct-answers-in-python
       correct = correct + 1
    else if :
       print('incorrect')
       incorrect = incorrect + 1
       
def display_results (answers, correct):
    """Display correct answers out of total answers"""
    grade = (correct * 100)/ 10)
    print ('Your scored',grade, 'percent')
    if (grade > 70)
       print('Better luck next time',name)

    if (grade < 80)
       print('Good Job', name,' You Are A Sports Genius')



### TESTS ###

def test_display_question ():
    print 'Result is:',display_question("What is your favorite color?","Blue")
    print 'Result is:',display_question("What is 3+7?",10)

def test_display_title ():
    #print raw_input('What is your name?')
    #print('Welcome to the tivia game',name)
    display_title()
    
def test_randomize_questions ():
    print('hi')
    print randomize_questions(['who are you?','what do you like?','why are you here?'])

def test_display_results ():
    display_results()

def test_all():    
    test_display_results()
    test_randomize_questions()
    test_display_results()
    test_display_title()

test_all()

###Final Code###

import random

def display_title ():
    """display the title using the players name"""
    print raw_input('What is your name?')
    print("Welcome to the Ultimate Sports Trivia Game',name'!')

def display_directions ():
    """display the directions using response given by player"""
    print raw_input ('Are you ready to begin?')
    if 'yes':
    print('Okay! In the game the only way to get a correct answer is to put answer in all CAPITAL LETTERS. Also no using sentences in your answer, only give the answer as its normal noun/pronoun. Lastly, no using the or a. Type anything below to begin.')
    else:
    print('Ready to begin yet?')


def randomize_questions ('Who has the most total touchdowns on the New England Patriots as of 2015?','Which country won the 2015 Womens FIFA World Cup?','What is the name of the penalty in hockey when a player hits another player with the hockey stick?','What is Bostons NBA basketball team?','In basketball what is a basket from the court halfline worth?','Which MLB baseball team won the World Series in 2013?','What is three strikes in a row in bowling called?','In track and field what is the event where someone jumps over obstacles while racing?', 'What is the name of Americas largest skaateboarding conversation?', 'What does NASCAR stand for?') 
item = random_choice
    """Takes the questions,  puts them into  a random order"""

def main_loop (questions):
    """Using questions, randomize questions, ask players questions, display results"""
    display_title = (raw_input, title)
    display_directions = raw_input
    randomize_questions = questions
    display_question = (questions, answers)
    display_results = answers
    play_game = (display_title, randomize_questions, display_questions, display_results)

answers = (correct, incorrect)
name = raw_input
item = random_choice
