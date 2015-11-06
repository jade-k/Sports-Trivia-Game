import random

def display_title (name):
    """print the title using the player's name"""
    name = raw_input('What is your name?')
    print('Welcome to the Ultimate Sports Trivia Game',name)
    
def display_question (question, answer, correct):
    """Display question. Get user answer. Return True if correct."""
    # Write code here
    # return True # FIXME
    answer = raw_input(question)
    # help from http://stackoverflow.com/questions/28491833/how-to-count-correct-answers-in-python
    if answer == (answer):
       print('correct!')
       # help from http://stackoverflow.com/questions/28491833/how-to-count-correct-answers-in-python
       correct = correct + 1
    else:
       print('incorrect')
       incorrect = incorrect + 1
       
def display_results (answers, correct):
    """Display correct answers out of total answers"""
   # grade = (correct * 100)/ 10)
   # print ('Your scored',grade, 'percent')
   # if (grade > 70)
      # print('Better luck next time',name)

   # if (grade < 80)
       # print('Good Job', name,' You Are A Sports Genius')


### TESTS ###

def test_display_question ():
    print 'Result is:',display_question("What is your favorite color?","Blue")
    print 'Result is:',display_question("What is 3+7?",10)

def test_display_title (name):
    #print raw_input('What is your name?')
    #print('Welcome to the tivia game',name)
    display_title(name)
    
def test_randomize_questions ():
    print('hi')
    print randomize_questions(['who are you?','what do you like?','why are you here?'])

def test_display_results (answers, correct): 
    display_results()

def test_all():    
    test_display_results()
    test_randomize_questions()
    test_display_results()
    test_display_title()

    test_all()

###Final Code###

import random

def display_title (): #Jade and Patrick
    """display the title using the players name"""
    print raw_input('What is your name?')
    print("Welcome to the Ultimate Sports Trivia Game',name'!")

def display_directions (): #Jade
    """display the directions using response given by player"""
    print raw_input ('Are you ready to begin?')
    if 'yes':
        print('Okay! In the game the only way to get a correct answer is to put answer in all CAPITAL LETTERS. Also no using sentences in your answer, only give the answer as its normal noun/pronoun. Lastly, no using the or a. Type anything below to begin.')
    else:
        print('Ready to begin yet?')


def display_question (question, answer, correct): #Patrick
    """Display question. Get user answer. Return True if correct."""
    # Write code here
    # return True # FIXME
    answer = raw_input(question)
    if answer == (a):
       print('correct!')
       # help from http://stackoverflow.com/questions/28491833/how-to-count-correct-answers-in-python
       correct = correct + 1
    else:  
       print('incorrect')
       incorrect = incorrect + 1

def random_shuffle (q_and_a): #Jade
    """Shuffles the questions,  puts them into  a random order"""

    return q_and_a

def display_results (answers, correct, incorrect): #Patrick
    """Display correct answers out of total answers"""
    grade = ("correct * 100)/ 10")
    print ('Your scored',grade, 'percent')
    if (grade > 70):
       print('Better luck next time',name)

    if (grade < 80):
       print('Good Job', name,' You Are A Sports Genius')

def main_loop (): #Jade
    """Using questions, randomize questions, ask players questions, display results"""
    display_title()
    display_directions()
    questions_and_answers = [('Who has the most total touchdowns on the New England Patriots as of 2015?','rob gronkowski'),('Which country won the 2015 Womens FIFA World Cup?','united states'),('What is the name of the penalty in hockey when a player hits another player with the hockey stick?','high stick'),('What is Bostons NBA basketball team?','celtics'),('In basketball what is a basket from the court halfline worth?','3 points'),('Which MLB baseball team won the World Series in 2013?','red sox'),('What is three strikes in a row in bowling called?','turkey'),('In track and field what is the event where someone jumps over obstacles while racing?','hurdles'),('What is the name of Americas largest skateboarding conversation?','x games'),('What does NASCAR stand for?','national association for stock car auto racig')]
    random_shuffle(questions_and_answers)
    results = []
    for q_and_a in questions_and_answers:
        question = q_and_a[0]
        answer = q_and_a[1]
        display_question(question, answer, correct)
    display_results(answers)
    results = []
    play_game(display_title, randomize_questions, display_questions, display_results)

main_loop()


