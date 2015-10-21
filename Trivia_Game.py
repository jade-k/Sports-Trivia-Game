def display_title ():
    """print the title using the player's name"""
    print raw_input('What is your name?')
    print('Welcome to the Ultimate Sports Trivia Game',name)

def randomize_questions (questions):
    """Take all the questions and randomize them"""
    # Write code here
    print 'what?'

def display_question (question, answer):
    """Display question. Get user answer. Return True if correct."""
    # Write code here
    return True # FIXME

def display_results (answers):
    """Display correct answers out of total answers"""
    # Write code here



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
