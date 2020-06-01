import random

silent_answer = ["*shrugs*", "*silence*", "*stoic face combined with silence*", "*annyoed silence*"]

question_answer = ["What can I have to eat?", "When can I get a new book?", "When are we going back to New York?"]

statement_answer = ["Nah", "No", "One second", "Yeah, let me just finish this first", "Please stop pestering me about this", "Did Mom put you up to this?"]

food_answer = ["I'm good with anything", "Can I have desert?", "What can I have to eat?"]

def create_speech(user_statement, answer, num):
    # this is not a pure function because it's nondeterministic but that's
    # okay because it's intended functionality
    
    # handle this case first and exit early if it fails
    if answer not in user_statement:
        return None
        
    if num == 1:
        return random.choice(silent_answer)
    elif num == 2:
        return random.choice(statement_answer)    
    else:
        return "\n".join((random.choice(statement_answer), random.choice(question_answer)))
        
while True:
    num = random.randint(1,3)

    user_statement = input("")

    answers = ["ACT", "grade", "school"]
    for i in answers:
        response = create_speech(user_statement=user_statement, answer=i, num=num) 
        if response is not None:
            print(response)

    if "food" or "Food" in user_statement:
        print(random.choice(food_answer))
    # This if statement handles all questions with the word "food" in them


    if "add" in user_statement:
        question_answer.append("orange")
        print(question_answer[-1])
    # This will write to the above answers

    if ("remove" in user_statement):
        # trying to remove "orange" will fail if "orange" is not already in the list
        question_answer.pop()
        print(question_answer[-1])
    # This will remove one of the above answers