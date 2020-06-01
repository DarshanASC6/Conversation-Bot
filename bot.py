import random

silent_answer = ["*shrugs*", "*silence*", "*stoic face combined with silence*", "*annyoed silence*"]

question_answer = ["What can I have to eat?", "When can I get a new book?", "When are we going back to New York?"]

statement_answer = ["Nah", "No", "One second", "Yeah, let me just finish this first", "Please stop pestering me about this", "Did Mom put you up to this?"]

food_answer = ["I'm good with anything", "Can I have desert?", "What can I have to eat?"]

answers = ["ACT", "grade", "Grade", "school", "School"]

def create_speech(user_statement, answer, num):

    if answer not in user_statement:
        return None

    if num == 1:
        return random.choice(silent_answer)
    elif num == 2:
        return random.choice(statement_answer)    
    else:
        return random.choice(question_answer)

while True:

    num = random.randint(1,3)

    user_statement = input("")

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
        print(question_answer)
    # This will write to the above answers

    if ("remove" in user_statement):
        question_answer.pop()
        print(question_answer[-1])
        print(question_answer)
    # This will remove one of the above answers