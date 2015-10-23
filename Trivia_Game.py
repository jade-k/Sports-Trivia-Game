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
