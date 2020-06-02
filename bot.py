import random

silent_answer = ["*shrugs*", "*silence*", "*stoic face combined with silence*", "*annyoed silence*"]

question_answer = ["What can I have to eat?", "When can I get a new book?", "When are we going back to New York?"]

statement_answer = ["Nah", "No", "One second", "Yeah, let me just finish this first", "Please stop pestering me about this", "Did Mom put you up to this?"]

food_answer = ["I'm good with anything", "Can I have desert?", "What can I have to eat?"]

greeting_answer = ["Hello", "Ayo", "Sup?"] 

keywords = ["ACT", "grade", "Grade", "school", "School"]

def create_speech(user_statement, answer, num):

    if answer not in user_statement:
        return None

    if num == 1:
        return random.choice(silent_answer)
    elif num == 2:
        return random.choice(statement_answer)    
    else:
        return random.choice(question_answer)

def add():
    x = user_statement.split(" ")

    answer = x[1]
    
    array_name = x[2]
    
    array_name.append(answer)
    # Error in the code
    
    print("added",answer,"to", array_name)


while True:

    num = random.randint(1,3)

    user_statement = input("")

    for i in keywords:
        response = create_speech(user_statement=user_statement, answer=i, num=num) 
        if response is not None:
            print(response)

    if ("food" or "Food") in user_statement:
        print(random.choice(food_answer))
    # This if statement handles all questions with the word "food" in them

    if "add" in user_statement:
        add()
    # This will write to the above answers

    if ("remove" in user_statement):
        question_answer.pop()
    # This will remove one of the above answers

    if ("show" in user_statement):
        print(keywords)

    if ("help" in user_statement):
        print("poo")
    # This will display a list of commands that can be given